from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, Category
from .forms import PostForm, editForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        #precisamos enviar para o html home
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


class DetalhesView(DetailView):
    model = Post
    template_name = 'detalhes.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #iremos puxa todas as fields do model
    #fields = '__all__'
    #podemos definit apenas algums fields
    #fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    #iremos puxa todas as fields do model
    #fields = '__all__'
    #podemos definit apenas algums fields
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = editForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def CategoryView(request, cats):
    #consulta ao banco de dados

    category_posts = Post.objects.filter(category=cats.replace('-', ''))

    return render(request, 'categories.html', {'cats': cats.title().replace('-', ''), 'category_posts': category_posts})