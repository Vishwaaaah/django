from django.contrib import admin
from django.urls import path
from home import views
from home.models import Contact
# Register your models here.
admin.site.register(Contact)
