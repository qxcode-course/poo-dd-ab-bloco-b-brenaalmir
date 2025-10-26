class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self) -> int:
        gastos = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6,
        }
        return gastos.get(self.hardness, 1)

    def __str__(self):
        return f"{self.thickness}:{self.hardness}:{self.size}"


class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.tip: Lead | None = None

    def hasGrafite(self) -> bool:
        return self.tip is not None

    def insert(self, lead: Lead):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return
        if lead.thickness != self.thickness:
            print("fail: calibre incompativel")
            return
        self.tip = lead

    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return None
        self.tip = None

    def write(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return

        if self.tip.size <= 10:
            print("fail: tamanho insuficiente")
            return

        gasto = self.tip.usagePerSheet()
        if self.tip.size - gasto < 10:
            print("fail: folha incompleta")
            self.tip.size = 10
        else:
            self.tip.size -= gasto

    def __str__(self):
        if self.tip:
            return f"calibre: {self.thickness:.1f}, grafite: [{self.tip}]"
        return f"calibre: {self.thickness:.1f}, grafite: null"


def main():
    pencil = None
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line == "":
            continue

        print(f"${line}")
        parts = line.split()
        cmd = parts[0]

        if cmd == "end":
            break

        elif cmd == "init":
            calibre = float(parts[1])
            pencil = Pencil(calibre)

        elif cmd == "insert":
            if pencil is None:
                print("fail: lapiseira nao iniciada")
                continue
            calibre = float(parts[1])
            dureza = parts[2]
            tamanho = int(parts[3])
            pencil.insert(Lead(calibre, dureza, tamanho))

        elif cmd == "remove":
            if pencil is None:
                print("fail: lapiseira nao iniciada")
                continue
            pencil.remove()  

        elif cmd == "write":
            if pencil is None:
                print("fail: lapiseira nao iniciada")
                continue
            pencil.write()

        elif cmd == "show":
            print(pencil)


if __name__ == "__main__":
    main()

