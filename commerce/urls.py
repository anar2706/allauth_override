
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import ProductList,ProductDetail,ProductCreate,delete_view,ProductEdit

app_name = 'shop'


urlpatterns = [
    path('',ProductList.as_view(),name='home'),
    path('<slug>',ProductDetail.as_view(),name='detail'),
    path('create/',ProductCreate.as_view(),name='create'),
    path('<slug>/edit/',ProductEdit.as_view(),name='edit'),
    path('<slug>/delete/',delete_view,name='delete')
    


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)