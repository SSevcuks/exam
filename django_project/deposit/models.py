from django.db import models


class Deposit(models.Model):
    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.FloatField()
    interest = models.FloatField()




# def interest_(self, deposit, term, rate):
#     self.deposit = deposit
#     self.term = term
#     self.rate = rate
#
#     interest = 0
#
#     for i in range(term):
#         interest = interest + (deposit + interest) * rate
#
#     return interest



