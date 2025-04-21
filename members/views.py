from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
#from task_app.models import create_predefined_categories

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse('task_app:list_task'))
        else:
            messages.success(request,"登陆信息错误，请重试……")
            return redirect('/members/login_user/')
    else:
        return render(request,'authenticate/login.html')

def logout_user(request):
    logout(request)
    return redirect(reverse('members:login_user'))

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 创建UserProfiel实例并保存用户信息
            profile = UserProfile.objects.create(
                user=user,
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"注册成功 !")
            return redirect(reverse('task_app:list_task'))
    else:
        form = RegisterUserForm()
    return render(request,'authenticate/register_user.html',context={'form':form})

# 用户资料
@login_required
def user_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '资料更新成功！')
            return redirect('members:user_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'authenticate/user_profile.html', {'form': form})