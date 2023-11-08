from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        # or exclude = ('post', 'author', 'created_at', 'modified_at', )
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4}),
        }
