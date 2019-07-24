from django.shortcuts import render, redirect
from repository import models
from backend.forms import ArticleForm, ArticleDetailForm


# Create your views here.
def article_list(request):
    all_articles = models.Article.objects.all()
    return render(request, 'backend/article_list.html', {'all_articles': all_articles})


def article_add(request):
    form_obj = ArticleForm()
    detail_form = ArticleDetailForm()
    title = '新增文章'
    if request.method == 'POST':
        detail_form = ArticleDetailForm(request.POST)
        if detail_form.is_valid():
            detail_form.save()

        qd = request.POST.copy()
        qd['detail'] = detail_form.instance.pk
        form_obj = ArticleForm(data=qd, files=request.FILES)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('backend:article_list')

        if detail_form.is_valid() and detail_form.instance:
            detail_form.instance.delete()

    return render(request, 'backend/article_form.html',
                  {'title': title, 'form_obj': form_obj, 'detail_form': detail_form})


def article_edit(request, pk):
    obj = models.Article.objects.filter(pk=pk).first()
    form_obj = ArticleForm(instance=obj)
    detail_form = ArticleDetailForm(instance=obj.detail)
    title = '编辑文章'
    if request.method == 'POST':
        detail_form = ArticleDetailForm(request.POST, instance=obj.detail)
        if detail_form.is_valid():
            detail_form.save()

        qd = request.POST.copy()
        qd['detail'] = detail_form.instance.pk
        form_obj = ArticleForm(data=qd, files=request.FILES, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('backend:article_list')

    return render(request, 'backend/article_form.html',
                  {'title': title, 'form_obj': form_obj, 'detail_form': detail_form})


def article_del(request, pk):
    obj = models.Article.objects.filter(pk=pk).first()
    obj.detail.delete()
    return redirect('backend:article_list')
