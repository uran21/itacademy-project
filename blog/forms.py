from django import forms
from blog.models import Post, Theme

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields=['theme','title','content']

class ThemeForm(forms.ModelForm):
	class Meta:
		model = Theme
		fields=['title','color','image']