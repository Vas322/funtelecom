from funsite.models import Department


def contact_main_office(request):
    contact_office_main = Department.objects.get(name_department='Офис Зеленоград')
    email_main_office = contact_office_main.email_department
    phone_main_office = contact_office_main.phone_department
    context = {'contact_office_main': contact_office_main, 'email_main_office': email_main_office,
               'phone_main_office': phone_main_office}
    return context
