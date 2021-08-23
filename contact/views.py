from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactForm


def home(request):
    return render(request, 'contact/home.html')


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fikr bildirganingiz uchun rahmat')
            return redirect('home')

    return render(request, 'contact/form.html', {'form': form})
