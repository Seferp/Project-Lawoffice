from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import BlogHomePage, SinglePost
from .models import Tag, Post, Comment

from datetime import date
# Create your tests here.


class BlogHomePageTest(TestCase):

    def setUp(self):
        self.Post = Post.objects.create(
            title='Test name',
            excerpt='Test short excerpt',
            slug='test-name'
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

    def test_post_detail_comment(self):
        self.assertContains(self.response, self.Comment.user_name)
        self.assertContains(self.response, self.Comment.text)
        expected_date = self.Comment.date.strftime('%d.%m.%Y')
        self.assertContains(self.response, expected_date)