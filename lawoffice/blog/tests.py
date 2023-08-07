from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.core.files.uploadedfile import SimpleUploadedFile
from .views import BlogHomePage, SinglePost
from .models import Tag, Post, Comment
from .forms import CommentForm

from datetime import date
# Create your tests here.


class BlogHomePageTest(TestCase):

    def setUp(self):
        self.Post = Post.objects.create(
            title='Test name',
            excerpt='Test short excerpt',
            slug='test-name',
            image=SimpleUploadedFile('test_post_image.jpg', b'Image content')
        )
        self.url = reverse('blog')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_blog_home_url(self):
        self.assertEqual(resolve(self.url).func.view_class, BlogHomePage.as_view().view_class)

    def test_blog_home_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_blog_home_view_template(self):
        self.assertTemplateUsed(self.response, 'blog/blog-main-page.html')

    def test_blog_home_content(self):
        self.assertContains(self.response, self.Post.title)
        self.assertContains(self.response, self.Post.excerpt)
        self.assertContains(self.response, self.Post.image)
        self.assertTrue(self.Post.image.name.endswith('.jpg'))

class PostDetailTest(TestCase):
    def setUp(self):
        self.Tag = Tag.objects.create(
            caption='Test tag'
        )
        self.Post = Post.objects.create(
            title='Test name',
            date=date.today().strftime('%d.%m.%Y'),
            slug='test-name',
            content='Test description',
            image=SimpleUploadedFile('test_post_image.jpg', b'Image content')
        )
        self.Post.tag.add(self.Tag)
        self.Comment = Comment.objects.create(
            user_name='Test name',
            text='Test message',
            post=self.Post,
            date=date.today().strftime('%d.%m.%Y')
        )
        self.url = reverse('post-detail', args=[self.Post.slug])
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_post_detail_url(self):
        self.assertEqual(resolve(self.url).func.view_class, SinglePost.as_view().view_class)

    def test_post_detail_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_detail_view_template(self):
        self.assertTemplateUsed(self.response, 'blog/post-detail.html')

    def test_post_detail_content_tag(self):
        self.assertContains(self.response, self.Tag)

    def test_post_detail_content_post(self):
        self.assertContains(self.response, self.Post.title)
        expected_date = self.Post.date.strftime('%d.%m.%Y')
        self.assertContains(self.response, expected_date)
        self.assertContains(self.response, self.Post.content)
        self.assertContains(self.response, self.Post.image)
        self.assertTrue(self.Post.image.name.endswith('.jpg'))

    def test_post_detail_comment(self):
        self.assertContains(self.response, self.Comment.user_name)
        self.assertContains(self.response, self.Comment.text)
        expected_date = self.Comment.date.strftime('%d.%m.%Y')
        self.assertContains(self.response, expected_date)


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            caption = 'Test caption'
        )

    def test_tag_model(self):
        self.assertTrue(isinstance(self.tag, Tag))
        self.assertTrue(self.tag.caption, 'Test caption')


class PostModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            caption='Test caption'
        )
        self.post = Post.objects.create(
            title='Test title',
            excerpt='Test excerpt',
            date=date.today().strftime('%d.%m.%Y'),
            slug='test-title',
            content='Test content',
        )
        self.post.tag.add(self.tag)

    def test_post_model(self):
        self.assertTrue(isinstance(self.post, Post))
        self.assertTrue(self.post.title, 'Test title')
        self.assertTrue(self.post.excerpt, 'Test excerpt')
        self.assertTrue(self.post.date, date.today().strftime('%d.%m.%Y'))
        self.assertTrue(self.post.slug, 'test-title')
        self.assertTrue(self.post.content, 'Test content')
        self.assertTrue(self.post.tag, self.tag)


class CommentModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            caption='Test caption'
        )
        self.post = Post.objects.create(
            title='Test title',
            excerpt='Test excerpt',
            date=date.today().strftime('%d.%m.%Y'),
            slug='test-title',
            content='Test content',
        )
        self.post.tag.add(self.tag)
        self.comment = Comment.objects.create(
            user_name='Test username',
            user_email='test@test.com',
            text='Test text',
            post=self.post,
            date=date.today().strftime('%d.%m.%Y'),
        )

    def test_comment_model(self):
        self.assertTrue(isinstance(self.comment, Comment))
        self.assertTrue(self.comment.user_name, 'Test username')
        self.assertTrue(self.comment.user_email, 'test@test.com')
        self.assertTrue(self.comment.text, 'Test text')
        self.assertTrue(self.comment.post, self.post)
        self.assertTrue(self.comment.date, date.today().strftime('%d.%m.%Y'))

class CommentFormTest(TestCase):
    def setUp(self):
        self.data_valid = {
            'user_name': 'Test name',
            'user_email': 'test_email@test.com',
            'text': 'Test last name',
        }
        self.data_invalid = {
            'user_name': 'Test name',
            'user_email': 'test',
            'text': 'Test last name',
        }
        self.contact_from_valid = CommentForm(data=self.data_valid)
        self.contact_from_invalid = CommentForm(data=self.data_invalid)

    def test_contact_form_valid(self):
        self.assertTrue(self.contact_from_valid.is_valid())

    def test_contact_form_invalid(self):
        self.assertFalse(self.contact_from_invalid.is_valid())