from django.urls import path

from .views import account_list, account_page, accounts_api, create_transaction, export_view, transactions_api

urlpatterns = [
    path("accounts/create/", account_page, name="account_page"),
    path("accounts/", account_list, name="account_list"),
    path("transactions/", create_transaction, name="transaction_page"),
    path("export/", export_view, name="export_view"),
    path("api/accounts/", accounts_api, name="accounts_api"),
    path("api/transactions/", transactions_api, name="transactions_api"),
]
