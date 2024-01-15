from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MyUser)


# # admin.py
# from django.contrib import admin
# from django import forms
# from django_countries.fields import CountryField
# from django_countries.widgets import CountrySelectWidget
# from django.contrib.auth.admin import UserAdmin
# from .models import MyUser

# class MyUserAdminForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         widgets = {
#             'country': CountrySelectWidget(),
#         }

# class MyUserAdmin(UserAdmin):
#     form = MyUserAdminForm
#     list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'country')
#     fieldsets = UserAdmin.fieldsets + (
#         ('Additional Information', {'fields': ('country',)}),
#     )

# admin.site.register(MyUser, MyUserAdmin)
