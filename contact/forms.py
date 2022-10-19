from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'messageLabel'}))
