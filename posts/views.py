from django.http import  HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import  get_object_or_404, redirect, Http404
from django.shortcuts import render
from django.db.models import Q
from .models import Post
# import the form
from .forms import PostForm


# create new post function
def post_create(request):
	# permeation  for create the posts
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "form.html", context)


# see the details in new page
def post_detail(request, id = None):   # retrieve

	instance = get_object_or_404(Post, id=id)
	# share_string = quote_plus(instance.content)

	context = {
		"title": instance.title,
		"instance": instance,

	}
	return render(request, "details.html", context)

# view all posts in the same page
def post_list(request):


	queryset_list=Post.objects.active()
	#  sherch function
	query = request.GET.get("find")
	if query:
		queryset_list = queryset_list.filter(
			 Q(title__contains=query)|
			 Q(content__contains=query)
			).distinct()

	# paginator use for crating pages for contaent
	paginator = Paginator(queryset_list, 6)   # nuomber of the postes in the page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"x": queryset,
		"title": "List"
	}
	return render(request, "index.html", context)


# up date the conant of the post
def post_update(request, id = None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance= get_object_or_404(Post, id = id)
	form=PostForm(request.POST or None , request.FILES or None,  instance=instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "form.html", context)

#   get it fuck a way


def post_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	return redirect("posts:list")


# comic page
def comic(request):
	return render(request, "comic.html")

# Success
def success(request):
	return render(request, "success.html")

# sport
def sport(request):
	return render(request, "sport.html")
# art
def art(request):
	return render(request, "art.html")
# static pages
def about(request):
	return render(request, "about.html")

def policy(request):
	return render(request, "policy.html")
# def features(request):policy
