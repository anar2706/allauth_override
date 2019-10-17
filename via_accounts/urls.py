

from django.urls import path,include,re_path
from .views import ProfileSignUpView

urlpatterns = [
   path('visdom/',ProfileSignUpView.as_view(),name='visdom')
]
