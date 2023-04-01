import funcoes as f


def calcule():
    a = input("Digite o primeiro número: ")
    b = input("Digite o segundo número: ")
    try:
      a = eval(a)  
    except (NameError, SyntaxError):
      pass
    try:
      b = eval(b)  
    except (NameError, SyntaxError):
      pass
    operacao = input("Digite qual operação deseja: ")

    match operacao:
      case 'soma' | '+':
        print(f.soma(a,b))
      case 'subtração' | '-':
        print(f.subtracao(a,b))
      case 'divisão' | '/':
        print(f.divisao(a,b))
      case 'multiplicação' | '*':
        print(f.multiplicacao(a,b))
      case _:
        print("Operação não reconhecida!")
