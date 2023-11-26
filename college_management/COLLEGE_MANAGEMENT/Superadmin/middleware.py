from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print("=========================",modulename)
        user = {}

        for key, value in request.session.items():
            user[key] = value
        # print(user)
        
        try:
            if user['is_authenticated']:
                if user['role'] == 'Superadmin':
                    if modulename != 'Superadmin.views' and modulename != 'Home.views':
                        return redirect(reverse('home'))

                elif user['role'] == 'Admin':
                    print(user['role'])
                    if modulename != 'Admins.views' and modulename != 'Home.views':
                        return redirect(reverse('home'))

                elif user['role'] == 'Subadmin':
                    if modulename != 'Subadmin.views' and modulename != 'Home.views':
                        return redirect(reverse('home'))

                elif user['role'] == 'Faculty':
                    if modulename != 'Faculty.views' and modulename != 'Home.views':
                        return redirect(reverse('home'))

                elif user['role'] == 'Student':
                    if modulename != 'Student.views' and modulename != 'Home.views':
                        return redirect(reverse('home'))
                else:
                    return redirect(reverse('login'))
            else:
                if request.path == reverse('login') or modulename == 'django.contrib.auth.views' or request.path == reverse('login'):
                    pass
                else:
                    return redirect(reverse('login'))
        except Exception as e: 
            print(e)
            if request.path == reverse('login') or request.path == reverse('post-login') or request.path == reverse('home') or modulename == 'django.contrib.auth.views' or request.path == reverse('login'):
                pass
            else:
                return redirect(reverse('login'))
