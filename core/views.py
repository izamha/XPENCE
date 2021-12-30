import base64
import json
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view

from users.forms import (ProfileUpdateForm)
from .forms import (AccountForm, CategoryForm, ExpenseForm, IncomeForm)
from .models import (Account, Expense, Income, Category)
from users.models import CustomUser
from rest_framework.response import Response
from rest_framework import generics, views
from .serializers import (AccountSerializer,
                          UserSerializer,
                          ExpenseSerializer,
                          IncomeSerializer, CategorySerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from django.http import Http404


class Dashboard(LoginRequiredMixin, TemplateView):
    account_form_class = AccountForm
    category_form_class = CategoryForm
    expense_form_class = ExpenseForm
    income_form_class = IncomeForm
    profile_form_class = ProfileUpdateForm
    template_name = 'core/home.html'

    def post(self, request):
        post_data = request.POST or None
        account_form = self.account_form_class(post_data, prefix='account')
        category_form = self.category_form_class(post_data, prefix='category')
        expense_form = self.expense_form_class(post_data, prefix='expense')
        income_form = self.income_form_class(post_data, prefix='income')
        profile_form = self.profile_form_class(post_data, prefix='profile')

        # Additional data
        accounts_by_user = Account.objects.filter(user__in=[self.request.user])
        exp_instance = Expense()

        # Total Expenses(for a user)
        total_exp_by_user = exp_instance.total_expense(request.user)

        # Total Income(for a user)
        total_income_by_user = exp_instance.total_income(request.user)

        # Total Expenses in cash(for a user)
        total_exp_by_user_cash = exp_instance.format_money(
            exp_instance.total_expense_in_cash(request.user)
        )

        # Total Income in cash(for a user)
        total_income_by_user_cash = exp_instance.format_money(
            exp_instance.total_income_in_cash(request.user)
        )

        # Total Amount Income - Expense
        total_amount = exp_instance.format_money(int(exp_instance.total_income_in_cash(request.user)) - int(
            exp_instance.total_expense_in_cash(request.user)))

        income_form.fields['account'].queryset = Account.objects.filter(user__in=[request.user])

        context = self.get_context_data(account_form=account_form,
                                        category_form=category_form,
                                        expense_form=expense_form,
                                        income_form=income_form,
                                        profile_form=profile_form,
                                        accounts=accounts_by_user,
                                        expenses=total_exp_by_user,
                                        income=total_income_by_user,
                                        expenses_cash=total_exp_by_user_cash,
                                        income_cash=total_income_by_user_cash,
                                        total_amount=total_amount)

        if account_form.is_valid():
            self.form_save(account_form)
        if category_form.is_valid():
            self.form_save(category_form)
        if expense_form.is_valid():
            self.form_save(expense_form)
        if income_form.is_valid():
            self.form_save(income_form)
        if profile_form.is_valid():
            # self.form_save(profile_form)
            pass

        return self.render_to_response(context)

    def form_save(self, form):
        form.instance.user = self.request.user
        obj = form.save()
        messages.success(self.request, "Saved successfully!")
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request)


class AccountDetailView(TemplateView):
    account_form_class = AccountForm
    category_form_class = CategoryForm
    expense_form_class = ExpenseForm
    income_form_class = IncomeForm
    profile_form_class = ProfileUpdateForm

    template_name = 'core/home.html'

    def post(self, request, **kwargs):
        post_data = request.POST or None
        account_form = self.account_form_class(post_data, prefix='account')
        category_form = self.category_form_class(post_data, prefix='category')
        expense_form = self.expense_form_class(post_data, prefix='expense')
        income_form = self.income_form_class(post_data, prefix='income')
        profile_form = self.profile_form_class(post_data, prefix='profile')

        # Accounts by a user
        exp_instance = Expense()
        income_instance = Income()
        pk = self.kwargs.get('pk')

        accounts_by_user = Account.objects.filter(user__in=[request.user])

        # Total expenses by a user
        total_exp_by_user = exp_instance.total_expense(request.user)

        income_by_account = exp_instance.format_money(
            income_instance.income_by_account(pk, request.user))

        expense_by_account = exp_instance.format_money(
            income_instance.expense_by_account(pk, request.user))

        total_amount = exp_instance.format_money(int(income_instance.income_by_account(pk, request.user)) - int(
            income_instance.expense_by_account(pk, request.user)))

        an_account = Account.objects.get(pk=pk)
        the_account = Account.objects.get(pk=pk)

        income_form.fields['account'].queryset = Account.objects.filter(user__in=[request.user])

        context = self.get_context_data(
            account_form=account_form,
            category_form=category_form,
            expense_form=expense_form,
            income_form=income_form,
            profile_form=profile_form,

            account=an_account,
            the_account=the_account,
            accounts=accounts_by_user,
            expenses=total_exp_by_user,
            income=income_by_account,
            expense=expense_by_account,
            total_amount=total_amount
        )

        if account_form.is_valid():
            self.form_save(account_form)
        if category_form.is_valid():
            self.form_save(category_form)
        if expense_form.is_valid():
            self.form_save(expense_form)
        if income_form.is_valid():
            self.form_save(income_form)
        if profile_form.is_valid():
            # self.form_save(profile_form)
            pass
        return self.render_to_response(context)

    def form_save(self, form):
        form.instance.user = self.request.user
        obj = form.save()
        messages.success(self.request, "Saved successfully!")
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request)


def account(request, pk):
    exp_instance = Expense()
    income_instance = Income()

    total_exp_by_user = exp_instance.total_expense(request.user)
    accounts_by_user = Account.objects.filter(user__in=[request.user])

    income_by_account = exp_instance.format_money(
        income_instance.income_by_account(pk, request.user))

    expense_by_account = exp_instance.format_money(
        income_instance.expense_by_account(pk, request.user))

    total_amount = exp_instance.format_money(int(income_instance.income_by_account(pk, request.user)) - int(
        income_instance.expense_by_account(pk, request.user)))

    an_account = Account.objects.get(pk=pk)
    the_account = Account.objects.get(pk=pk)
    context = {'account': an_account,
               'the_account': the_account,
               'accounts': accounts_by_user,
               'expenses': total_exp_by_user,
               'income': income_by_account,
               'expense': expense_by_account,
               'total_amount': total_amount}
    return render(request, 'core/home.html', context)


def test(request):
    accounts_by_user = Account.objects.filter(user__in=[request.user])
    context = {'title': 'Test', 'accounts': accounts_by_user}
    return render(request, 'core/test.html', context)


"""
    API Implementations
"""


class CategoryView(generics.RetrieveAPIView):
    """ Retrieves all Category(s) """
    # permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryDetails(generics.ListAPIView):
    """ List Account Category """
    serializer_class = CategorySerializer

    def get_queryset(self):
        cat_id = self.kwargs['pk']
        return Category.objects.filter(pk=cat_id)


@api_view(['POST'])
def categoryCreate(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def categoryUpdate(request, pk):
    cat = Category.objects.get(pk=pk)
    serializer = IncomeSerializer(instance=cat, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def categoryDelete(request, pk):
    cat = Category.objects.get(pk=pk)
    cat.delete()

    return Response('Successfully deleted an Income!')


class AccountsView(generics.RetrieveAPIView):
    """ Retrieves all accounts """
    # permission_classes = (IsAuthenticated,)
    queryset = Account.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)


class ExpenseView(generics.RetrieveAPIView):
    """ Retrieves all Expenses """
    # permission_classes = (IsAuthenticated,)
    queryset = Expense.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ExpenseSerializer(queryset, many=True)
        return Response(serializer.data)


class AccountByUser(generics.ListAPIView):
    """ List Account object(s) that belong to an authenticated user"""
    # permission_classes = (IsAuthenticated, )
    serializer_class = AccountSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Account.objects.filter(user__in=[user_id])


@api_view(['POST'])
def accountCreate(request):
    serializer = AccountSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def accountUpdate(request, pk):
    _account = Account.objects.get(pk=pk)
    serializer = IncomeSerializer(instance=_account, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def accountDelete(request, pk):
    _account = Account.objects.get(pk=pk)
    _account.delete()

    return Response('Successfully deleted an Account!')


class ExpenseByUser(generics.ListAPIView):
    """ List Account object(s) that belong to an authenticated user"""
    # permission_classes = (IsAuthenticated, )
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Expense.objects.filter(user__in=[user_id])


class AccountDetails(generics.ListAPIView):
    """ List Account object """
    serializer_class = AccountSerializer

    def get_queryset(self):
        account_id = self.kwargs['pk']
        return Account.objects.filter(pk=account_id)


class ExpenseDetails(generics.ListAPIView):
    """ List Expense Object """
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        expense_id = self.kwargs['pk']
        return Expense.objects.filter(pk=expense_id)


class IncomeView(generics.RetrieveAPIView):
    """ Retrieves all Expenses """
    # permission_classes = (IsAuthenticated,)
    queryset = Income.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = IncomeSerializer(queryset, many=True)
        return Response(serializer.data)


class IncomeByUser(generics.ListAPIView):
    """ List Account object(s) that belong to an authenticated user"""
    # permission_classes = (IsAuthenticated, )
    serializer_class = IncomeSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Income.objects.filter(user__in=[user_id])


class IncomeDetails(generics.ListAPIView):
    """ List Income Object """
    serializer_class = IncomeSerializer

    def get_queryset(self):
        income_id = self.kwargs['pk']
        return Income.objects.filter(pk=income_id)


@api_view(['POST'])
def expenseCreate(request):
    serializer = ExpenseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def expenseUpdate(request, pk):
    expense = Expense.objects.get(pk=pk)
    serializer = IncomeSerializer(instance=expense, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def expenseDelete(request, pk):
    expense = Expense.objects.get(pk=pk)
    expense.delete()

    return Response('Successfully deleted an Expense!')


@api_view(['POST'])
def incomeCreate(request):
    serializer = IncomeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def incomeUpdate(request, pk):
    income = Income.objects.get(pk=pk)
    serializer = IncomeSerializer(instance=income, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def incomeDelete(request, pk):
    income = Income.objects.get(pk=pk)
    income.delete()

    return Response('Successfully deleted an Income!')


class UserDetailsView(views.APIView):
    """ User Details """
    queryset = CustomUser.objects.all()

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
