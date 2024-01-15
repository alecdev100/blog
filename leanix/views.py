from django.views import generic
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class ListView(generic.ListView):
    template_name = 'leanix/home.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='Pub').order_by('datetime_modified')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'leanix/post_detail.html'
    context_object_name = 'post'


class CreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'leanix/post_create.html'


class UpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'leanix/post_create.html'


class DeleteView(generic.DeleteView):
    model = Post
    template_name = 'leanix/post_delete.html'
    success_url = reverse_lazy('home')
