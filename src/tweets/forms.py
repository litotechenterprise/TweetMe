from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            "user",
            "content",
        ]

    # Simple Validation of data
        def clean_content(self, *args, **kwargs):
            content = self.cleaned_data.get("content")
            if content == "abc":
                raise forms.ValidationError("Cannot be ABC")
            return content