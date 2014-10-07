# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import Post
from forms import PostForm

class PostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('post-list')
    form_class = PostForm

class PostListView(ListView):
    model = Post
    queryset = Post.objects.order_by('-pub_date')
    context_object_name = 'post_list'
    
class PostDetailView(DetailView):
    model = Post
    
class PostUpdateView(UpdateView):
    model = Post
    success_url = reverse_lazy('post-list')
    form_class = PostForm
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
