from django import forms
from blog.models import Post, Tag

class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ['name', 'slug']


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['is_active', 'title', 'slug', 'body', 'style', 'tags']
