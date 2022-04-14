# Define closure. 
def print_msg(msg): # enclosing func
    def printer(m): # nested func
        print(msg+m)
    return printer # must return nested func

P = print_msg("hello ")
P("world")