from .models import *
from django import forms


# class NewImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         exclude = ['profile', 'likes', 'imagecomments',]


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []
        fields = ['profilepic', 'bio','username', 'contact']


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        exclude = []
        fields = ['first_name', 'last_name', 'email']
# class NewComment(forms.ModelForm):
#     class Meta:
#         model = Comment
#         exclude = ['commentator','comment_image']
