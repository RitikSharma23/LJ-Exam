from django.http import HttpResponseRedirect

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request):
        # Skip authentication check for the login page
        session_data = dict(request.session)
        print("Session Data:", session_data)
        
        # if(session_data['is_authenticated']):
        if "is_authenticated" in session_data:
          if not session_data['is_authenticated'] and request.path != '/login/' and request.path != '/post-login/':
              return HttpResponseRedirect('/login/')
          return self.get_response(request)
        else:
          request.session['is_authenticated'] = False
          return HttpResponseRedirect('/login/')
          
