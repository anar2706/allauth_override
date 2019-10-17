from django.shortcuts import render
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from django.views.generic import CreateView
from .forms import ProfileForm
# Create your views here.


class ProfileSignUpView(SignupView):
    template_name = 'account/signup.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['profile_form'] = ProfileForm(self.request.POST)
        
        return context 

    def form_valid(self,form):
        response = super().form_valid(form)

        profile_form = ProfileForm(self.request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = self.user
            profile.save()
        return response

