from django.http import HttpResponseRedirect

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # User is not authenticated, perform actions here
            # For example, you can redirect them to the login page
            return HttpResponseRedirect('/login/')
        return self.get_response(request)
