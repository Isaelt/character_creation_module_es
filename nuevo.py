from math import sqrt

message: str = ('Bienvenidos al mejor programa jamas hecho para obtener '
                'la raíz cuadrada de un número')
print(message)


def calculatesquareroot(number):
    """Calcula la raíz cuadrada."""
    return sqrt(number)


def calc(your_number: float) -> str:
    if your_number <= 0:
        return None
    raiz = calculatesquareroot(your_number)
    return print(f'Calculamos la raíz cuadrada de tu número.'
                 f'Es igual a {raiz}')


calc(25.5)
