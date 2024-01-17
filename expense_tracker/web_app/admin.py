from django.contrib import admin

from expense_tracker.web_app.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass