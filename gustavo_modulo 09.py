# Guia de Programação: Tratamento de Erros (Módulo 09)

def aula_tratamento_erros():
    print("--- Desafio 1: Divisão ---")
    try:
        numerador = int(input("Digita o numerador: "))
        denominador = int(input("Digita o denominador: "))
        resultado = numerador / denominador

    except ValueError:
        print("Erro: Digita apenas números inteiros!")

    except ZeroDivisionError:
        print("Erro: Não podes dividir por zero.")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    else:
        print(f"Sucesso! Resultado: {resultado}")

    finally:
        print("--- Fim da Divisão ---")


aula_tratamento_erros()


# Desafio 2: Telemóvel e Duração (Tratando o Input)
class Celular:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def fazer_chamada(self, duracao):
        try:
            gasto = int(duracao) * 2

            if self.bateria >= gasto:
                self.bateria -= gasto
                print(f"Chamada de {duracao} min feita! Bateria: {self.bateria}%")
            else:
                print("Bateria insuficiente.")

        except ValueError:
            print("Erro: A duração deve ser um número inteiro!")


meu_celular = Celular("Samsung", "S24")
meu_celular.fazer_chamada("Dez")  


# Desafio 3: Telemóvel e Custo (Tratando Tipos de Dados)
class Celular:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def fazer_chamada(self, custo_bateria):
        print(f"\n--- Chamada no {self.modelo} ---")

        try:
            self.bateria -= custo_bateria

        except TypeError:
            print("ERRO: O custo da bateria deve ser um número!")

        else:
            print(f"Sucesso! Bateria atual: {self.bateria}%")

        finally:
            print("Sistema finalizado.")


meu_celular = Celular("Samsung", "S24")
meu_celular.fazer_chamada("muito")  


# Desafio 4: Status de Bateria (Lógica + Erros)
class Celular:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def verificar_status(self):
        try:
            entrada = input(f"Bateria do {self.modelo}: ")
            nivel = float(entrada)

            if nivel < 0 or nivel > 100:
                print("Valor inválido! Digite de 0 a 100.")

            elif nivel < 15:
                print(f"⚠️ Bateria em {nivel}%. Carregue já.")

            elif nivel > 85:
                print(f"✔️ Bateria em {nivel}%. Carga excelente!")

            else:
                print(f"🔋 Bateria em {nivel}%. Status normal.")

        except ValueError:
            print("Erro: Digite apenas números!")


cel = Celular("Samsung", "S24")
cel.verificar_status()