from django.contrib import admin

from solo.admin import SingletonModelAdmin

from .models import AboutUs, ImageAboutUs, News, Help, ImageHelp, Excellence, PublicOffer, Slider, Header, Footer, \
    AdminContacts, CallBack


class ImageAboutUsInLine(admin.TabularInline):
    model = ImageAboutUs
    max_num = 3
    min_num = 1


@admin.register(AboutUs)
class AboutUs(SingletonModelAdmin):
    inlines = [ImageAboutUsInLine, ]

    def has_add_permission(self, request):
        no_add = super().has_add_permission(request)
        if no_add and AboutUs.objects.exists():
            no_add = False
        return no_add

    class Meta:
        model = AboutUs


admin.site.register(News)
admin.site.register(Help)
admin.site.register(Excellence)


@admin.register(ImageHelp)
class ImageHelpAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        no_add = super().has_add_permission(request)
        if no_add and ImageHelp.objects.exists():
            no_add = False
        return no_add

    class Meta:
        model = ImageHelp


@admin.register(PublicOffer)
class PublicOffer(SingletonModelAdmin):
    def has_add_permission(self, request):
        no_add = super().has_add_permission(request)
        if no_add and PublicOffer.objects.exists():
            no_add = False
        return no_add

    class Meta:
        model = PublicOffer


@admin.register(Header)
class Header(SingletonModelAdmin):
    def has_add_permission(self, request):
        no_add = super().has_add_permission(request)
        if no_add and Header.objects.exists():
            no_add = False
        return no_add

    class Meta:
        model = Header


admin.site.register(Footer)
admin.site.register(Slider)
admin.site.register(AdminContacts)


class CallBackAdmin(admin.ModelAdmin):
    search_fields = ('name', 'phone',)
    list_display = ['name', 'phone', 'call_status', 'date_created']
    list_filter = ['call_status']


admin.site.register(CallBack, CallBackAdmin)







