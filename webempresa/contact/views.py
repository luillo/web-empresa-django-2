from django.shortcuts import render , redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Envio y Redireccion
            email = EmailMessage(
                "La cafetera : Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "sistemas@begroup.com.mx",
                ["l.onofre@begroup.com.mx"],
                reply_to=[email]
            )
            try:
                email.send()
                # Todo salio bien
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no salio Bien
                return redirect(reverse('contact')+"?fail")


    return render(request, "contact/contact.html", {'form':contact_form})