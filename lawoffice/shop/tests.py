from django.test import TestCase, Client, TransactionTestCase
from django.urls import reverse, resolve
from django.core.files.uploadedfile import SimpleUploadedFile
from .views import ShopHomePage, Contracts, Lawsuit, Writings, ItemDetail, cart_view, add_to_cart
from .models import Document, Item, Cart

from datetime import date
# Create your tests here.


class ShopHomeTest(TestCase):

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

        self.url = reverse('shop')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_shop_home_url(self):
        self.assertEqual(resolve(self.url).func.view_class, ShopHomePage.as_view().view_class)

    def test_shop_home_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_shop_home_view_template(self):
        self.assertTemplateUsed(self.response, 'shop/shop-main-page.html')

    def test_shop_home_content_document(self):
        self.assertContains(self.response, self.Document_contract.type)
        self.assertContains(self.response, self.Document_contract.image)
        self.assertTrue(self.Document_contract.image.name.endswith('.jpg'))

        self.assertContains(self.response, self.Document_writing.type)
        self.assertContains(self.response, self.Document_writing.image)
        self.assertTrue(self.Document_writing.image.name.endswith('.jpg'))

        self.assertContains(self.response, self.Document_lawsuit.type)
        self.assertContains(self.response, self.Document_lawsuit.image)
        self.assertTrue(self.Document_lawsuit.image.name.endswith('.jpg'))


class ContractsTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='Umowy'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            type=self.Document,
            price='10.00',
            image=SimpleUploadedFile('test_item_image.jpg', b'Image content')

        )
        self.url = reverse('contracts')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_contracts_url(self):
        self.assertEqual(resolve(self.url).func.view_class, Contracts.as_view().view_class)

    def test_contracts_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contracts_view_template(self):
        self.assertTemplateUsed(self.response, 'shop/contracts-view.html')

    def test_contracts_content(self):
        self.assertContains(self.response, self.Item.name)
        self.assertContains(self.response, self.Item.image)
        self.assertTrue(self.Item.image.name.endswith('.jpg'))


class LawsuitsTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='Pozwy'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            type=self.Document,
            price=10.00,
            image=SimpleUploadedFile('test_item_image.jpg', b'Image content')
        )
        self.url = reverse('lawsuits')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_lawsuits_url(self):
        self.assertEqual(resolve(self.url).func.view_class, Lawsuit.as_view().view_class)

    def test_lawsuits_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_lawsuits_view_template(self):
        self.assertTemplateUsed(self.response, 'shop/lawsuits-view.html')

    def test_lawsuits_content(self):
        self.assertContains(self.response, self.Item.name)
        self.assertContains(self.response, self.Item.image)
        self.assertTrue(self.Item.image.name.endswith('.jpg'))

class WritingsTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='Pisma'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            type=self.Document,
            price=10.00,
            image=SimpleUploadedFile('test_item_image.jpg', b'Image content')
        )
        self.url = reverse('writings')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_writings_url(self):
        self.assertEqual(resolve(self.url).func.view_class, Writings.as_view().view_class)

    def test_writings_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_writings_view_template(self):
        self.assertTemplateUsed(self.response, 'shop/writings-view.html')

    def test_writings_content(self):
        self.assertContains(self.response, self.Item.name)
        self.assertContains(self.response, self.Item.image)
        self.assertTrue(self.Item.image.name.endswith('.jpg'))

class ItemDetailContractTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='umowy'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            description='Test description',
            type=self.Document,
            price=10.00,
            file=SimpleUploadedFile('test_item_file.pdf', b'File content'),
            image=SimpleUploadedFile('test_item_image.jpg', b'Image content')
        )
        self.url = reverse('contract-detail', kwargs={'slug': self.Item.slug})
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_item_detail_contract_url(self):
        self.assertEqual(resolve(self.url).func.view_class, ItemDetail.as_view().view_class)

    def test_item_detail_contract_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_item_detail_contract_view_template(self):
        self.assertTemplateUsed(self.response, 'shop/item-detail.html')

    def test_item_detail_contract_content(self):
        self.assertContains(self.response, self.Item.name)
        self.assertContains(self.response, self.Item.description)
        self.assertContains(self.response, str(self.Item.price))
        self.assertContains(self.response, self.Item.image)
        self.assertTrue(self.Item.image.name.endswith('.jpg'))
        self.assertTrue(self.Item.file.name.endswith('.pdf'))

class ItemDetailLawsuitTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='pozwy'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            description='Test description',
            type=self.Document,
            price=10.00,
            file=SimpleUploadedFile('test_item_file.pdf', b'File content'),
            image=SimpleUploadedFile('test_item_image.jpg', b'Image content')
        )
        self.url = reverse('lawsuit-detail', kwargs={'slug': self.Item.slug})
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_item_detail_lawsuit_url(self):
        self.assertEqual(resolve(self.url).func.view_class, ItemDetail.as_view().view_class)

    def test_item_detail_lawsuit_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_item_detail_lawsuit_view_template(self):
        self.assertTemplateUsed(self.response, 'shop/item-detail.html')

    def test_item_detail_lawsuit_content(self):
        self.assertContains(self.response, self.Item.name)
        self.assertContains(self.response, self.Item.description)
        self.assertContains(self.response, str(self.Item.price))
        self.assertContains(self.response, self.Item.image)
        self.assertTrue(self.Item.image.name.endswith('.jpg'))
        self.assertTrue(self.Item.file.name.endswith('.pdf'))


class ItemDetailWritingTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='pisma'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            description='Test description',
            type=self.Document,
            price=10.00,
            file=SimpleUploadedFile('test_item_file.pdf', b'File content'),
            image=SimpleUploadedFile('test_item_image.jpg', b'Image content')
        )
        self.url = reverse('writing-detail', kwargs={'slug': self.Item.slug})
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_item_detail_writing_url(self):
        self.assertEqual(resolve(self.url).func.view_class, ItemDetail.as_view().view_class)

    def test_item_detail_writing_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_item_detail_writing_view_template(self):
        self.assertTemplateUsed(self.response, 'shop/item-detail.html')

    def test_item_detail_writing_content(self):
        self.assertContains(self.response, self.Item.name)
        self.assertContains(self.response, self.Item.description)
        self.assertContains(self.response, str(self.Item.price))
        self.assertContains(self.response, self.Item.image)
        self.assertTrue(self.Item.image.name.endswith('.jpg'))
        self.assertTrue(self.Item.file.name.endswith('.pdf'))


class CartTest(TestCase):
    def setUp(self):
        self.url = reverse('cart')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_cart_url(self):
        self.assertEqual(resolve(self.url).func, cart_view)

    def test_cart_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_cart_view_template(self):
        self.assertTemplateUsed(self.response, 'shop/cart.html')
class AddT0CartTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.Document = Document.objects.create(
            type='pisma'
        )
        self.item = Item.objects.create(
            name='Test name',
            slug='test-name',
            type=self.Document,
            price=10.00,
        )
    def test_add_to_cart_url(self):
        url = reverse('add-to-cart', args=[self.item.slug])
        self.assertEqual(resolve(url).func, add_to_cart)
    def test_add_to_cart_view(self):
        url = reverse('add-to-cart', args=[self.item.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    def test_add_to_cart(self):
        url = reverse('add-to-cart', args=[self.item.slug])
        response = self.client.get(url)
        cart = Cart.objects.get(item=self.item)
        self.assertEqual(cart.item, self.item)
        self.assertEqual(cart.quantity, 1)


class DocumentModelTest(TestCase):
    def setUp(self):
        self.document = Document.objects.create(
            type='Test type'
        )

    def test_document_model(self):
        self.assertTrue(isinstance(self.document, Document))
        self.assertTrue(self.document.type, 'Test type')


class ItemModelTest(TestCase):
    def setUp(self):
        self.document = Document.objects.create(
            type='Test type'
        )
        self.item = Item.objects.create(
            name='Test name',
            slug='test-name',
            description='Test description',
            type= self.document,
            price=10
        )

    def test_document_model(self):
        self.assertTrue(isinstance(self.item, Item))
        self.assertTrue(self.item.name, 'Test name')
        self.assertTrue(self.item.slug, 'test-name')
        self.assertTrue(self.item.description, 'Test description')
        self.assertTrue(self.item.type, self.document)
        self.assertTrue(self.item.price, 10)


class CartModelTest(TestCase):
    def setUp(self):
        self.document = Document.objects.create(
            type='Test type'
        )
        self.item = Item.objects.create(
            name='Test name',
            slug='test-name',
            description='Test description',
            type= self.document,
            price=10
        )
        self.cart = Cart.objects.create(
            session_id='Test session',
            item=self.item,
            quantity=1,
            created_at=date.today()
        )

    def test_document_model(self):
        self.assertTrue(isinstance(self.cart, Cart))
        self.assertTrue(self.cart.session_id, 'Test session')
        self.assertTrue(self.cart.item, self.item)
        self.assertTrue(self.cart.quantity, 1)
        self.assertTrue(self.cart.created_at, date.today())
