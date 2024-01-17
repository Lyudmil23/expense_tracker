from django.shortcuts import render

from expense_tracker.web_app.forms import ExpenseForm
from expense_tracker.web_app.models import Expense


def index(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    expenses = Expense.objects.all()
    expense_form = ExpenseForm()

    context = {
        'expense_form': expense_form,
        'expenses': expenses,
    }

    return render(request, 'web_app/index.html', context)
