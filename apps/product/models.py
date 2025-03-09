from django.db import models
from slugify import slugify
import uuid
# Create your models here.

class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название товара"
    )
    slug = models.TextField(
        verbose_name="SLUG",
        unique=True
    )
    description = models.TextField(
        verbose_name="Описание товара"
    )
    price = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        verbose_name="Цена"
    )
    is_active = models.BooleanField(
        verbose_name="Активный",
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания товара",
        null=True
    )
    
    def __str__(self):
        return self.title
    
    def get_first_image(self) -> 'ProductImage':
        product_image = ProductImage.objects.filter(product=self).first()
        return product_image.image.url if product_image else None
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            while Product.objects.filter(slug=self.slug).exists():
                unique_suffix = uuid.uuid4().hex[:6]
                self.slug = f"{base_slug}-{unique_suffix}"

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        
class ProductImage(models.Model):
    product = models.ForeignKey(
        to="Product",
        on_delete=models.CASCADE,
        verbose_name="Изображение",
        related_name="product"
    )
    image = models.ImageField(
        upload_to="product_image/",
        verbose_name="Изображение"
    )
    position = models.PositiveIntegerField(
        default=0,
        blank=True, null=True
    )
    
    def __str__(self):
        return str(self.image.name)
    
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ['position', ]


# Модель для Категории
class Category(models.Model):
    name = models.CharField(max_length=155, unique=True)
    desciotion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name