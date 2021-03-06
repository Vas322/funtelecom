from django.urls import path

from funsite.views import index, detail_brand, detail_news, all_news, all_brands, company_info, contacts_our_company, \
    support_page, add_new_partner, mail_to_support

urlpatterns = [
    path('', index, name='index'),
    path('brand/<int:pk>/', detail_brand, name='detail_brand'),
    path('news/<int:pk>/', detail_news, name='detail_news'),
    path('all_news/', all_news, name='all_news'),
    path('all_brands/', all_brands, name='all_brands'),
    path('company_info', company_info, name='company_info'),
    path('contacts_our_company', contacts_our_company, name='contact_our_company'),
    path('support_page/', support_page, name='support_page'),
    path('add_new_partner/', add_new_partner, name='add_new_partner'),
    path('mail_to_support/', mail_to_support, name='mail_to_support'),
]
