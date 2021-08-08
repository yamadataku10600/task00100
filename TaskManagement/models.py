from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class JObOffer(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    job_desctiption = models.TextField()
    saraly = models.PositiveIntegerField()
    prefectuers = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.company_name
