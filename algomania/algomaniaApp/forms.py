from django import forms

class QuestionForm(forms.Form):
    # from_email = forms.EmailField(required=True)
    question = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    questiontags = forms.CharField(required=True)
    codesnippets = forms.CharField(required=True)
