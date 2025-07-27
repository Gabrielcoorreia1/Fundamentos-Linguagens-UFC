class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
        print(f"Um novo veículo da marca {self.marca}, modelo {self.modelo}, foi criado.")

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O {self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self, decremento):
        if self.velocidade - decremento >= 0:
            self.velocidade -= decremento
        else:
            self.velocidade = 0
        print(f"O {self.modelo} freou para {self.velocidade} km/h.")
    
    def descrever(self):

        return f"Este é um veículo {self.marca} {self.modelo}."


class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def ligar_motor(self):
        print(f"O motor do {self.modelo} foi ligado. Vrum vrum!")

    def descrever(self):
        return f"Este é um carro {self.marca} {self.modelo} com {self.portas} portas."


class Bicicleta(Veiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def pedalar(self):
        print(f"Você começou a pedalar a {self.modelo}. A paisagem é bela!")

    def descrever(self):
        return f"Esta é uma bicicleta {self.marca} {self.modelo}, movida a pedal."


if __name__ == "__main__":
    print("--- Criando e testando um Carro ---")
    meu_fusca = Carro(marca="Volkswagen", modelo="Fusca", portas=2)
    meu_fusca.ligar_motor()
    meu_fusca.acelerar(40)
    print(meu_fusca.descrever())
    
    print("\n" + "-"*35 + "\n")

    print("--- Criando e testando uma Bicicleta ---")
    minha_bike = Bicicleta(marca="Caloi", modelo="Cross")
    minha_bike.pedalar()
    minha_bike.acelerar(10)
    print(minha_bike.descrever())

