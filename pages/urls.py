from django.urls import path

from .views import index, AboutPageView, test

urlpatterns = [
    path("", index, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("test/", test, name="test"),
]
