class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getCapacidade(self):
        return self.__capacidade

    def getCarga(self):
        return self.__carga

    def setCarga(self, valor: int):
        self.__carga = max(0, min(valor, self.__capacidade))

    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia

    def getPotencia(self):
        return self.__potencia

    def mostrar(self):
        print(f"(Potência {self.__potencia})")


class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        bat = f"({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})" if self.__bateria else "Nenhuma"
        car = f"(Potência{self.__carregador.getPotencia()})" if self.__carregador else "Desconectado"
        print(f"Status: {status}, Bateria: {bat}, Carregador: {car}")

    def ligar(self):
        if (self.__bateria and self.__bateria.getCarga() > 0) or self.__carregador:
            self.__ligado = True
            print("notebook ligado")

        else:
            print("não foi possível ligar")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notebook desligado")

    def usar(self, tempo: int):
        if not self.__ligado:
            print("notebook desligado")
            return

        if not self.__bateria and not self.__carregador:
            print("erro: sem bateria e sem carregador")
            self.__ligado = False
            return 

        if self.__bateria is None:
            print("Notebook utilizado com sucesso (carregador apenas)")
            return

        carga = self.__bateria.getCarga()

        if self.__carregador is None:
            if carga == 0:
                print("notebook descarregado")
                self.__ligado = False
                return
            if tempo > carga:
                print(f"Usando por {carga} minutos, notebook descarregou")
                self.__bateria.setCarga(0)
                self.__ligado = False
            else:
                print(f"Usando por {tempo} minutos")
                self.__bateria.setCarga(carga - tempo)
        
        else:
            potencia = self.__carregador.getPotencia()
            nova_carga = carga - tempo + tempo * potencia
            self.__bateria.setCarga(nova_carga)
            print("Notebook utilizado com sucesso")

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria:
            print("bateria removida")
        b = self.__bateria
        self.__bateria = None
        return b

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador

    def rmCarregador(self):
        if self.__carregador:
            print("carregador removido")
        c = self.__carregador
        self.__carregador = None
        return c



notebook = Notebook() # criando notebook
notebook.mostrar()    # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado
notebook.ligar()      # msg: não foi possível ligar
notebook.usar(10)     # msg: notebook desligado

bateria = Bateria(50) # criando bateria que suporta 50 minutos e começa carregada
bateria.mostrar()     # (50/50)
notebook.setBateria(bateria) # coloca a bateria no notebook

notebook.mostrar() # msg: Status: Desligado, Bateria: (50/50), Carregador: Desconectado
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: (50/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 30 minutos
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 20 minutos, notebook descarregou
notebook.mostrar() # msg: Status: Desligado, Bateria: (0/50), Carregador: Desconectado

bateria = notebook.rmBateria() # msg: bateria removida
bateria.mostrar()  # (0/50)
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado

carregador = Carregador(2) # criando carregador com 2 de potencia
carregador.mostrar() # (Potência 2)

notebook.setCarregador(carregador) # adicionando carregador no notebook
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: (Potência 2)
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: Nenhuma, Carregador: (Potência 2)

notebook.setBateria(bateria)
notebook.mostrar() # msg: Status: Ligado, Bateria: (0/50), Carregador: (Potência 2)
notebook.usar(10)  # msg: Notebook utilizado com sucesso
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: (Potência 2)