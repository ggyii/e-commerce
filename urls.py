from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about', views.index, name="AboutUs"),
    path('contact', views.contact, name="ContactUs"),
    path('category/<slug:slug>', views.category, name="Category"),
    path('tracker', views.tracker, name="Tracker"),
    path('search', views.search, name="Search"),
    path('checkout', views.checkout, name="Checkout"),
    path('productview/<int:pr_id>', views.prodview, name="ProductView"),
]
