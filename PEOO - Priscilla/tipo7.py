# Componentes:
# Kaio Emidio Fernandes Evangelista
# Vinícius Gabriel Palhares do Nascimento

class Poligono:
    def __init__(self, numLados):  
        self.numLados = numLados

    def get_numLados(self):
        return self.numLados

    def set_numLados(self, numLados):
        self.numLados = numLados

    def calcular_perimetro(self):
        peri = 0
        print(f"Para calcular o perímetro é necessário a medida dos {self.numLados} lados.")
        for i in range(self.numLados):  
            lado = float(input(f"Digite a medida do {i + 1}º lado: "))
            peri += lado
        print(f"O perímetro do polígono é: {peri}")

class TestarPoligono:
    def main():
        numLados = int(input("Digite o número de lados do polígono: "))
        poligono = Poligono(numLados)
        poligono.calcular_perimetro()

nl = int(input("Digite o número de lados do polígono: "))
poli = Poligono(nl)
poli.calcular_perimetro()
nl = int(input("Digite o novo número de lados do polígono: "))
poli.set_numLados(nl)
poli.calcular_perimetro()