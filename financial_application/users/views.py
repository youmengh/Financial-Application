from django.shortcuts import render
from .forms import AccountForm, BankForm
from .models import Account
# Create your views here.
def main_page(request):
    # template path
    template_name = 'users/table.html'

	# code to view accounts from the database	
    accounts = Account.objects.all()
    context = {
            'accounts': accounts
    }
    # render the page
    return render(request, template_name, context)



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

