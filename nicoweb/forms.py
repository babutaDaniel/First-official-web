from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')
choices_list = []
for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','category', 'body','upload_image','post_date')
        labels = {
            'title': '',
            'title_tag': '',
            'author':'' ,
            'category': '',
            'body': '',
            'upload_image':'',
            'post_date':'',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title Tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'user', 'type':'hidden','placeholder':'author' }),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control','placeholder':'Category'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'About'}),
            'upload_image':'',
            'post_date':forms.TextInput(attrs={'placeholder':'Post Date',}),
        }
