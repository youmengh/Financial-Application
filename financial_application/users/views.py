from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def main_page(request):
    # template path
    template_name = 'users/table.html'

    # code to view accounts from the database
    # accounts = Account.objects.all()
    # context = {
    #     'accounts': accounts
    # }

    # render the page
    return render(request, template_name)


# def add_account(request):
#     template_name = 'users/add_account.html'
#     if request.method == "POST":
#         account_form = AccountForm(request.POST)
#         if account_form.is_valid():
#             account = account_form.save(commit=False)
#             account.save()
#     else:
#         account_form = AccountForm()
#     context = {
#         'account_form': account_form
#     }
#     return render(request, template_name, context)

def account_form(request, id=0):
    template_name = 'users/add_account.html'
    if request.method == "GET":
        if id == 0:
            form = AccountForm()
        else:
            account = Account.objects.get(pk=id)
            form = AccountForm(instance=account)
        return render(request, 'users/add_account.html', {'form': form})
    else:
        if id == 0:
            form = AccountForm(request.POST)
        else:
            account = Account.objects.get(pk=id)
            form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
        else:
            print("invalid")
        return redirect('/users/view-accounts/')

def account_delete(request, id):
    account = Account.objects.get(pk=id)
    account.delete()
    return redirect('/users/view-accounts')

def add_bank(request):
    template_name = 'users/add_bank.html'
    if request.method == "POST":
        bank_form = BankForm(request.POST)
        if bank_form.is_valid():
            bank = bank_form.save(commit=False)
            bank.save()
    else:
        bank_form = BankForm()
    context = {
        'bank_form': bank_form
    }
    return render(request, template_name, context)

def add_user(request):
    template_name = 'users/add_user.html'
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
    else:
        user_form = UserForm()
    context = {
        'user_form': user_form
    }
    return render(request, template_name, context)

def add_cardinfo(request):
    template_name = 'users/add_cardinfo.html'
    if request.method == "POST":
        card_form = CardForm(request.POST)
        if card_form.is_valid():
            card = card_form.save(commit=False)
            card.save()
    else:
        card_form = CardForm()
    context = {
        'card_form': card_form
    }
    return render(request, template_name, context)

def add_transaction(request):
    template_name = 'users/add_transaction.html'
    if request.method == "POST":
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            transaction.save()
    else:
        transaction_form = TransactionForm()
    context = {
        'transaction_form': transaction_form
    }
    return render(request, template_name, context)

def view_accounts(request):
    # template path
    template_name = 'users/view_accounts.html'

    # code to view accounts from the database
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }
    # render the page
    return render(request, template_name, context)


def view_users(request):
    # template path
    template_name = 'users/view_users.html'

    # code to view accounts from the database
    users = Customer.objects.all()
    context = {
        'users': users
    }
    # render the page
    return render(request, template_name, context)


def view_banks(request):
    # template path
    template_name = 'users/view_banks.html'

    # code to view accounts from the database
    banks = Bank.objects.all()
    context = {
        'banks': banks
    }
    # render the page
    return render(request, template_name, context)


def view_cardinfo(request):
    # template path
    template_name = 'users/view_cardinfo.html'

    # code to view accounts from the database
    cards = CardInfo.objects.all()
    context = {
        'cards': cards
    }
    # render the page
    return render(request, template_name, context)


def view_transactions(request):
    # template path
    template_name = 'users/view_transactions.html'

    # code to view accounts from the database
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions
    }
    # render the page
    return render(request, template_name, context)
