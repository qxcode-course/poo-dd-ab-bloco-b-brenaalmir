class Chinela:
 def __init__(self):
    self.tamanho = 0

 def setTamanho(self, valor):
    if not isinstance(valor, int):
        print("Erro, resposta invalida")
        return False

    if valor < 20 or valor > 50:
        print ("Erro, só pode entre 20 e 50")
        return False

    if valor % 2 != 0:
        print("Erro, só pode número par")
        return False


    self.tamanho = valor 
    print(f"tamanho da chinela escolhido {self.tamanho}.")
    return True

if __name__=="__main__":
    Chinela = Chinela()


    while True:
        try:
            valor = int(input("digite aqui o tamanho da porcaria dessa sua chinela de merda(20 a 50, apeas merdas de números pares): "))
            if Chinela.setTamanho(valor):
                break
        except ValueError:
                print("digita um número inteiro porra!")

        print(f"tamanho da chinela{Chinela.tamanho}")