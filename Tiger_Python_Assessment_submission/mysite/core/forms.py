from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('full_name', 'email', 'chicago_collision_data', 'flight_call', 'light_levels')
