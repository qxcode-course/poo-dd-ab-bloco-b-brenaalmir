class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def getNome(self) -> str:
        return self.__nome

    def getIdade(self) -> int:
        return self.__idade

    def __str__(self) -> str:
        return f"{self.__nome}:{self.__idade}"


class Motoca:
    def __init__(self, potencia: int = 1):
        self.potencia = potencia
        self.time = 0
        self.pessoa: Pessoa | None = None

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.pessoa = pessoa
        return True

    def remover(self) -> Pessoa | None: 
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return None
        aux = self.pessoa
        self.pessoa = None
        return aux

    def buyTime(self, minutos: int):
        self.time += minutos

    def drive(self, minutos: int):
        if self.time <= 0:
            print("fail: buy time first")
            return
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return
        if self.pessoa.getIdade() > 10:
            print("fail: too old to drive")
            return

        if minutos >= self.time:
            print(f"fail: time finished after {self.time} minutes")
            self.time = 0 
        else:
            self.time -= minutos

    def honk(self):
        print(f"P{'e' * self.potencia}m")

    def __str__(self):
        if self.pessoa is None:
            pessoa_str = "(empty)"
        else:
            pessoa_str = f"({self.pessoa})"
        return f"power:{self.potencia}, time:{self.time}, person:{pessoa_str}"

def main():
    moto = Motoca()
    while True:
        line = input().strip()
        if not line:
            continue

        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(moto)

        elif args[0] == "init":
            potencia = int(args[1]) if len(args) > 1 else 1
            moto = Motoca(potencia)

        elif args[0] == "enter":
            if len(args) >= 3:
                nome = args[1]
                idade = int(args[2])
                pessoa = Pessoa(nome, idade)
                moto.inserir(pessoa)

        elif args[0] == "leave":
            pessoa = moto.remover()
            if pessoa:
                print(pessoa)

        elif args[0] == "buy":
            if len(args) > 1:
                minutos = int(args[1])
                moto.buyTime(minutos)

        elif args[0] == "drive":
            if len(args) > 1:
                minutos = int(args[1])
                moto.drive(minutos)

        elif args[0] == "honk":
            moto.honk()

        else:
            print("fail: invalid command")

if __name__ == "__main__":
    main()