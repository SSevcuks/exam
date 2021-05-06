from django.shortcuts import render, HttpResponse
from django.views.generic import View, ListView, FormView, DetailView
from deposit.models import Deposit
from deposit.forms import DepositForm


class DepositListView(ListView):
    model = Deposit
    template_name = 'deposit_list.html'


class AddDepositView(FormView):
    form_class = DepositForm
    template_name = 'add_deposit.html'


    def form_valid(self, form):
        form.save()
        deposit = form.cleaned_data['deposit']
        term = form.cleaned_data['term']
        rate = form.cleaned_data['rate']


        return HttpResponse(f"<p>Deposit: <strong>{deposit}"
                            f"</strong><br>Term: {term}"
                            f"<br>Rate: {rate}</p>")



class GetDepositView(DetailView):
    model = Deposit
    template_name = 'deposit.html'




