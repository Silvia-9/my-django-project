from django.db import models
from django.utils import timezone

class Expense(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    currency = models.CharField(max_length=3,default='GBP')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
class Meta:
    ordering = ['-date']

    def __str__(self):
        return f"{self.category}: {self.amount} {self.currency}"

