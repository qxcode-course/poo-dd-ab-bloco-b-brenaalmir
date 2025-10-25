  class Roupa:
    def __init__(self):
        self.tamanho = ""

    def setTamanho(self, valor):
        tamanhos_validos =["PP","P","M","G","GG","XG"]
        valor=valor.strip().upper()

        if valor in tamanho_validos:
            self.tamanho = valor 
            print(f"Tamanho da roupa escolhido como{self.tamanho} .")
            return True

        else:
            print (f"tamanho invalido colega, só pode :{','.join}")
