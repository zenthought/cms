from django import forms
from repository import models


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field in self.fields.values(): #self.fields有序字典
            field.widget.attrs['class'] = 'form-control'


class ArticleDetailForm(forms.ModelForm):
    class Meta:
        model = models.ArticleDetail
        fields = "__all__"
