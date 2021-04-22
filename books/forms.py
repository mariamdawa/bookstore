from django import forms
from .models import Book,Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
    def clean (self):
        super(BookForm,self).clean()
        title=self.cleaned_data.get('title')

        if not len(title) >= 10 and len(title)<=50:
            raise forms.ValidationError("Book title must be between 10 and 50 characters.")
        
        return self.cleaned_data

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"
    def clean (self):
        super(CategoryForm,self).clean()
        name=self.cleaned_data.get('name')

        if len(name)<2:
            raise forms.ValidationError("Category must be more than 2 characters.")
        
        return self.cleaned_data