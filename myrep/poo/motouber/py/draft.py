class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self) -> int:
        return self.__nome

    def getDinheiro(self) -> int:
        return self.__dinheiro

    def setDinheiro(self, valor: int):
        self.__dinheiro = valor

    def __str__(self) -> str:
        return f"{self.__nome}:{self.__dinheiro}"


class Moto:
    def __init__(self):
        self.__custo = 0 
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def setMotorista(self, nome: str, dinheiro: int):
        self.__motorista = Pessoa(nome, dinheiro)

    def setPassageiro(self, nome: str, dinheiro: int):
        if self.__motorista is None:
            print("fail: no driver in the motorcycle")
            return
        self.__passageiro = Pessoa(nome, dinheiro)

    def dirigir(self, km: int):
        if self.__motorista is None or self.__passageiro is None:
            return
        self.__custo += km

    def deixarPassageiro(self):
        if self.__passageiro is None:
            print("fail: no passenger to leave")
            return
        custo = self.__custo
        dinheiro_pass = self.__passageiro.getDinheiro()
        dinheiro_motorista = self.__motorista.getDinheiro()

        if dinheiro_pass < custo:
            print("fail: Passenger does not have enough money")
            self.__motorista.setDinheiro(dinheiro_motorista + custo)
            self.__passageiro.setDinheiro(0)
            print(f"{self.__passageiro.getNome()}:0 left")

        else:
            self.__passageiro.setDinheiro(dinheiro_pass - custo)
            self.__motorista.setDinheiro(dinheiro_motorista + custo)
            print(f"{self.__passageiro.getNome()}:{self.__passageiro.getDinheiro()} left")
        