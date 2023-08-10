def proccessStrParams(*args: str):
    """
        this function takes query string arguments,
        and split each argument in , sign,
        then convert each value in this array to integer,
        after proccess all params, 
        it returns all params as array with the same order that function takes
    """
    params = []

    for param in args:
        if param != '':
            try:
                params.append([int(i) for i in param.split(',')])
            except AttributeError:
                pass
            except ValueError:
                params.append([])
        else:
            params.append([])

    return params
