from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path("", views.home),
    path("home", views.home, name="home"),
    path("products", views.products, name="products"),
    
    path("about_us", views.about_us, name="about"),
    path("contact_us", views.contact_us, name="contact"),
    #path("product_details", views.product_details, name="monarch-gun"),
    path('product_details/<int:id>/', views.product_details, name='product_details'),
   
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
