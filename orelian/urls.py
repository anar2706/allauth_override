
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from via_accounts.views import ProfileSignUpView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('commerce.urls',namespace='shop')),
    url(r'^accounts/signup/', ProfileSignUpView.as_view(), name='account_signup'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    
   
]
