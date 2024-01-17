from django.forms import ModelForm

from expense_tracker.web_app.models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'category')