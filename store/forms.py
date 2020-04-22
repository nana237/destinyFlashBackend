from django import forms
class AGENT_DESTINYForm (forms.ModelForm)
    class Meta:
        model=AGENT_DESTINY
        widgets = {
            'motDePassA' : forms.PasswordInput()
        }