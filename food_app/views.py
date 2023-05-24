from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from .models import Item, CATEGORY
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ContactForm
from decouple import config


EMAIL_HOST_USER = config("EMAIL_HOST_USER")


# Create class-based views
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["meals"] = CATEGORY
        return context




class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            message_body = f"{subject}. From: {email} \n{message} \n{first_name} {last_name}"
            email_message = EmailMessage("New message", message_body, to=[EMAIL_HOST_USER])
            email_message.send()

            messages.success(request, "Your message was successfully submitted! Thank you!")
    return render(request, "contact.html")

