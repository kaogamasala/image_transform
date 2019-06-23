from django.forms import ModelForm
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ['description', 'photo']

# class MosaicDocumentForm(forms.ModelForm):
# 	class Meta:
# 		model = Document
# 		fields = ['description', 'photo']