from django.contrib import admin
from .models import Company, AboutWorker, Feedback

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date')
    list_filter = ('date',)
    search_field = ('title', 'description')

@admin.register(AboutWorker)
class AddWorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'place')
    search_fields = ('first_name', 'last_name', 'age', 'place')
    list_filter = ('age', 'place')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date', 'message')
    search_fields = ('name', 'email', 'message')
    list_filter = ('date',)





