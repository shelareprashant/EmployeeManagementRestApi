from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    doj = models.DateField()
    email_id = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    designation = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

