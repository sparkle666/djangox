from django import forms


class PromptForm(forms.Form):
    prompt = forms.CharField(label='Prompt', max_length=100)
