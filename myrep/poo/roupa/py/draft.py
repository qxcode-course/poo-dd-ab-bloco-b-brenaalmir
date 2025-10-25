class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor) -> bool:
        tamanhos_validos =["PP","P","M","G","GG","XG"]
        valor = valor.strip().upper()

        if valor in tamanhos_validos:
            self.__tamanho = valor 
            return True
    
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return False

    def show(self):
        tamanho_str = self.__tamanho 
        print(f"size: ({tamanho_str})")

if __name__== "__main__":
    roupa = Roupa()

    while True:
        comando = input().strip().split()

        if not comando:
            continue

        if comando[0] == "show":
            print("$show")
            roupa.show()

        elif comando[0] == "size" and len(comando) > 1:
            print(f"$size {comando[1]}")
            roupa.setTamanho(comando[1])

        elif comando[0] == "end":
            print("$end")
            break