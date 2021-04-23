from django.http import HttpResponseForbidden
from django.shortcuts import redirect
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_anonymous:
            return self.get_response(request)
        if request.user.is_authenticated:
            if not request.user.is_active:
                return HttpResponseForbidden("Your account is not active")
        return self.get_response(request)
            # return HttpResponseForbidden("Your account is not active")
        # return redirect("/login")
        # Code to be executed for each request/response after
        # the view is called.
        

        