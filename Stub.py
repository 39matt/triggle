class Stub:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def nova_vrednost(self, cor: tuple):
        self.x = cor[0]
        self.y = cor[1]
        return