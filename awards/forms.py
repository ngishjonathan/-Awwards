from django import forms
from .models import Profile,Project,Review

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    # def __init__(self, *args, **kwargs):
    #     super(NewProfForm, self).__init__(*args, **kwargs)
        # self.fields['prof_pic'].required = False

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','pub_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['project']