from django.contrib import admin
from .models import Document
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
	list_display = ('id', 'description', 'photo', 'uploaded_at', 'output', 'user')
admin.site.register(Document, DocumentAdmin)