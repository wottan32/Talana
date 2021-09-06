from django import forms
from .models import ClUserData, InvitationToken


class ClUserDataForm(forms.ModelForm):
    class Meta:
        model = ClUserData
        fields = ('rut', 'Nombre', 'Apellido_1', 'Apellido_2', 'mail')

    def clean_email(self):
        data = self.cleaned_data['mail']

        if ClUserData.objects.filter(mail=data).exists():
            raise forms.ValidationError('Solamente puede registrar un mail')

        return data


class InvitationTokenCheckForm(forms.Form):
    code = forms.CharField(max_length=40, required=True)

    def clean_code(self):
        data = self.cleaned_data['code']

        if not InvitationToken.objects.filter(code=data, uses__gte=1).exists():
            raise forms.ValidationError('Unknown token')

        return data

    def use_token(self):
        token = InvitationToken.objects.get(code=self.cleaned_data['code'])
        token.uses -= 1
        token.save(update_fields=('uses',))
        return token


class ConfirmRedeemInvitation(forms.Form):
    confirmation = forms.BooleanField(initial=False,
                                      required=True)
