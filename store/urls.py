from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store import views

urlpatterns = [

    path('', views.home, name='home'),
    path('servers_desktops/', views.ServerDesktop, name='servers_desktops'),
    path('servers_desktops/<slug:data>', views.ServerDesktop, name='sddata'),
    path('laptops/', views.Laptops, name='laptops'),
    path('laptops/<slug:data>', views.Laptops, name='ldata'),
    path('mobiles/', views.Mobiles, name='mobiles'),
    path('mobiles/<slug:data>', views.Mobiles, name='mdata'),
    path('gadgets/', views.Gadgets, name='gadgets'),
    path('gadgets/<slug:data>', views.Gadgets, name='gadgets'),
    #path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
