from django.shortcuts import render, HttpResponsePermanentRedirect
from django.views.generic import View, ListView, DetailView
from deposit.models import Deposit


class DepositListView(ListView):
    model = Deposit
    template_name = 'deposit_list.html'

def add_deposit(request):
    if request.method == 'POST':

        deposit = request.POST['deposit']
        term = request.POST['term']
        rate = request.POST['rate']

        def interest(deposit, term, rate):


            interest = 0

            for i in range(term):
                interest = interest + (deposit + interest) * rate

            return interest

        deposit = Deposit(deposit=deposit,
                          term=term,
                          rate=rate,
                          interest=interest(int(deposit), int(term), float(rate)),
                          )

        deposit.save()

        context = {
            'deposit': deposit,
        }
        return HttpResponsePermanentRedirect('/')


    return render(
        template_name='form.html',
        request=request
    )

class GetDepositView(DetailView):
    model = Deposit
    template_name = 'deposit.html'
