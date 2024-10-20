from django.shortcuts import render, redirect, get_object_or_404

from contact.forms import ContactForm
from django.urls import reverse

from contact.models import Contact


def create(request):
    form_action = reverse("contact:create")
    if request.method == "POST":

        form = ContactForm(request.POST)

        context = {"form": form, 'form_action': form_action}
        
        if form.is_valid():
            contact = form.save()
            return redirect("contact:udpate", contact_id=contact.id)

        return render(request, "contact/create.html", context)

    context = {"form": ContactForm(), "form_action": form_action}
    return render(request, "contact/create.html", context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse("contact:update", args=[contact_id])
    
    if request.method == "POST":

        form = ContactForm(request.POST, isntace=contact)

        context = {"form": form, 'form_action': form_action}
        
        if form.is_valid():
            contact = form.save()
            return redirect("contact:udpate", contact_id=contact.id)

        return render(request, "contact/create.html", context)

    context = {"form": ContactForm(instance = contact), "form_action": form_action}
    return render(request, "contact/create.html", context)

    