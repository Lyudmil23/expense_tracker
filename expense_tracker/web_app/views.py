import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect

from expense_tracker.web_app.forms import ExpenseForm
from expense_tracker.web_app.models import Expense


def index(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    expenses = Expense.objects.all()
    total_expenses = sum(expense.amount for expense in expenses)

    #Logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = sum(d.amount for d in data)

    # Logic to calculate 30 days expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = sum(d.amount for d in data)

    # Logic to calculate 7 days expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = sum(d.amount for d in data)

    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))

    expense_form = ExpenseForm()

    context = {
        'expense_form': expense_form,
        'expenses': expenses,
        'total_expenses': total_expenses,
        'yearly_sum': yearly_sum,
        'monthly_sum': monthly_sum,
        'weekly_sum': weekly_sum,
        'daily_sums': daily_sums,
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