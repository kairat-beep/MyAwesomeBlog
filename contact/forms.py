from django.forms import ModelForm, Textarea

from .models import ContactMessage


class ContactMessageForm(ModelForm):

    class Meta:
        model = ContactMessage
        fields = "__all__"
        widgets = {"message": Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
