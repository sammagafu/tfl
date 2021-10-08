from django import forms

class AppointmentForm(forms.Form):

    SALES = [

    ('20% off for service', '20% off for service'),
    ('10% off for body work', '10% off for body work'),

    ]

    name = forms.CharField()
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    offer = forms.ChoiceField(choices=SALES)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass