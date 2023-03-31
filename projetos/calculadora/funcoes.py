def soma(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser um número, recebido a={a}, tipo({type(a)}), b={b} tipo ({type(b)})")
    

def subtracao(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser um número, recebido a={a}, tipo({type(a)}), b={b} tipo ({type(b)})")


def divisao(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b == 0:
            raise ZeroDivisionError(f"Impossível dividir por zero!")
        else:
            return a / b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser um número, recebido a={a}, tipo({type(a)}), b={b} tipo ({type(b)})")
    

def multiplicaco(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser um número, recebido a={a}, tipo({type(a)}), b={b} tipo ({type(b)})")