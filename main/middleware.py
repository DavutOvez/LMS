from django.shortcuts import redirect

def simple_middleware(get_response):

    def middleware(request):
        if request.path != '/login/':
            if not request.user.is_authenticated:
                return redirect('/login/')
            
        response = get_response(request)
        
        return response

    return middleware