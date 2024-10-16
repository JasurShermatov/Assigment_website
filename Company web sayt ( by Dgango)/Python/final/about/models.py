from django.db import models

# Create your models here.

class Company(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    picture = models.ImageField(upload_to='static/images/company', blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Company'
        ordering = ['date']
        verbose_name_plural = 'Company'

class AboutWorker(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    picture = models.ImageField(upload_to='static/images/workers', max_length=100, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    place = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'AboutWorker'

class Feedback(models.Model):
    email = models.EmailField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Feedback'
        ordering = ['date']















