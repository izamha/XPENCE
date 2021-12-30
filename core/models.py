from django.core.validators import RegexValidator
from django.db import models
from users.models import CustomUser

CATEGORY_TYPE = (
    ('expense', 'Expense Category'),
    ('income', 'Income Category'),
)

CURRENCY = (
    ('rwandan', 'Rwf'),
    ('usd', 'USD'),
    ('ugandan', 'Ugandan Shillings'),
)


class Account(models.Model):
    name = models.CharField(max_length=255)
    currency = models.CharField(default='rwandan', max_length=255, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'%s' % self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Category Name', max_length=255)
    type = models.CharField(choices=CATEGORY_TYPE, default='expense', max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'%s' % self.name


class Income(models.Model):
    amount_regex = RegexValidator(regex=r'^\1\d{9,14}', message='This amount you entered makes no sense!')
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Income %s' % self.pk

    def income_by_account(self, account_id, current_user):
        incomes = Income.objects.filter(account__in=[account_id], user__in=[current_user.id])
        amount = 0
        for income in incomes:
            amount += income.amount
        return amount

    def expense_by_account(self, account_id, current_user):
        expenses = Expense.objects.filter(account__in=[account_id], user__in=[current_user.id])
        amount = 0
        for expense in expenses:
            amount += expense.amount
        return amount


class Expense(models.Model):
    amount_regex = RegexValidator(regex=r'^\1\d{9,14}', message='This amount you entered makes no sense!')
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Expense %s' % self.pk

    @staticmethod
    def format_money(money):
        return '{:,}'.format(money)

    def total_expense(self, current_user):
        expenses = Expense.objects.filter(user__in=[current_user.id])
        return expenses.count()

    def total_income(self, current_user):
        incomes = Income.objects.filter(user__in=[current_user.id])
        return incomes.count()

    def total_expense_in_cash(self, current_user):
        expenses = Expense.objects.filter(user__in=[current_user.id])
        amount = 0
        for expense in expenses:
            amount += expense.amount
        return amount

    def total_income_in_cash(self, current_user):
        incomes = Income.objects.filter(user__in=[current_user.id])
        amount = 0
        for income in incomes:
            amount += income.amount
        return amount
