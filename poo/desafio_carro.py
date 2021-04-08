class Carro:
    def __init__(self, velMax=5):
        self.velMax = velMax
        self.velAtual = 0

    def acelerar(self, delta=5):
        nova = self.velAtual + delta
        self.velAtual = nova if nova <= self.velMax else self.velMax

        return self.velAtual

    def frear(self, delta=5):
        nova = self.velAtual - delta
        self.velAtual = nova if nova >= 0 else 0

        return self.velAtual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
