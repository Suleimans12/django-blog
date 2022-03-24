from django import forms
from . models import Post
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
	body = forms.CharField(widget=CKEditorWidget())
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Post
		fields = [
			'image', 
			'title', 
			'body', 
			'draft', 
			'publish'
		]
