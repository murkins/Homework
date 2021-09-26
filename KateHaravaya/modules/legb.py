a = "I am global variable!"

def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        #a = "I am local variable!"

        # task 2.1
        # global a

        # task 2.2

        print(a)

    # task 1
    inner_function()