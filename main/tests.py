from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Product, NetworkNode
from users.models import User


# Create your tests here.

class NetworkNodeTestCase(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create(
            email='test@mail.ru',
            first_name='Test',
            last_name='Test',
            password='12345'
        )
        self.client.force_authenticate(user)
        self.user = user

        Product.objects.create(
            product_name='test_product',
            model='test_model',
            release_date='2024-01-01'
        )

    def test_create_networknode(self):
        networknode1 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Завод',
        }

        response1 = self.client.post(
            '/create-networknode/',
            data=networknode1
        )
        self.assertEqual(
            response1.status_code,
            status.HTTP_201_CREATED
        )
        networknode2 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Завод',
            'supplier': [NetworkNode.objects.all().first().id]
        }

        response2 = self.client.post(
            '/create-networknode/',
            data=networknode2
        )
        self.assertEqual(
            response2.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode3 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Завод',
            'debt': 100
        }

        response3 = self.client.post(
            '/create-networknode/',
            data=networknode3
        )
        self.assertEqual(
            response3.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode4 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Розничная сеть',
            'supplier': NetworkNode.objects.all().first().id,
            'debt': 100
        }

        response4 = self.client.post(
            '/create-networknode/',
            data=networknode4
        )
        self.assertEqual(
            response4.status_code,
            status.HTTP_201_CREATED
        )

        networknode5 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Неправильная категория',
            'supplier': NetworkNode.objects.all().first().id,
            'debt': 100
        }

        response5 = self.client.post(
            '/create-networknode/',
            data=networknode5
        )
        self.assertEqual(
            response5.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode6 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Розничная сеть',
            'debt': 100
        }

        response6 = self.client.post(
            '/create-networknode/',
            data=networknode6
        )
        self.assertEqual(
            response6.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode7 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Розничная сеть',
            'supplier': NetworkNode.objects.all().last().id,
            'debt': 100
        }

        response7 = self.client.post(
            '/create-networknode/',
            data=networknode7
        )
        self.assertEqual(
            response7.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode8 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Розничная сеть',
            'supplier': NetworkNode.objects.all().first().id,
        }

        response8 = self.client.post(
            '/create-networknode/',
            data=networknode8
        )
        self.assertEqual(
            response8.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode9 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Розничная сеть',
            'supplier': NetworkNode.objects.all().first().id,
            'debt': -100
        }

        response9 = self.client.post(
            '/create-networknode/',
            data=networknode9
        )
        self.assertEqual(
            response9.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode10 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'ИП',
            'debt': 100
        }

        response10 = self.client.post(
            '/create-networknode/',
            data=networknode10
        )
        self.assertEqual(
            response10.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode11 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'ИП',
            'supplier': NetworkNode.objects.all().last().id,
            'debt': 100
        }

        response11 = self.client.post(
            '/create-networknode/',
            data=networknode11
        )
        self.assertEqual(
            response11.status_code,
            status.HTTP_201_CREATED
        )

        networknode12 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'ИП',
            'supplier': NetworkNode.objects.all().last().id,
            'debt': 100
        }

        response12 = self.client.post(
            '/create-networknode/',
            data=networknode12
        )
        self.assertEqual(
            response12.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode13 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'ИП',
            'supplier': NetworkNode.objects.all().first().id,
            'debt': 100
        }

        response13 = self.client.post(
            '/create-networknode/',
            data=networknode13
        )
        self.assertEqual(
            response13.status_code,
            status.HTTP_201_CREATED
        )

        networknode14 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'ИП',
            'supplier': NetworkNode.objects.all().first().id,
        }

        response14 = self.client.post(
            '/create-networknode/',
            data=networknode14
        )
        self.assertEqual(
            response14.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        networknode15 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'ИП',
            'supplier': NetworkNode.objects.all().first().id,
            'debt': -100
        }

        response15 = self.client.post(
            '/create-networknode/',
            data=networknode15
        )
        self.assertEqual(
            response15.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_update_networknode(self):
        Product.objects.create(
            product_name='test_product_name',
            model='test_model',
            release_date='2024-01-01'
        )
        networknode1 = {
            'name': 'test_name',
            'email': 'test_email@mail.ru',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 'test_house_number',
            'products': [Product.objects.all().last().id],
            'category': 'Завод',
        }
        self.client.post(
            '/create-networknode/',
            data=networknode1
        )

        update_field1 = {
            'name': 'new_name'
        }
        response1 = self.client.patch(
            f'/update-networknode/{NetworkNode.objects.all().last().id}/',
            data=update_field1
        )
        self.assertEqual(
            response1.status_code,
            status.HTTP_200_OK
        )

        update_field2 = {
            'category': 'ИП'
        }
        response2 = self.client.patch(
            f'/update-networknode/{NetworkNode.objects.all().last().id}/',
            data=update_field2
        )
        self.assertEqual(
            response2.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        update_field3 = {
            'supplier': f'{NetworkNode.objects.all().last().id}'
        }
        response3 = self.client.patch(
            f'/update-networknode/{NetworkNode.objects.all().last().id}/',
            data=update_field3
        )
        self.assertEqual(
            response3.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        update_field4 = {
            'debt': 1000
        }
        response4 = self.client.patch(
            f'/update-networknode/{NetworkNode.objects.all().last().id}/',
            data=update_field4
        )
        self.assertEqual(
            response4.status_code,
            status.HTTP_400_BAD_REQUEST
        )


class ProductTestCase(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create(
            email='test@mail.ru',
            first_name='Test',
            last_name='Test',
            password='12345'
        )
        self.client.force_authenticate(user)
        self.user = user

    def test_create_product(self):
        product = {
            'product_name': 'test_product_name',
            'model': 'test_model',
            'release_date': '2024-01-01'
        }
        response = self.client.post(
            '/create-product/',
            data=product
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
