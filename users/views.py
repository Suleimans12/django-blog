from django.urls import reverse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from . forms import UserRegistrationForm, UserLogInForm



class UserRegistrationView(FormView, SuccessMessageMixin):
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_message = 'User registered successfully'
    success_url = reverse_lazy('login') # /login/

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get('password'))
        user.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)



def login_view(request):
    form = UserLogInForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        # Get form values for username and password
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        #  Check if the user is valid
        user = authenticate(username=username, password=password)
        # Log in  a user
        login(request, user)
        messages.success(request, "Logged in successfully")
        return redirect(reverse('index'))


    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect(reverse('login'))