from django.shortcuts import render
# from django.core.urlresolvers import resolve
from functools import wraps
from configuration.models import Privileged
from configuration.models import User
from django.contrib import messages
from django.shortcuts import redirect
# import ipdb
from django.urls import resolve
from django.http import HttpResponse, HttpResponseRedirect


def access_permission_required(view_func):
    """This is The custome decorator for checking permission of a controller function"""
    def _decorator(request, *args, **kwargs):
        # #check if the user has proper permission to access this function
        myfunc, myargs, mykwargs = resolve(request.get_full_path())
        view_function = myfunc.__name__
        user = request.session['id']
        if user is None:
            return render(request, 'user/login.html')
        user_profile = User.objects.get(id=user)
        role_id = user_profile.group
        access = Privileged.objects.filter(group_id=role_id, moduleurl__url=view_function)
        if not access.exists():
            return render(request, 'user/404.html')
        response = view_func(request, *args, **kwargs)
        # maybe do something after the view_func call
        return response
    return wraps(view_func)(_decorator)

def login_required(session_key, fail_redirect_to):
    def _session_required(view_func):
        @wraps(view_func)
        def __session_required(request, *args, **kwargs):
            try:
                session = request.session.get(session_key)
                if session is None:
                    raise ValueError('Login Session is Expired Please Login Again!')
            except KeyError as e:
                messages.error(request, 'Login Session is Expired Please Login Again!')
                return redirect(fail_redirect_to)
            except ValueError as e:
                messages.error(request, 'Login Session is Expired Please Login Again!')
                return redirect(fail_redirect_to)
            else:
                return view_func(request, *args, **kwargs)
        return __session_required
    return _session_required


def session_required(session_key, fail_redirect_to):
    def _session_required(view_func):
        @wraps(view_func)
        def __session_required(request, *args, **kwargs):
            current_url = resolve(request.path_info).url_name
            request.session['redirect_to'] = 'epub:' + current_url
            # print (request.session['redirect_to'])
            # ipdb.set_trace()
            try:
                session = request.session.get(session_key)
                if session is None:
                    raise ValueError('Login Session is Expired Please Login Again!')
            except KeyError as e:
                # messages.error(request, 'You Are Not Logged In!')
                return redirect(fail_redirect_to)
            except ValueError as e:
                # messages.error(request, e.message)
                return redirect(fail_redirect_to)
            else:
                return view_func(request, *args, **kwargs)
        return __session_required
    return _session_required
