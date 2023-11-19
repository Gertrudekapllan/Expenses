from django.shortcuts import render, redirect

from expense.forms import ExpenseForm
from expense.models import Expense


def expense_list(request):
    services = Expense.objects.all()
    return render(request, 'expense/expense-list.html', locals())


def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = Expense.objects.create(
                title = form.cleaned_data["title"],
                expense = form.cleaned_data["expense"],
            )
        return redirect("expense:expense-list")
    else:
        form = ExpenseForm()
        return render(request, 'expense/expense-create.html', locals())
