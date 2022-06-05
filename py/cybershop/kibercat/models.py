from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'

    def __str__(self):
        return "%s" % self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, blank=True, null=True, default=None)
    name = models.CharField(max_length=64, db_index=True)
    article_name = models.CharField(max_length=64, db_index=True)
    discount = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, db_index=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Каталог товара'
        verbose_name_plural = 'Каталог товаров'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.pk

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
