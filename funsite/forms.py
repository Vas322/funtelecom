from django import forms

from funsite.models import Partner, Employee, Phone, Email, Address, Country, City, EmployeePosition, MailToSupport


class PartnerForm(forms.ModelForm):
    """The form saves information about name the new partner in the database."""

    class Meta:
        model = Partner
        fields = ('name_partner_company', 'target_registration', 'position_partner_on_market')


class PhoneNumberForm(forms.ModelForm):
    """The form saves information about the phone in the database."""

    class Meta:
        model = Phone
        fields = ('phone_number', 'extension_number',)


class EmailForm(forms.ModelForm):
    """The form saves information about the email in the database."""

    class Meta:
        model = Email
        fields = ('email',)


class AddressForm(forms.ModelForm):
    """The form saves information about the address in the database."""

    class Meta:
        model = Address
        fields = ('title',)


class CountryForm(forms.ModelForm):
    """The form saves information about the address in the database."""

    class Meta:
        model = Country
        fields = ('name_country',)


class CityForm(forms.ModelForm):
    """The form saves information about the address in the database."""

    class Meta:
        model = City
        fields = ('name_city',)


class EmployeeForm(forms.ModelForm):
    """The form saves information about the employee"""

    class Meta:
        model = Employee
        fields = ('last_name', 'first_name', 'employee_position')


class MailToSupportForm(forms.ModelForm):
    class Meta:
        model = MailToSupport
        fields = ['subject', 'name', 'sender', 'equipment_name', 'serial_number', 'message']
