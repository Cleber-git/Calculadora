class carro:
    def __init__(self, marca, ano, dono):
        self.marca = marca
        self.ano =  ano
        self.dono = ano
        self.velocidade = 0
    
    def ligar(self):
        self.velocidade = 10
        from time import sleep
        print('Automóvel dando partida...')
        sleep(1.5)
        print(f'Carro em movimento, {self.velocidade}km/h')

    def frear(self):
        from time import sleep
        print('Carro freando...')
        sleep(1.5)
        print(f'A velocidade atual do carro é: {self.velocidade}km/h')
    
    def show(self):
        print(f'O carro está em {self.velocidade}km/h')

    def acelerar(self, veloz):
        if veloz >= 0:
            self.velocidade += veloz 


cleber = carro('fiat', 2002, 'Cleber Neves')
arthur = carro('creta', 2022, 'Arthur Neves')

cleber.ligar()
cleber.acelerar(30)
cleber.show()
