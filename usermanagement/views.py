from django.shortcuts import render, redirect
from usermanagement.models import *
from .forms import *
import json
import requests
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
import appraisal.settings
from django.conf import settings
from django.utils import timezone
import datetime, time
from datetime import datetime


# Create your views here.

def login(request):
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            return redirect('usermanagement:dashboard')
    else:
        form = LoginForm
        return render(request, 'user/login.html', {'form': form})


def login_validate(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form['username'].value()
        password = form['password'].value()
        try:

            user=User.objects.get(username=username)
            if user:
                if user.username == username:
                    groupid = user.group.split(',')
                    request.session['logged_in'] = True
                    request.session['username'] = user.username
                    request.session['firstname'] = user.first_name
                    request.session['id'] = user.pk
                    request.session['group_id'] = groupid
                    logindate = datetime.now()
                    Log.objects.create(
                        user_id=request.session['id'],
                        date_time=logindate,
                        login_data=logindate,
                        action='1',
                        component='login',
                        ip=request.META.get('REMOTE_ADDR')
                        # ip=request.META.get('HTTP_X_REAL_IP')
                    )
                    return redirect("usermanagement:dashboard")
                else:
                    messages.error(request, 'Incorrect  User name  or Password')
                    return redirect('usermanagement:login')
            else:
                obj = {
                    "username": username,
                    "password": password
                }
                payload = json.dumps(obj)
                headers = {'Content-Type': 'application/json'}
                try:
                    re = requests.post(settings.HRMLOGIN, data=payload, headers=headers)
                    ress = re.json()
                    print(ress)
                    if ress["isLoginSuccess"] == True:
                        user = User.objects.get(username=username, is_active=1)
                        groupid = user.group.split(',')
                        request.session['logged_in'] = True
                        request.session['username'] = user.username
                        request.session['firstname'] = user.first_name
                        request.session['id'] = user.pk
                        request.session['group_id'] = groupid
                        logindate = datetime.now()
                        Log.objects.create(
                            user_id=request.session['id'],
                            date_time=logindate,
                            login_data=logindate,
                            action='1',
                            component='login',
                            ip=request.META.get('REMOTE_ADDR')
                            # ip=request.META.get('HTTP_X_REAL_IP')
                        )
                        return redirect("usermanagement:dashboard")
                    else:
                        messages.error(request, 'Incorrect  User name  or Password')
                        return redirect('usermanagement:login')
                except Exception as e:
                    print(e)
                    messages.error(request, 'Smart Enterprise Connection Error!')
                    return redirect('usermanagement:login')
        except Exception as e:
            print(e)
            messages.error(request, 'Account is not active. Please contact HR.')
            return redirect('usermanagement:login')
    else:
        return render(request, 'user/login.html', {'form': form})


def dashboard(request):
    module = list()
    user = User.objects.get(id=request.session['id'])
    user_permissions = Privileged.objects.filter(group_id=user.group)
    module = Privileged.objects.filter(group_id=user.group).values('module_type_id').distinct()
    list_result = [entry for entry in module]
    request.session['module'] = list_result
    try:
        urls = list()
        for p in user_permissions:
            userurl = Moduleurl.objects.filter(id=p.moduleurl_id)
            for url in userurl:
                urls.append(url.url)
                request.session['urls'] = urls
    except:
        user = None
    userdata = {
        'user_id': request.session['id'],
        'username': request.session['username'],
        'firstname': request.session['firstname'],
        'urls': urls,
        'module': module,
    }
    context = {'data': userdata}
    return render(request, 'user/dashboard.html', context)


def logout(request):
    user_log = Log.objects.filter(user_id=request.session['id']).last()
    user_log.logout_data = datetime.now()
    user_log.save()
    try:
        del request.session['logged_in']
        return redirect('usermanagement:login')
    except:
        return redirect('usermanagement:login')
