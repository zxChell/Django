from django import forms


class UserForm(forms.Form):
    login = forms.CharField(required=False, min_length=5, max_length=25)
    password = forms.IntegerField(min_value=12)
    email = forms.EmailField()


class UserFormTwo(forms.Form):
    login = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    passwordTwo = forms.CharField()