from django import forms

from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('text', )

    def save(self, user, forum):
        obj = super().save(commit=False)
        obj.registered_by = user
        obj.forum = forum
        obj.save()
        return obj


class ReplyForm(forms.ModelForm):
    class Meta:
        model = models.Reply
        fields = ('text', )

    def save(self, user, post):
        obj = super().save(commit=False)
        obj.registered_by = user
        obj.post = post
        obj.save()
        return obj
