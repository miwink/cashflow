from django.conf.urls import url
from rest_framework.routers import DefaultRouter

import admin.views as views

urlpatterns = [
    url(r'^$', views.index, name='admin-index'),

    url(r'^confirm/$', views.confirm_overview, name='admin-confirm'),
    url(r'^attest/$', views.attest_overview, name='admin-attest'),
    url(r'^pay/$', views.pay_overview, name='admin-pay'),
    url(r'^account/$', views.account_overview, name='admin-account'),

    url(r'^expense/(?P<pk>\d+)/verification/edit/$', views.edit_expense_verification, name='admin-expense-edit-verification'),
    url(r'^expense/(?P<expense_pk>\d+)/verification/$', views.set_verification, name='admin-expense-verification'),
    url(r'^expense/(?P<pk>\d+)/confirm/$', views.confirm_expense, name='admin-expense-confirm'),

    url(r'^expense_part/(?P<pk>\d+)/attest/$', views.attest_expense_part, name='admin-expense_part-attest'),
]