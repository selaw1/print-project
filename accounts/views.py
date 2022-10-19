from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, CreateView

from accounts.forms import RegistrationForm


# Custom user model
UserBase = get_user_model()


class HomeView(TemplateView):
    template_name = "accounts/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

class UserCreateView(CreateView):
    model = UserBase
    form_class = RegistrationForm
    template_name = 'accounts/registration/registration.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs) 

    def form_valid(self, form):
        # Email Activation Setup
        # current_site = get_current_site(self.request)
        # subject = 'Activate Your Account'
        # message = render_to_string('account/registration/account_activation_email.html', {
        #     'user':user,
        #     'domain':current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token':account_activation_token.make_token(user),
        # })
        # user.email_user(subject=subject, message=message)

        # Success message 
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Check Your Email For Account Activation Link'
        ) 
        return super().form_valid(form)

