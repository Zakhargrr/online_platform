from django.db import models


# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='название продукта')
    model = models.CharField(max_length=20, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода')

    def __str__(self):
        return f"{self.product_name} (модель {self.model})"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


CATEGORY_CHOICES = [
    ("Завод", "Завод"),
    ("Розничная сеть", "Розничная сеть"),
    ("ИП", "ИП"),
]


class NetworkNode(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=30, verbose_name='страна')
    city = models.CharField(max_length=30, verbose_name='город')
    street = models.CharField(max_length=30, verbose_name='улица')
    house_number = models.CharField(max_length=30,
                                    verbose_name='номер дома')  # тип char, т.к. есть номера домов с буквами (24А и тд.)
    products = models.ManyToManyField(Product, verbose_name='продукты')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL,
                                 null=True, blank=True, verbose_name='поставщик')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, verbose_name='категория')
    debt = models.FloatField(verbose_name='задолженность', default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f"{self.category} {self.name} - долг {self.debt}"

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'
