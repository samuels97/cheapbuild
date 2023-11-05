from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
	class Meta:
		widgets = {
            "name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter your name!"}),
			"email":forms.EmailInput(attrs={"class":"form-control", "placeholder":"Enter your Email!"}),
			"body":forms.Textarea(attrs={"class":"form-control", "placeholder":"Enter your comment!","rows":"3"}),
        }
		model  = Comment
		fields = ('name', 'email', 'body')