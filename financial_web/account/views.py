# module account views

from django.shortcuts import render, redirect
from account.models import Account, Kyc
from account.form import kycForm


def kyc_registration_view(request):
    user = request.user
    account = Account.objects.get(user=user)
    try:
        kyc = Kyc.objects.get(user)
    except:
        kyc = None
    if request.method == "POST":
        form = KycForm(request.POST, request.File, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "Kyc successfully submitted, In review now")
            return redirect("core:index")
    else:
        form = kycForm(instance=kyc)
    context={
        'account': account,
        'form':form,
    }
    return render(request, 'account/kyc-form.html', context)

        