# 1° criem uma classe chamada "calculadora". 2°
# 2° criem todas as funcões basicas de operações. 3°
# 3° não permita divisão por 0!. 4°
# 4° o algoritimo só pode parar quando, no menu, eu digitar 0. 5°
# 5° salve os resultados em um banco de dados 1°
# 6° não tem html nem css.

import sqlite3

class BancoDeDados:
    def __init__(self, arquivo = 'banco.db'):
        self.arquivo = arquivo
              

    def conectar(self):
        conexao = sqlite3.connect(self.arquivo)
        return conexao
    
    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resultados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operacao TEXT,
                a INTEGER,
                b INTEGER,
                resultado REAL
            )
        """)

        conexao.commit()
        conexao.close()

    def salvar_valores(self, operacao, a, b, resultado):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO resultados (operacao, a, b, resultado) VALUES (?, ?, ?, ?)",
            (operacao, a, b, resultado)
        )
        conexao.commit()
        conexao.close()
# classe são funcionalidade onde tem que estanciar
class Calculadora:
    def __init__(self, banco): # para estanciar e disser como funciona uma classe 
        self.banco = banco 

    def somar(self, a, b):
        resultado = a + b
        self.banco.salvar_valores("soma", a, b, resultado)
        return resultado
    
    def subtracao(self, a, b):
        resultado = a - b
        self.banco.salvar_valores("subtracao", a, b, resultado)
        return resultado
    
    def multiplicacao(self, a, b):
        resultado = a * b
        self.banco.salvar_valores("multiplicacao", a, b, resultado)
        return resultado
    
    def divisao(self, a, b):
        if b == 0:
            print("Erro: Divisão por zero não é permitida!")
            return None
        else: 
            resultado = a / b
            self.banco.salvar_valores("divisao", a, b, resultado)
            return resultado
        
def main():
    banco = BancoDeDados()
    banco.criar_tabela()
    calculadora = Calculadora(banco)

    while True:
        print("Bem-Vindo a nossa calculadora!")
        print("--------------------------------------")
        print("[1] - Somar!")
        print("[2] - Subtrair!")
        print("[3] - Multiplicar!")
        print("[4] - Dividir!")

        opcao = input("Escolha uma opcão: ")

        if opcao == "0":
            print("Encerrando a nossa calculadora, Tchau! ")
            break
        elif opcao not in {"1", "2", "3", "4"}:
            print("opcão onválida. Tente novamente.")
            continue

        primeiro = input("Digite o primeiro número inteiro: ")
        segundo = input("Digite o segundo número inteiro: ")

        if not (primeiro.isdigit() and segundo.isdigit):
            print("Erro: Digite apenas números inteiros  positivos.")
            continue

        a = int(primeiro)
        b = int(segundo)

        if opcao == "1":
            resultado = calculadora.somar(a, b)
            print("o resultado é:", resultado)
        elif opcao == "2":
            resultado = calculadora.subtracao(a, b)
            print("o resultado é", resultado)
        elif opcao == "3":
            resultado = calculadora.multiplicacao(a, b)
            print("o resultado é", resultado)
        elif opcao == "4":
            resultado = calculadora.divisao(a, b)
            print("o resultado é", resultado)

if __name__ == "__main__":
    main()
                    

        
        