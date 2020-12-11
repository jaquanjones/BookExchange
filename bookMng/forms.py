from django import forms
from django.forms import ModelForm

from .models import Book, Review


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'category',
            'description',
            'picture',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'web': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'picture': forms.FileInput(attrs={
                'class': 'form-control-file',
                'id': 'image-upload',
                'required': True
            }),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'content'
        ]
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 10,
                }
            ),
        }

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = [
#             'items',
#             'first_name',
#             'last_name',
#             'email',
#             'address',
#             'country',
#             'state',
#             'zipcode'
#         ]
#         widgets = {
#             'first_name': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'last_name': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'email': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'address': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#             'address2': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 },
#             ),
#             'country': forms.ChoiceField(
#                 attrs={
#                     'class': 'custom-select d-block w-100',
#                 },
#                 choices='United States'
#             ),
#             'state': forms.ChoiceField(
#                 attrs={
#                     'class': 'custom-select d-block w-100'
#                 },
#                 choices='California'
#             ),
#             'zipcode': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             ),
#
#         }
