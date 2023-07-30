from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import ShopHomePage, Contracts, Lawsuit, Writings, ItemDetail, cart_view
from .models import Document, Item, Cart

# Create your tests here.


class ShopHomeTest(TestCase):

    def setUp(self):
        self.Document_contract = Document.objects.create(type='Umowa')
        self.Document_writing = Document.objects.create(type='Pismo')
        self.Document_lawsuit = Document.objects.create(type='Pozew')

        self.Item_contract = Item.objects.create(
            name='Test name contract',
            slug='test-name-contract',
            price='10',
            type=self.Document_contract
        )
        self.Item_writing = Item.objects.create(
            name='Test name writing',
            slug='test-name-writing',
            price='10',
            type=self.Document_writing
        )
        self.Item_lawsuit = Item.objects.create(
            name='Test name lawsuit',
            slug='test-name-lawsuit',
            price='10',
            type=self.Document_lawsuit
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
        self.assertEqual(self.Document_contract.type, 'Umowa')
        self.assertEqual(self.Document_writing.type, 'Pismo')
        self.assertEqual(self.Document_lawsuit.type, 'Pozew')

    def test_shop_home_item(self):
        self.assertEqual(self.Item_contract.type, self.Document_contract)
        self.assertEqual(self.Item_writing.type, self.Document_writing)
        self.assertEqual(self.Item_lawsuit.type, self.Document_lawsuit)


class ContractsTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='Umowa'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            type=self.Document,
            price='10.00'
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

    # def test_contracts_

class LawsuitsTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='Pozew'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            type=self.Document,
            price=10.00
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

class WritingsTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='Pismo'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            type=self.Document,
            price=10.00
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
            price=10.00
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
            price=10.00
        )
        self.url = reverse('lawsuit-detail', kwargs={'slug': self.Item.slug})
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
            price=10.00
        )
        self.url = reverse('writing-detail', kwargs={'slug': self.Item.slug})
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


class CartTest(TestCase):
    def setUp(self):
        self.Document = Document.objects.create(
            type='pisma'
        )
        self.Item = Item.objects.create(
            name='Test name',
            slug='test-name',
            description='Test description',
            type=self.Document,
            price=10.00
        )
        self.Cart = Cart.objects.create(
            item=self.Item,
            quantity=1
        )
        self.url = reverse('cart')
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_cart_url(self):
        self.assertEqual(resolve(self.url).func, cart_view)

    def test_cart_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_cart_view_template(self):
        self.assertTemplateUsed(self.response, 'shop/cart.html')

    def test_cart_view_content(self):
        self.assertContains(self.response, self.Item.name)
        self.assertContains(self.response, str(self.Cart.quantity))
        self.assertContains(self.response, str(self.Item.price))
        total_price = str(self.Cart.quantity*self.Item.price)
        self.assertContains(self.response, total_price)

