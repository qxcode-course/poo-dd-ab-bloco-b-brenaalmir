class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getCapacidade(self):
        return self.__capacidade

    def getCarga(self):
        return self.__carga

    def setCarga(self, valor: int):
        self.__carga = max(0, min(valor, self.__capacidade))

    def usar(self, tempo: int):
        if tempo > self.__carga:
            usado = self.__carga
            self.__carga = 0
            return usado, True
        else:
            self.__carga -= tempo
            return tempo, False

    def carregar(self, quantidade: int):
        self.setCarga(self.__carga + quantidade)

    def __str__(self):
        return f"{self.__carga}/{self.__capacidade}"


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia

    def __str__(self):
        return f"{self.__potencia}W"


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None
        self.__tempo_uso = 0

    def show(self):
        msg = "Notebook: "
        if not self.__ligado:
            msg += "desligado"
        else:
            msg += f"ligado por {self.__tempo_uso} min"

        if self.__bateria and self.__carregador:
            msg += f", Carregador {self.__carregador}, Bateria {self.__bateria}"
        elif self.__bateria:
            msg += f", Bateria {self.__bateria}"
        elif self.__carregador:
            msg += f", Carregador {self.__carregador}"

        print(msg)

    def turn_on(self):
        if (self.__bateria and self.__bateria.getCarga() > 0) or self.__carregador:
            self.__ligado = True
        else:
            print("fail: não foi possível ligar")

    def turn_off(self):
        self.__ligado = False

    def set_battery(self, capacidade: int):
        if self.__bateria:
            print("fail: bateria já conectada")
            return
        self.__bateria = Bateria(capacidade)

    def rm_battery(self):
        if not self.__bateria:
            print("fail: Sem bateria")
            return
        print(f"Removido {self.__bateria}")
        self.__bateria = None
        if not self.__carregador:
            self.__ligado = False

    def set_charger(self, potencia: int):
        if self.__carregador:
            print("fail: carregador já conectado")
            return
        self.__carregador = Carregador(potencia)

    def rm_charger(self):
        if not self.__carregador:
            print("fail: Sem carregador")
            return
        print(f"Removido {self.__carregador}")
        self.__carregador = None
        if not (self.__bateria and self.__bateria.getCarga() > 0):
            self.__ligado = False

    def use(self, tempo: int):
        if not self.__ligado:
            print("fail: desligado")
            return

        if self.__bateria and not self.__carregador:
            usado, descarregou = self.__bateria.usar(tempo)
            self.__tempo_uso += usado
            if descarregou:
                print("fail: descarregou")
                self.__ligado = False
            return

        if self.__bateria and self.__carregador:
            self.__tempo_uso += tempo
            ganho = self.__carregador.getPotencia() * tempo - tempo
            self.__bateria.carregar(ganho)
            return

        if not self.__bateria and self.__carregador:
            self.__tempo_uso += tempo
            return


def main():
    nb = Notebook()
    while True:
        line = input().strip()
        if not line:
            continue
        print(f"${line}")
        args = line.split()
        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "show":
            nb.show()
        elif cmd == "turn_on":
            nb.turn_on()
        elif  cmd == "turn_off":
            nb.turn_off()
        elif cmd == "set_battery":
            nb.set_battery(int(args[1]))
        elif cmd == "rm_battery":
            nb.rm_battery()
        elif cmd == "set_charger":
            nb.set_charger(int(args[1]))
        elif cmd == "rm_charger":
            nb.rm_charger()
        elif cmd == "use":
            nb.use(int(args[1]))
        else:
            print("fail: comando inválido")

if __name__ == "__main__":
    main()