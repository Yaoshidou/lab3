#-×-coding:utf-8-*-
#表单定义文件
from django import forms
from django.forms import ModelForm
from models import Book, Author
class CreateBookForm(ModelForm):
    AuthorID = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = "__all__"
class CreateAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
class ChangeBookForm(forms.Form):
    ISBN = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"readonly":True}))
    Title = forms.CharField(max_length=20)
    AuthorID = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label=None)
    Publisher = forms.CharField(max_length=20)
    PublishDate = forms.DateField()
    Price = forms.FloatField()
class ChangeAuthorForm(forms.Form):
    AuthorID = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"readonly":True}))
    Name = forms.CharField(max_length=20)
    Age = forms.IntegerField()
    Country = forms.CharField(max_length=50)
