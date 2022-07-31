from django import forms
class libform(forms.Form):
    Book_name = forms.CharField(max_length=30)
    Book_author = forms.CharField(max_length=30)
    Book_category = forms.CharField(max_length=30)
    Book_shelf = forms.CharField(max_length=30)
    Number_of_available_copies = forms.IntegerField()
    isbn = forms.CharField( max_length=13)
    Image = forms.ImageField(required=False)


class Sform(forms.Form):
    Book_name = forms.CharField(max_length=30)
class returnss(forms.Form):
    Return_Code = forms.CharField(max_length=30)






