from django.contrib.messages.views import SuccessMessageMixin
from django.utils.html import escape
from django.views.generic.edit import FormView

from contact.forms import ContactMessageForm
from contact.models import ContactMessage


class ContactMessageView(SuccessMessageMixin, FormView):

    template_name = "contact/contact.html"
    form_class = ContactMessageForm
    success_url = "thanks"
    success_message = "%(name)s"

    def form_valid(self, form):

        # Clean user data. Just in case
        ContactMessage.objects.create(
            name=escape(form.cleaned_data["name"]),
            message=escape(form.cleaned_data["message"]),
        )
        return super().form_valid(form)
