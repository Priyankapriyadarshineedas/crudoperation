from django import forms

from .models import Person, Address, Account


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'dob', 'gen', 'reg', 'password')


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, Person):
        return Person.name


class CreateAddressForm(forms.ModelForm):
    persons = forms.ModelMultipleChoiceField(queryset=Person.objects.all(), required=False)

    class Meta:
        model = Address
        fields = ('street', 'city', 'state', 'zipcode', 'persons')
        street = forms.CharField()
        city = forms.CharField()
        state = forms.CharField()
        zipcode = forms.IntegerField()

        persons = CustomMMCF(
            queryset=Person.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )


# forms.py


class AccountForm(forms.ModelForm):
    persons = forms.ModelMultipleChoiceField(queryset=Person.objects.all(), required=False)

    class Meta:
        model = Account
        fields = ('account_type', 'account_number', 'balance', 'ifsc_code', 'branch', 'persons')
        account_type = forms.CharField()
        account_number = forms.CharField()
        balance = forms.DecimalField()
        ifsc_code = forms.CharField()
        branch = forms.CharField()
        persons = CustomMMCF(
            queryset=Person.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
