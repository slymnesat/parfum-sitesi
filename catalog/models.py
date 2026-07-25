from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="URL Slug")

    def save(self, *args, **kwargs):
        if not self.slug:
            # Tüm Türkçe karakterleri İngilizce karşılıklarına çeviriyoruz
            replacements = {
                'ı': 'i', 'İ': 'I', 'ş': 's', 'Ş': 'S',
                'ğ': 'g', 'Ğ': 'G', 'ç': 'c', 'Ç': 'C',
                'ö': 'o', 'Ö': 'O', 'ü': 'u', 'Ü': 'U'
            }
            temp_name = self.name
            for tr, eng in replacements.items():
                temp_name = temp_name.replace(tr, eng)
            self.slug = slugify(temp_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"


class Perfume(models.Model):
    name = models.CharField(max_length=200, verbose_name="Parfüm Adı")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori")
    description = models.TextField(verbose_name="Açıklama")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat (TL)")
    image = models.ImageField(upload_to='perfumes/', verbose_name="Ürün Görseli")
    is_active = models.BooleanField(default=True, verbose_name="Satışta mı?")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Parfüm"
        verbose_name_plural = "Parfümler"