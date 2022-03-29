from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms

from .models import Image, Collection, Product, Colors


class ImageInLine(admin.TabularInline):
    model = Image
    max_num = 8
    min_num = 0


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), label=Product._meta.get_field('description').verbose_name)

    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        if self.cleaned_data['colors']:
            if len(self.cleaned_data.get('colors')) > 8:
                raise forms.ValidationError('The number of colors cannot exceed 8!')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, ]
    form = ProductForm


admin.site.register(Collection)
admin.site.register(Colors)
