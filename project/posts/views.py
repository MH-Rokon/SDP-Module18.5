from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.decorators import login_required

@login_required 
def add_post(request):
    if  request.method == 'POST':
      post_form=forms.PostForm(request.POST)
      if post_form.is_valid():
         post_form.instance.author=request.user
         post_form.save()
         return redirect("add_post")
    else:   
        post_form=forms.PostForm()
    return render(request,'add_post.html',{'form':post_form})
