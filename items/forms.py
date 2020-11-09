from django import forms


class CategoryForm(forms.Form):
    genre = forms.CharField(max_length=50, widget=forms.ModelChoiceField(attrs={'class': 'myselectform'}))