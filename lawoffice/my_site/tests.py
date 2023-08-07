from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import Home, about_me_view, contact_view, FAQ, Specializations, SpecializationsDetail,\
    privacy_policy_view, information_clause_view
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import FAQ as FAQ_model, Specialization, Contact
from.forms import ContactForm
from blog.models import Post
from shop.models import Document

from datetime import date

# Create your tests here.


class HomeTest(TestCase):

    def setUp(self):

        self.Document_contract = Document.objects.create(
            type='Umowy',
            image=SimpleUploadedFile('test_contract_image.jpg', b'Image content')
        )
        self.Document_writing = Document.objects.create(
            type='Pisma',
            image=SimpleUploadedFile('test_writing_image.jpg', b'Image content')
        )
        self.Document_lawsuit = Document.objects.create(
            type='Pozwy',
            image=SimpleUploadedFile('test_lawsuit_image.jpg', b'Image content')
        )

        self.Specialization = Specialization.objects.create(
            name='Test',
            slug='test',
            image=SimpleUploadedFile('test_specialization_image.jpg', b'Image content')
        )
        self.Post = Post.objects.create(
            title='Test title',
            excerpt='Test short excerpt',
            date=date.today().strftime('%d.%m.%Y'),
            slug='test-title',
            image=SimpleUploadedFile('test_post_image.jpg', b'Image content')
        )
        self.url = reverse('home')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_home_url(self):
        self.assertEqual(resolve(self.url).func.view_class, Home.as_view().view_class)

    def test_home_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_view_template(self):
        self.assertTemplateUsed(self.response, 'my_site/home.html')

    def test_home_content_specialization(self):
        self.assertContains(self.response, self.Specialization.name)
        self.assertContains(self.response, self.Specialization.image)
        self.assertTrue(self.Specialization.image.name.endswith('.jpg'))

    def test_home_content_post(self):
        self.assertContains(self.response, self.Post.title)
        self.assertContains(self.response, self.Post.excerpt)
        expected_date = self.Post.date.strftime('%d.%m.%Y')
        self.assertContains(self.response, expected_date)
        self.assertContains(self.response, self.Post.image)
        self.assertTrue(self.Post.image.name.endswith('.jpg'))

    def test_home_content_shop(self):
        self.assertContains(self.response, self.Document_contract.type)
        self.assertContains(self.response, self.Document_contract.image)
        self.assertTrue(self.Document_contract.image.name.endswith('.jpg'))

        self.assertContains(self.response, self.Document_writing.type)
        self.assertContains(self.response, self.Document_writing.image)
        self.assertTrue(self.Document_writing.image.name.endswith('.jpg'))

        self.assertContains(self.response, self.Document_lawsuit.type)
        self.assertContains(self.response, self.Document_lawsuit.image)
        self.assertTrue(self.Document_lawsuit.image.name.endswith('.jpg'))


class AboutMeTest(TestCase):
    def setUp(self):
        self.url = reverse('about-me')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_about_me_url(self):
        self.assertEqual(resolve(self.url).func, about_me_view)

    def test_about_me_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_me_view_template(self):
        self.assertTemplateUsed(self.response, 'my_site/about-me.html')


class ContactTest(TestCase):
    def setUp(self):
        self.url = reverse('contact')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_contact_url(self):
        self.assertEqual(resolve(self.url).func, contact_view)

    def test_contact_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contact_view_template(self):
        self.assertTemplateUsed(self.response, 'my_site/contact.html')


class FaqTest(TestCase):
    def setUp(self):
        self.faq = FAQ_model.objects.create(
            question='TEST?',
            answer='TEST'
        )
        self.url = reverse('faq')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_faq_url(self):
        self.assertEqual(resolve(self.url).func.view_class, FAQ.as_view().view_class)

    def test_faq_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_faq_view_template(self):
        self.assertTemplateUsed(self.response, 'my_site/faq.html')

    def test_faq_content(self):
        self.assertContains(self.response, self.faq.question)
        self.assertContains(self.response, self.faq.answer)


class SpecializationTest(TestCase):
    def setUp(self):
        self.Specialization = Specialization.objects.create(
            name='Test',
            excerpt='Test excerpt',
            slug='test',
            image=SimpleUploadedFile('test_specialization_image.jpg', b'Image content')
        )
        self.url = reverse('specialization')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_specialization_url(self):
        self.assertEqual(resolve(self.url).func.view_class, Specializations.as_view().view_class)

    def test_specialization_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_specialization_view_template(self):
        self.assertTemplateUsed(self.response, 'my_site/specialization.html')

    def test_specialization_content(self):
        self.assertContains(self.response, self.Specialization.name)
        self.assertContains(self.response, self.Specialization.excerpt)
        self.assertContains(self.response, self.Specialization.image)
        self.assertTrue(self.Specialization.image.name.endswith('.jpg'))


class SpecializationDetailTest(TestCase):
    def setUp(self):
        self.specialization = Specialization.objects.create(
            name='Test',
            description='Test description',
            excerpt='Test excerpt',
            slug='test',
            image=SimpleUploadedFile('test_specialization_image.jpg', b'Image content')
        )
        self.url = reverse('specialization-detail', kwargs={'slug': self.specialization.slug})
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_specialization_detail_url(self):
        self.assertEqual(resolve(self.url).func.view_class, SpecializationsDetail.as_view().view_class)

    def test_specialization_detail_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_specialization_detail_view_template(self):
        self.assertTemplateUsed(self.response, 'my_site/specialization-detail.html')

    def test_specialization_detail_content(self):
        self.assertContains(self.response, self.specialization.name)
        self.assertContains(self.response, self.specialization.description)
        self.assertContains(self.response, self.specialization.image)
        self.assertTrue(self.specialization.image.name.endswith('.jpg'))


class InformationClauseTest(TestCase):
    def setUp(self):
        self.url = reverse('information-clause')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_information_clause_url(self):
        self.assertEqual(resolve(self.url).func, information_clause_view)

    def test_information_clause_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_information_clause_view_template(self):
        self.assertTemplateUsed(self.response, 'my_site/information-clause.html')


class PrivacyPolicyTest(TestCase):
    def setUp(self):
        self.url = reverse('privacy-policy')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_privacy_policy_url(self):
        self.assertEqual(resolve(self.url).func, privacy_policy_view)

    def test_privacy_policy_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_privacy_policy_view_template(self):
        self.assertTemplateUsed(self.response, 'my_site/privacy-policy.html')


class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ_model.objects.create(
            question='Test question',
            answer='Test answer'
        )

    def test_faq_model(self):
        self.assertTrue(isinstance(self.faq, FAQ_model))
        self.assertEqual(self.faq.question, 'Test question')
        self.assertEqual(self.faq.answer, 'Test answer')


class SpecializationModelTest(TestCase):
    def setUp(self):
        self.specialization = Specialization.objects.create(
            name='Test name',
            description='Test description',
            excerpt='Test excerpt',
            slug='test-name',
        )

    def test_specialization_model(self):
        self.assertTrue(isinstance(self.specialization, Specialization))
        self.assertEqual(self.specialization.name, 'Test name')
        self.assertEqual(self.specialization.description, 'Test description')
        self.assertEqual(self.specialization.excerpt, 'Test excerpt')
        self.assertEqual(self.specialization.slug, 'test-name')


class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            first_name='Test name',
            last_name='Test last name',
            email='Test email',
            subject='Test subject',
            message='Test message'
        )

    def test_contact_model(self):
        self.assertTrue(isinstance(self.contact, Contact))
        self.assertTrue(self.contact.first_name, 'Test name')
        self.assertTrue(self.contact.last_name, 'Test last name')
        self.assertTrue(self.contact.email, 'Test email')
        self.assertTrue(self.contact.subject, 'Test subject')
        self.assertTrue(self.contact.message, 'Test message')


class ContactFormTest(TestCase):
    def setUp(self):
        self.data_valid = {
            'first_name': 'Test name',
            'last_name': 'Test last name',
            'email': 'test_email@test.com',
            'subject': 'Test subject',
            'message': 'Test message'
        }
        self.data_invalid = {
            'first_name': 'Test name',
            'last_name': 'Test last name',
            'email': 'test',
            'subject': 'Test subject',
            'message': 'Test message'
        }
        self.contact_from_valid = ContactForm(data=self.data_valid)
        self.contact_from_invalid = ContactForm(data=self.data_invalid)

    def test_contact_form_valid(self):
        self.assertTrue(self.contact_from_valid.is_valid())

    def test_contact_form_invalid(self):
        self.assertFalse(self.contact_from_invalid.is_valid())
