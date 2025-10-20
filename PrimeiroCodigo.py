def saudacao(nome):   #para criar uma função= primeiro digitamos "def", depois o nome da função
                      # E em seguida usamos () - que podem ter ou nao variaveis.
                      #outra nomeclatura para variavel aqeui é chamado de "parâmetro";
                      # def faz o pyton entender que voce esta fazendo uma funçao . 2*nome da função "saudação" 3*parenteses
                      #4*elementos opicional variavel.o que vai dentro dos parenteses
                      #print mostra as informações

    print(f"Eae!, {nome}!") # "print" é o comando que imprime algo no terminal.

saudacao("Nady")  # aqui esta um exemplo sobre como ativar/chamar uma funçao = colocamos o nome dela 
                  # e fornecemos o que ela precisa.

def soma(a,b):
    resultado = a + b 
    return resultado #"return = tornar o resultado visil fora da funçao, manipula uma funçao dela, voce pode mexer"

total = soma(6, 10)
print(total)

def subtracao(a, b): #tudo que esta dentro do parenteses è figurativo.
    resultado = a - b
    return resultado

print(subtracao(10, 8))

def divisao(a, b):
    print("Não realize divisão por 0")
    resultado = a / b
    return resultado

print(divisao(10, 2))

def multiplicacao(a, b):
    resultado = a * b
    return resultado

print(multiplicacao(5, 3))

def media(a, b):
    resultado = (a+b) / 2
    return resultado

print(media(1,2))

# variavel inteiros 123  ex: 3.14
# variavel extreme abc ex: x="1" lidos como textos.
