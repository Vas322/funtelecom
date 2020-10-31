from funsite.models import Department


def contact_main_office(request):
    contact_office_main_proc = Department.objects.get(name_department='Офис Зеленоград')
    email_main_office_proc = contact_office_main_proc.email_department
    phone_main_office_proc = contact_office_main_proc.phone_department
    country_main_office_proc = contact_office_main_proc.department_country
    city_main_office_proc = contact_office_main_proc.department_city
    street_main_office_proc = contact_office_main_proc.department_street
    number_house_main_office_proc = contact_office_main_proc.department_number_house
    number_office_main_office_proc = contact_office_main_proc.department_number_office
    department_access_map_link_main_office_proc = contact_office_main_proc.department_access_map_link

    context = {'contact_office_main_proc': contact_office_main_proc, 'email_main_office_proc': email_main_office_proc,
               'phone_main_office_proc': phone_main_office_proc, 'country_main_office_proc': country_main_office_proc,
               'city_main_office_proc': city_main_office_proc, 'street_main_office_proc': street_main_office_proc,
               'number_house_main_office_proc': number_house_main_office_proc,
               'number_office_main_office_proc': number_office_main_office_proc,
               'department_access_map_link_main_office_proc': department_access_map_link_main_office_proc}
    return context
