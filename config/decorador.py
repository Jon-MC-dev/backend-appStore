def ejecuteConsult(funcion):
    def new_function(a, b):
        print("Funcion llamada!")
        return funcion(a, b)
    return new_function


@ejecuteConsult
def add(a, b):
    return a + b
print(add(7, 5))
