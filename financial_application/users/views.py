from django.shortcuts import render
from .forms import AccountForm, BankForm, UserForm
from .models import Account, Customer, Bank, CardInfo, Transaction


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


def add_account(request):
    template_name = 'users/add_account.html'
    if request.method == "POST":
        account_form = AccountForm(request.POST)
        if account_form.is_valid():
            account = account_form.save(commit=False)
            account.save()
    else:
        account_form = AccountForm()
    context = {
        'account_form': account_form
    }
    return render(request, template_name, context)


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
