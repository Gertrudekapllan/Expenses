from django.db.models.functions import ExtractYear, ExtractWeek, datetime, TruncMonth
from django.shortcuts import render, redirect
from django.db.models import Count, Sum
from django.db.models.functions import TruncWeek
from expense.forms import ExpenseForm
from expense.models import Expense


def expense_list(request):
    expenses = Expense.objects.all()
    expenses_weeks = (
        Expense.objects.annotate(
            week_start=TruncWeek('created'),
        )
        .values('week_start')
        .annotate(total_expenses=Sum('expense'))
        .order_by('week_start')
    )
    expenses_monthly = (
        Expense.objects.annotate(
            month_start=TruncMonth('created'),
        )
        .values('month_start')
        .annotate(total_expenses=Sum('expense'))
        .order_by('month_start')
    )

    week_data = []
    month_data = []
    for record in expenses_weeks:
        week_start = record['week_start']
        total_expenses = record['total_expenses']
        week_data.append({'week_start': week_start, 'total_expenses': total_expenses})
    for rec in expenses_monthly:
        month_start = rec['month_start']
        total_expenses = rec['total_expenses']
        month_data.append({'month_start': month_start, 'total_expenses': total_expenses})

    return render(request, 'expense/expense-list.html', locals())


def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = Expense.objects.create(
                title=form.cleaned_data["title"],
                expense=form.cleaned_data["expense"],
                created=form.cleaned_data["created"],
            )
        return redirect("expense:expense-list")
    else:
        form = ExpenseForm()
        return render(request, 'expense/expense-create.html', locals())
