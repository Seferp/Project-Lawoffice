from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import Home, about_me_view, contact_view, FAQ, Specializations, SpecializationsDetail,\
    privacy_policy_view, information_clause_view
from .models import FAQ as FAQ_model, Specialization
from blog.models import Post
from shop.models import Document

from datetime import date
# Create your tests here.


class HomeTest(TestCase):

    def setUp(self):

        self.Document_contract = Document.objects.create(type='Umowa')
        self.Document_writing = Document.objects.create(type='Pismo')
        self.Document_lawsuit = Document.objects.create(type='Pozew')

        self.Specialization = Specialization.objects.create(
            name='Test',
            slug='test'
        )
        self.Post = Post.objects.create(
            title='Test title',
            excerpt='Test short excerpt',
            date=date.today().strftime('%d.%m.%Y'),
            slug='test-title',
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

    def test_home_content_post(self):
        self.assertContains(self.response, self.Post.title)
        self.assertContains(self.response, self.Post.excerpt)
        expected_date = self.Post.date.strftime('%d.%m.%Y')
        self.assertContains(self.response, expected_date)

    def test_home_content_document(self):
        self.assertEqual(self.Document_contract.type, 'Umowa')
        self.assertEqual(self.Document_writing.type, 'Pismo')
        self.assertEqual(self.Document_lawsuit.type, 'Pozew')

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
            slug='test'
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


class SpecializationDetailTest(TestCase):
    def setUp(self):
        self.specialization = Specialization.objects.create(
            name='Test',
            description='Test description',
            excerpt='Test excerpt',
            slug='test'
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
        self.assertContains(self.response, self.specialization.description)


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
