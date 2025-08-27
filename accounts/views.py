from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Account for {username} was created! You can now sign in.')
        return response

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('habit:habit-list')
        return super().get(request, *args, **kwargs)

