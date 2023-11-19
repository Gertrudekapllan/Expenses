from django.db import models
from django.forms import ModelForm


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Expense(models.Model):
    title = models.CharField(max_length=100)
    expense = models.FloatField()
    created = models.DateTimeField(auto_now_add=False)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



