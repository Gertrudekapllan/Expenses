from django.urls import path
from .views import *

app_name = 'expense'

urlpatterns = [
    path('expense/create', expense_create,  name='expense-create'),
    path('expense/list', expense_list, name='expense-list')
]