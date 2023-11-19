from django import forms

from expense.models import Expense


class ExpenseForm(forms.Form):
    title = forms.CharField(max_length=100)
    expense = forms.FloatField()
    created = forms.DateTimeField(input_formats=True)


    def save(self):
        new_expense = Expense.objects.create(
            title=self.cleaned_data['title'],
            expense=self.cleaned_data['expense'],
            created=self.cleaned_data['created']
        )
        return new_expense
