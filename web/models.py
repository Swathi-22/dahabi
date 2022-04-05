

from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify

class Banner(models.Model):
    title=models.CharField(max_length=225)
    heading=models.CharField(max_length=200)
    image = VersatileImageField('Image',upload_to='index/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Banner")

    def __str__(self):
        return self.title


class Category(models.Model):
    title_in_arabic = models.CharField(max_length=225)
    # slug=models.SlugField(unique=True)
    title_in_english =models.CharField(max_length=225)
    is_active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return str(self.title_in_arabic)


class Product(models.Model):
    
    title=models.CharField(max_length=225)
    # offerprice=models.FloatField(blank=True,null=True)
    price=models.FloatField()
    cal = models.CharField(max_length=128)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = VersatileImageField('Image',upload_to='product/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    is_popular=models.BooleanField(default=False)
    slug=models.SlugField(unique=True)

    # def get_offer(self):
    #     if self.price == self.offerprice:
    #         return 0
    #     return round(100*(self.price - self.offerprice) / self.price ,2)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = VersatileImageField('Image',upload_to='gallery/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return str(self.image)


class Contact(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    feedback=HTMLField(blank=True, null=True)

    def __str__(self):
        return self.firstname



class Offer(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image = VersatileImageField('Image',upload_to='offer/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return self.title


class Vat(models.Model):
    vat_price = models.CharField(max_length=100)

    def __str__(self):
        return str(self.vat_price)
