class Roupa:
    def __init__(self):
        self.tamanho = None

    def setTamanho(self, valor):
        tamanhos_validos = ["PP","P","M","G","GG","XG"]
        valor = valor.strip().upper()

        if valor in tamanhos_validos:
            self.tamanho = valor 
            
            print(f"Tamanho da roupa escolhido como{self.tamanho} .")
            return True

        else:
            print(f"Tamanho inválido! Os tamanhos permitidos são: {', '.join(tamanhos_validos)}.")
            return False

if _name=="main_":
    roupa = Roupa()

    while True:
        tamanho_input = input ("Escolha o tamanho da roupa (PP,P,M,G,GG,XG):")    
        if roupa.setTamanho(tamanho_input):
            break

    print(f"Tamanho final da roupa {roupa.tamanho}.")