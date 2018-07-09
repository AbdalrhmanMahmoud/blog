from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post

# add and update form
class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget)
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"draft",
			"publish"
		]