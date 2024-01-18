from django.shortcuts import render, redirect

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


def edit(request, pk):
    if request.method == 'POST':
        expense = Expense.objects.get(pk=pk)
        expense_form = ExpenseForm(request.POST, instance=expense)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('index')
    else:
        expense = Expense.objects.get(pk=pk)
        expense_form = ExpenseForm(instance=expense)

    context = {
        'expense_form': expense_form,
    }

    return render(request, 'web_app/edit.html', context)


def delete(request, pk):
    if request.method == 'POST' and 'delete' in request.POST:
        expense = Expense.objects.get(pk=pk)
        expense.delete()

    return redirect('index')