from django import forms


class PromptForm(forms.Form):
    # prompt = forms.CharField(label='Prompt', max_length=100)
    prompt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control-lg w-100 prompt-input', "placeholder": "Enter a prompt: a running black man"}))
    # Add more fields as needed
