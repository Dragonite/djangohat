from django.forms import ModelForm
from django import forms

from .models import Event


class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            if fname == 'time':
                f.widget.attrs["class"] = "form-control"
                f.widget.attrs["id"] = "datetimepicker"
                f.widget.attrs["autocomplete"] = "off"
            f.widget.attrs["class"] = "form-control"
