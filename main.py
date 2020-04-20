def convertir_cadena(numeros):
    # recibe un array de numeros, y devuelve un nuevo array de cadenas segun si el numero es divisible por x numero o si esta incluido
    cadena = []
    for numero in numeros:
        if numero % 3 == 0 and numero % 5 == 0:
            cadena.append("FizzBuzz")
        elif numero % 3 == 0 or '3' in str(numero):
            cadena.append("Fizz")
        elif numero % 5 == 0 or '5' in str(numero):
            cadena.append("Buzz")
    return cadena


# verifico que el programa cumpla con lo pedido
assert convertir_cadena([15]) == ["FizzBuzz"]
assert convertir_cadena([3]) == ["Fizz"]
assert convertir_cadena([5]) == ["Buzz"]
assert convertir_cadena([5, 3, 15]) == ["Buzz", "Fizz", "FizzBuzz"]
assert convertir_cadena([-15, -10, -5, -3, 1, 3, 5, 10, 15, 18, 20]) == ["FizzBuzz",
                                                                         "Buzz", "Buzz", "Fizz", "Fizz", "Buzz", "Buzz", "FizzBuzz", "Fizz", "Buzz"]
