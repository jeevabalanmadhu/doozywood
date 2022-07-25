from .models import Post, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm,ChoicesForm,EventForm,TalentForm,ContactForm,ShowForm,RentalForm
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 30

    def get_queryset(self):
        try:
            keyword = self.request.GET['q']
        except:
            keyword = ''
        if (keyword != ''):
            object_list = self.model.objects.filter(
                Q(content__icontains=keyword) | Q(title__icontains=keyword))
        else:
            object_list = self.model.objects.all()
        # print(object_list)
        return object_list

class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    
    template_name = 'post_detail.html'
    if Post.form_choice == '1':
        title = Post.From+" to "+Post.to
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    post_choice = '0'
    template_name = 'post_form.html'
    def get_form_class(self):
       post_choice = self.request.GET.get('post_select', '1')
       
       self.post_choice= post_choice
       if post_choice == '1':
        return ShowForm

       if post_choice == '2':
            return TalentForm

       if post_choice == '3':
            return EventForm   

       if post_choice == '4':
            return RentalForm

       if post_choice == '5':
            return ContactForm  



    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['select_form'] = ChoicesForm()
        
        return context    
       
 
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.form_choice = self.post_choice
        if form.instance.form_choice == '1':
            form.instance.title = "added event from "+str(form.instance.From)+" to "+str(form.instance.to)+" in "+form.instance.location
        elif form.instance.form_choice == '4':
            form.instance.title = "posted show on "+str(form.instance.show_language)+" "+str(form.instance.genre) +" "+form.instance.show+" "+form.instance.name
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Post
    
    # post_choice = Post.form_choice
    if Post.form_choice == '3':
        fields = ['From','to','img','location','description','tags']        

    if Post.form_choice == '1':
        fields = ['talent','language','location','img','description','tags']
    
    template_name = 'post_form.html'
    
    def form_valid(self, form):
        
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def update_post(request, pk):
    post = Post.objects.get(id=pk)
    
    post_choice = post.form_choice
    # print(post_choice)
    fields='__all__'
    if post.form_choice == '1':
        form = ShowForm(instance=post)  

    if post.form_choice == '2':
        form = TalentForm(instance=post)  
    
    if post.form_choice == '3':
        form = EventForm(instance=post)  
    
    if post.form_choice == '4':
        form = RentalForm(instance=post) 

    if post.form_choice == '5':
        form = ContactForm(instance=post) 
    
    template_name = 'post_form_update.html'    
    if request.method == 'POST':
        if post.form_choice == '1':
            form = ShowForm(request.POST, instance=post)

        if post.form_choice == '2':
            form = TalentForm(request.POST, instance=post)
        
        if post.form_choice == '3':
            form = EventForm(request.POST, instance=post)
        
        if post.form_choice == '4':
            form = RentalForm(request.POST, instance=post)

        if post.form_choice == '5':
            form = ContactForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/')

    content = {'form':form, }
    return render(request,template_name,content)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'about.html', {'title': 'About'})


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        user = User.objects.get(id=request.POST.get('user_id'))
        text = request.POST.get('text')
        Comment(author=user, post=post, text=text).save()
        messages.success(request, "Your comment has been added successfully.")
    else:
        return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)
