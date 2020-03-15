from django.contrib import admin
from .models import *


class AdminSectionGeneral(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


class AdminGeneralServices(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


class AdminServices(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 4:
            return False
        else:
            return True


class AdminAboutMe(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


class AdminContacts(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


admin.site.register(SectionGeneral, AdminSectionGeneral)
admin.site.register(GeneralServices, AdminGeneralServices)
admin.site.register(Services, AdminServices)
admin.site.register(AboutMe, AdminAboutMe)
admin.site.register(Works)
admin.site.register(Review)
admin.site.register(CheckedTime)
admin.site.register(CheckedDate)
admin.site.register(Contacts, AdminContacts)
admin.site.register(Information)

