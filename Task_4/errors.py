def input_error(func):
    def inner(*args, **kwargs):
        for args in args :
            if args == "add":
                try:
                   return func(*args, **kwargs)
                except ValueError:
                   return "Give me name and phone please."
            if args == "change" and kwargs[0] == contacts[name]:
                try:
                    return func(*args, **kwargs)    
                except KeyError: 
                    return "Give me name correct name"

    return inner


    # def inner(args, contacts):
    #     for item in args:
    #         if :
                
   