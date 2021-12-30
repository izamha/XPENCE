from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

app_name = 'core'

urlpatterns = [
    path('', Dashboard.as_view(), name='home'),
    path('test/', test, name='test'),
    path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),

    # API end-points

    # Account
    path('api/accounts/', AccountsView.as_view(), name='accounts'),
    path('api/account/by/<int:pk>/', AccountByUser.as_view()),
    path('api/account/<int:pk>/', AccountDetails.as_view()),
    path('api/account/create/', accountCreate),
    path('api/account/update/<int:pk>/', accountUpdate),
    path('api/account/delete/<int:pk>/', accountDelete),

    # Expenses
    path('api/expenses/', ExpenseView.as_view(), name='expenses'),
    path('api/expense/by/<int:pk>/', ExpenseByUser.as_view()),
    path('api/expense/<int:pk>/', ExpenseDetails.as_view()),
    path('api/expense/create/', expenseCreate),
    path('api/expense/update/<int:pk>/', expenseUpdate),
    path('api/expense/delete/<int:pk>/', expenseDelete),

    # Income
    path('api/income-all/', IncomeView.as_view(), name='income'),
    path('api/income/by/<int:pk>/', IncomeByUser.as_view()),
    path('api/income/<int:pk>/', IncomeDetails.as_view()),
    path('api/income/create/', incomeCreate),
    path('api/income/update/<int:pk>/', incomeUpdate),
    path('api/income/delete/<int:pk>/', incomeDelete),

    # Category
    path('api/categories/', CategoryView.as_view(), name='categories'),
    path('api/category/<int:pk>/', CategoryDetails.as_view()),
    path('api/category/create/', categoryCreate),
    path('api/category/update/<int:pk>/', categoryUpdate),
    path('api/category/delete/<int:pk>/', categoryDelete),

    # User
    path('api/user/<int:pk>/', UserDetailsView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('api-token/', TokenObtainPairView.as_view()),
]
