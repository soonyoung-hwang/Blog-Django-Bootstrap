from .models import Comment
from django import forms


class CommentForm(forms.Modelform):
    class Meta:
        model = Comment
        fields = ("content",)
        # or exclude = ('post', 'author', 'created_at', 'modified_at', )
