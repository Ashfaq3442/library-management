from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=225)
    author=models.CharField(max_length=225)
    description=models.TextField()
    is_available = models.BooleanField(default=True)  # Field for availability
    borrower_name = models.CharField(max_length=225, blank=True, null=True)
    borrower_contact = models.CharField(max_length=225, blank=True, null=True)
    borrower_address = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title()
