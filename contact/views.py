from django.shortcuts import render, redirect
from django.contrib import messages
from contact .models import Contact,Info
from .forms import ContactForm


def contact_page(request):
    Infoo = Info.objects.all()[:1]
    forms = ContactForm()
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.INFO, 'Submitted!')
            return redirect('Post:thank_you')

    context = {
        'forms': forms,
         'Infoo' : Infoo
    }
    return render(request, 'contact/contact.html', context)
