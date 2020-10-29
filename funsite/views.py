from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib import messages

from funsite.forms import PartnerForm, PhoneNumberForm, EmailForm, AddressForm, CountryForm, CityForm, EmployeeForm, \
    MailToSupportForm
from funsite.models import Brand, News, Carousel, CompanyInfo, Department, Country, Email, Phone, City


def index(request):
    """Controller that displays the main page"""
    brand_list = Brand.objects.all()
    news_list = News.objects.order_by('-created_date')[:3]
    carousel_list = Carousel.objects.order_by('index').all()[:5]
    my_company_info = CompanyInfo.objects.all()
    context = {'brand_list': brand_list, 'news_list': news_list, 'carousel_list': carousel_list,
               'my_company_info': my_company_info}
    return render(request, "funsite/index.html", context)


def detail_brand(request, pk):
    """The controller displays detailed information about the brand"""
    brand = get_object_or_404(Brand, pk=pk)
    context = {'brand': brand}
    return render(request, 'funsite/detail_brand.html', context)


def detail_news(request, pk):
    """The controller displays detailed information about the news"""
    news = get_object_or_404(News, pk=pk)
    context = {'news': news}
    return render(request, 'funsite/detail_news.html', context)


def all_news(request):
    """Controller that displays the all news on page"""
    news_list = News.objects.order_by('-created_date')
    context = {'news_list': news_list}
    return render(request, "funsite/all_news.html", context)


def all_brands(request):
    """Controller that displays the all brands on page"""
    brand_list = Brand.objects.all()
    context = {'brand_list': brand_list}
    return render(request, "funsite/all_brands.html", context)


def company_info(request):
    """Controller that displays the info about company"""
    my_company_info = CompanyInfo.objects.get()
    context = {'my_company_info': my_company_info}
    return render(request, "funsite/company_info.html", context)


def contacts_our_company(request):
    """Controller that displays the contacts company on page 'Our contacts'"""
    contact_company = Department.objects.filter(published_on_page=True)
    context = {'contact_company': contact_company}
    return render(request, "funsite/contacts_company.html", context)


def support_page(request):
    """Controller that displays the info about support on page"""
    support_info = Department.objects.get(email_department__email='support@funtelecom.ru')
    context = {'support_info': support_info}
    return render(request, "funsite/support_page.html", context)


def add_new_partner(request):
    """The controller that processes the form to create a new partner."""
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)
        part_form = PartnerForm(request.POST)
        phone_form = PhoneNumberForm(request.POST)
        email_form = EmailForm(request.POST)
        address_form = AddressForm(request.POST)
        country_form = CountryForm(request.POST)
        city_form = CityForm(request.POST)
        if part_form.is_valid() and phone_form.is_valid() and email_form.is_valid() and address_form.is_valid() \
                and country_form.is_valid() and city_form.is_valid() and employee_form.is_valid():
            email_obj, created = Email.objects.get_or_create(email=email_form.cleaned_data["email"])
            employee_obj = employee_form.save(commit=False)
            employee_obj.email_employee = email_obj

            phone_obj, created = Phone.objects.get_or_create(phone_number=phone_form.cleaned_data["phone_number"])
            employee_obj.phone_employee = phone_obj

            country_obj, created = Country.objects.get_or_create(name_country=country_form.cleaned_data["name_country"])
            address_obj = address_form.save(commit=False)
            address_obj.country = country_obj

            city_obj, created = City.objects.get_or_create(name_city=city_form.cleaned_data["name_city"])
            address_obj.city = city_obj

            address_obj = address_form.save()
            employee_obj.address_employee = address_obj
            address_form.save()
            part_form.save()
            employee_form.save()

            messages.add_message(request, messages.SUCCESS, 'Заявка на сотрудничество отправлена!')
            return render(request, 'funsite/success_add_new_partner.html')
    else:
        employee_form = EmployeeForm()
        part_form = PartnerForm()
        email_form = EmailForm()
        phone_form = PhoneNumberForm()
        address_form = AddressForm()
        country_form = CountryForm()
        city_form = CityForm()
    context = {'part_form': part_form, 'phone_form': phone_form, 'email_form': email_form,
               'address_form': address_form, 'country_form': country_form, 'city_form': city_form,
               'employee_form': employee_form}
    return render(request, 'funsite/add_new_partner.html', context)


def mail_to_support(request):
    """The controller that sending an email to support"""
    if request.method == 'POST':
        mail_to_support_form = MailToSupportForm(request.POST)
        if mail_to_support_form.is_valid():
            subject = mail_to_support_form.cleaned_data['subject']
            name = mail_to_support_form.cleaned_data['name']
            sender = mail_to_support_form.cleaned_data['sender']
            equipment_name = mail_to_support_form.cleaned_data['equipment_name']
            serial_number = mail_to_support_form.cleaned_data['serial_number']
            message = 'Письмо было отправлено с сайта www.funtelecom.ru.\r\n От %s.\r\nАдрес для ответа: %s.\r\n'\
                      'Наименование оборудования: %s.\r\nСерийный номер оборудования: %s.\r\nОписание проблемы:'\
                      % (sender, name, equipment_name, serial_number)
            message += mail_to_support_form.cleaned_data['message']
            recipients = ['dmitrochenko.vasiliy@gmail.com']
            mail_to_support_form.save()
            send_mail(subject, message, sender, recipients, fail_silently=False)
            messages.add_message(request, messages.SUCCESS, 'Заявка в техподдержку отправлена!')
            return render(request, 'funsite/success_mail_to_support.html')
    else:
        mail_to_support_form = MailToSupportForm()
    context = {'mail_to_support_form': mail_to_support_form}
    return render(request, 'funsite/mail_to_support.html', context)
