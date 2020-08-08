from django.contrib import admin
from django.urls import path
from djangogram import views


urlpatterns = [

    path("hello-world/",views.hello_world),
    path("sorted/", views.sortIntegers),
    path("hi/<str:name>/<int:age>",views.say_hi)
]


