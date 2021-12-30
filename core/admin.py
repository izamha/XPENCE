from django.contrib import admin
from .models import (Account, Category, Expense, Income)

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Income)
