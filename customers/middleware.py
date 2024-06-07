# your_app/middleware.py
from django.http import JsonResponse

class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(response)
        if response.status_code == 404:
            error_message = 'Url not valid.'
            return JsonResponse({'error': error_message}, status=500)
        return response

