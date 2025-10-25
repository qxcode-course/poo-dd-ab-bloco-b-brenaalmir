class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str) -> bool:
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        valor = valor.strip().upper()

        if valor in tamanhos_validos:
            self.__tamanho = valor
            print(f"Tamanho da roupa escolhido como {self.__tamanho}.")
            return True
        else:
            print(f"Tamanho inválido! Os tamanhos permitidos são: {', '.join(tamanhos_validos)}.")
            return False


# loop principal 
roupa = Roupa()

while roupa.getTamanho() == "":  
    print("Digite seu tamanho de roupa:")
    tamanho = input()
    roupa.setTamanho(tamanho)

print(f"Parabéns, você comprou uma roupa tamanho {roupa.getTamanho()}.")