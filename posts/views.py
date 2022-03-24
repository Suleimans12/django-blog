from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . forms import PostForm
from . models import Post 

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

	def test_func(self):
		return self.request.user.is_superuser

class PostCreateView(SuperUserRequiredMixin, FormView):
	template_name = 'posts/form.html'
	form_class = PostForm
	login_url = '/login/'
	success_url = '/create/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Create'
		return context
    
	def form_valid(self, form):
		post = form.save(commit=False)
		post.author = self.request.user
		post.save()
		return super().form_valid(form)

	def form_invalid(self, form):
		return super().form_invalid(form)


class PostIndexView(ListView):
	template_name = 'posts/index.html'
	queryset = Post.objects.all()
	context_object_name = 'post_list'


class PostDetailView(DetailView):
	template_name = 'posts/detail.html'
	queryset = Post.objects.all()
	context_object_name = 'post'


class PostUpdateView(SuperUserRequiredMixin, FormView):
	template_name = 'posts/form.html'
	form_class = PostForm
	login_url = '/login/'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update'
		return context
	
	def get_form(self):
		pk = self.kwargs['pk']
		instance = Post.objects.get(pk=pk)
		form = self.form_class(self.request.POST or None, self.request.FILES or None, instance=instance)
		return form
    
	def form_valid(self, form):
		post = form.save(commit=False)
		post.author = self.request.user
		post.save()
		return super().form_valid(form)

	def form_invalid(self, form):
		return super().form_invalid(form)