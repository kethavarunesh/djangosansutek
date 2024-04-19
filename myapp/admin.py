from django.contrib import admin
from myapp.models import Contactform,ResumeSubmission
# Register your models here.

class ContactformAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email', 'phone', 'message')
    list_filter = ('name', 'email')


admin.site.register(Contactform, ContactformAdmin)
admin.site.register(ResumeSubmission)