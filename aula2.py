# criar uma função para calcular a area de um circulo
'''
def circulo(raio):
    pi = 3.1415926
    area = pi * (raio**2)
    return area

x = int(input())
print("Digite um valor do raio para calcularmos o valor da area do circulo" + circulo(x))
'''

'''
def aplicar_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final

print(aplicar_desconto(80, 10))
'''

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

x = int(input())
print(celsius_para_fahrenheit(x))