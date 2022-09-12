from django.db import models

# Create your models here.

class Payment_Table(models.Model):
    Fname = models.CharField(max_length=50,blank=False)
    Phone_Number = models.CharField(max_length=20, blank=True)
    Date = models.CharField(max_length=10)
    Amount_Paid = models.CharField(max_length=200)

    def __str__(self):
        return self.Fname + ' ' + self.Phone_Number + ' ' + self.Date + ' ' + self.Amount_Paid
