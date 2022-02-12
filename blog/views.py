from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post/list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'caption')
    template_name = 'blog/post/create.html'
    success_url = reverse_lazy('blog:post-list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('caption',)
    context_object_name = 'post'
    template_name = 'blog/post/update.html'

    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'pk': self.kwargs['pk']})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post/delete.html'
    success_url = reverse_lazy('blog:post-list')
