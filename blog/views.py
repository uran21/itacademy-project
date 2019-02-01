from functools import reduce
import operator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from blog.models import Post, Theme
from blog.forms import PostForm, ThemeForm

def home(request):
	posts=Post.objects.all()
	return render(request, 'articles/home.html',{
		'posts':posts
	})
	
	
def post(request, pk):
	blog_post=Post.objects.get(id=pk)
	# Post.objects.filter()
	return  render(request, 'articles/post.html',{
		'post':blog_post
	})
	
def theme(request, pk):

	blog_theme=Theme.objects.get(id=pk)
	posts=Post.objects.filter(theme=blog_theme)
	
	return  render(request, 'articles/home.html',{
		'posts':posts
	})
	
	
def add_post(request):
	if request.method=='POST':
		form=PostForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect(reverse('blog:home'))
	else:
		form=PostForm()
	
	
	return  render(request, 'articles/add_post.html',{
		'form':form
	})
	
def add_theme(request):
	if request.method=='POST':
		form=ThemeForm(request.POST,request.FILES)
		
		if form.is_valid():
			form.save()
			return redirect(reverse('blog:home'))
	else:
		form=ThemeForm()
	
	
	return  render(request, 'articles/add_theme.html',{
		'form':form
	})
	
def search_result(request):
	q=request.GET.get('q')
	use_content=request.GET.get('content')
	fltr=request.GET.get('find')
	# if use_content:
		# posts=Post.objects.filter(
			# Q(title__icontains=q)| Q(content__icontains=q)
		# )
	# else:
		# posts=Post.objects.filter(title__icontains=q)
	# query = [Q(title__icontains=q)]
	
	# if use_content:
		# query.append(Q(content__icontains=q))
	
		# posts=Post.objects.filter(reduce(operator.or_, query))
		
	# return render(request, 'articles/home.html', {
		# 'posts':posts,
		# 'q':q
		# })
			
	if (fltr=='all'):
		if use_content:
			posts=Post.objects.filter(
				Q(title__icontains=q)| Q(content__icontains=q)
			)
		else:
			posts=Post.objects.filter(title__icontains=q)
			
		return render(request, 'articles/home.html', {
			'posts':posts,
			'q':q
			})
	elif (fltr=='ex'):
		if use_content:
			posts=Post.objects.filter(
				Q(title__iexact=q)| Q(content__iexact=q)
			)
		else:
			posts=Post.objects.filter(title__iexact=q)
		return render(request, 'articles/home.html', {
			'posts':posts,
			'q':q,
				
			})
	elif (fltr=='st'):
		if use_content:
			posts=Post.objects.filter(
				Q(title__istartswith=q)| Q(content__istartswith=q)
			)
		else:
			posts=Post.objects.filter(title__istartswith=q)
		return render(request, 'articles/home.html', {
			'posts':posts,
			'q':q,
				
			})
	elif (fltr=='en'):
		if use_content:
			posts=Post.objects.filter(
				Q(title__iendswith=q)| Q(content__iendswith=q)
			)
		else:
			posts=Post.objects.filter(title__iendswith=q)
		return render(request, 'articles/home.html', {
			'posts':posts,
			'q':q,
		
			})
	 	