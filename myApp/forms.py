from django import forms
class Feedback(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    email=forms.EmailField()
    comments=forms.CharField(widget=forms.Textarea)
    def clean_name(self):
        n=self.cleaned_data['name']
        if(len(n)>10):
            raise forms.ValidationError("num of chars>10")
        