from django.conf.urls import url, include
from django.contrib import admin
import app1.views

urlpatterns = [
    url(r'^$', app1.views.first_page),
]
