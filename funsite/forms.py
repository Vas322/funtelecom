from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from funsite.models import Partner, Employee, Phone, Email, Address, Country, City, EmployeePosition, MailToSupport


class PartnerForm(forms.ModelForm):
    """The form saves information about name the new partner in the database."""
    name_partner_company = forms.CharField(max_length=200, label='',
                                           widget=forms.TextInput(attrs={'placeholder': 'Название вашей компании'}))
    target_registration = forms.CharField(max_length=100, label='',
                                          widget=forms.TextInput(attrs={'placeholder': 'Цель заявки'}),
                                          help_text='Например, покупка товаров оптом.')
    position_partner_on_market = forms.CharField(max_length=100, label='',
                                                 widget=forms.TextInput(attrs={'placeholder': 'Позиция на рынке'}),
                                                 help_text='Например, "Интегратор"')

    class Meta:
        model = Partner
        fields = ('name_partner_company', 'target_registration', 'position_partner_on_market')


class PhoneNumberForm(forms.ModelForm):
    """The form saves information about the phone in the database."""
    phone_number = forms.CharField(max_length=13, label='',
                                   widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}))
    extension_number = forms.CharField(max_length=10, label='',
                                       widget=forms.TextInput(attrs={'placeholder': 'Введите ваш добавочный номер'}))

    class Meta:
        model = Phone
        fields = ('phone_number', 'extension_number',)


class EmailForm(forms.ModelForm):
    """The form saves information about the email in the database."""
    email = forms.CharField(max_length=100, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Введите ваш email'}))

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
    name_country = forms.CharField(max_length=100, label='',
                                   widget=forms.TextInput(attrs={'placeholder': 'Введите вашу страну'}))

    class Meta:
        model = Country
        fields = ('name_country',)


class CityForm(forms.ModelForm):
    """The form saves information about the address in the database."""
    name_city = forms.CharField(max_length=100, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Введите ваш город'}))

    class Meta:
        model = City
        fields = ('name_city',)


class EmployeeForm(forms.ModelForm):
    """The form saves information about the employee"""

    class Meta:
        model = Employee
        fields = ('last_name', 'first_name', 'employee_position')


class MailToSupportForm(forms.ModelForm):
    """The form saves information about the message to technical support"""
    subject = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Тема письма'}))
    name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'ФИО'}))
    equipment_name = forms.CharField(max_length=100, label='',
                                     widget=forms.TextInput(attrs={'placeholder': 'Наименование оборудования'}))
    serial_number = forms.CharField(max_length=50, label='',
                                    widget=forms.TextInput(attrs={'placeholder': 'Серийный номер оборудования'}))
    sender = forms.EmailField(max_length=150, label='',
                              widget=forms.TextInput(attrs={'placeholder': 'Ваш email для ответа'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Детально опишите вашу проблему'}))

    class Meta:
        model = MailToSupport
        fields = ['subject', 'name', 'sender', 'equipment_name', 'serial_number', 'message']
