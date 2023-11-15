from django.http import QueryDict

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            custom_querydict = QueryDict(request.body)
            custom_querydict = custom_querydict.copy()
            # Modify the custom_querydict as needed
            custom_querydict['field1'] = 'ModifiedValue'  # Use b'' for bytes
            custom_querydict['field2'] = '99'  # Use b'' for bytes
            custom_querydict['specifications'] = 'soso'
            request.POST = custom_querydict.urlencode() # (s'utf-8')
        return self.get_response(request)