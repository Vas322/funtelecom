from funsite.models import Department, Address


def contact_main_office(request):
    contact_office_main_proc = Department.objects.get(name_department='Офис Зеленоград')
    email_main_office_proc = contact_office_main_proc.email_department
    phone_main_office_proc = contact_office_main_proc.phone_department
    city_main_office_proc = contact_office_main_proc.department_address.city
    street_main_office_proc = contact_office_main_proc.department_address.street
    number_house_main_office_proc = contact_office_main_proc.department_address.number_house
    address_access_map_link_proc = Address.objects.get(title='Офис Зеленоград')
    access_map_link_proc = address_access_map_link_proc.access_map_link
    context = {'contact_office_main_proc': contact_office_main_proc, 'email_main_office_proc': email_main_office_proc,
               'phone_main_office_proc': phone_main_office_proc, 'city_main_office_proc': city_main_office_proc,
               'access_map_link_proc': access_map_link_proc, 'street_main_office_proc': street_main_office_proc,
               'number_house_main_office_proc': number_house_main_office_proc}
    return context
