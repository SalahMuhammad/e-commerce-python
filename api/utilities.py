import json

def requestHandler(request):
    """ This method copies the request and converts it's data -
    's-keys', 's-values' into json dumps then set it to specifications field.
    """
    edited_request = request
    content_type = edited_request.META.get('CONTENT_TYPE')
    specifications = {}

    if 'application/x-www-form-urlencoded' in content_type:
        keys_list = edited_request.data.getlist('s-keys')
        values_list = edited_request.data.getlist('s-values')

        if len(keys_list) == len(values_list) > 0:
            edited_request.data._mutable = True

            for i in range(len(keys_list)):
                specifications[keys_list[i]] = values_list[i]

            edited_request.data['specifications'] = json.dumps(specifications)
            edited_request.data._mutable = False
    elif 'application/json' in content_type:
        pass

    return edited_request