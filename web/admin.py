from django.contrib import admin
from .models import Banner,Category,Product,Gallery,Contact,Offer,Vat


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'heading',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'image',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'image',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'username',)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ( 'title',)

@admin.register(Vat)
class VatAdmin(admin.ModelAdmin):
    pass
