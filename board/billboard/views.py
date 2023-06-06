from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator
from .models import Post, Author
from .forms import SignUpForm, SignInForm, PostForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import FeedBackForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import CommentForm
from .models import Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class MainView(ListView):
    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        paginator = Paginator(posts, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'billboard/home.html', context={
            'page_obj': page_obj
        })


class PostDetailView(DetailView):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        last_posts = Post.objects.all().order_by('-id')[:5]
        comment_form = CommentForm()
        return render(request, 'billboard/post_detail.html', context={
            'post': post,
            'last_posts': last_posts,
            'comment_form': comment_form
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(Post, url=slug)
            comment = Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'billboard/post_detail.html', context={
            'comment_form': comment_form
        })


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'billboard/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'billboard/signup.html', context={
            'form': form,
        })


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'billboard/signin.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'billboard/signin.html', context={
            'form': form,
        })


class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'billboard/contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {subject}', message, from_email, ['ratushnyiaa@bk.ru'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'billboard/contact.html', context={
            'form': form,
        })


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'billboard/success.html', context={
            'title': 'Спасибо'
        })


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'billboard/post_edit.html'


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'billboard/post_edit.html', {'form': form})

class BaseRegisterView(CreateView):
    pass

class GetCode(CreateView):
    pass
    #

