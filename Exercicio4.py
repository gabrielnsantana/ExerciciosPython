class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        self.idade += 1
    def engordar(self):
        self.peso += 1
    def emagrecer(self):
        self.peso -= 1
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5

Gabriel = Pessoa(nome = 'Gabriel', idade = 10, peso = 70.0, altura = 1.78)
print(f'Nome: {Gabriel.nome}, Idade: {Gabriel.idade}, Peso: {Gabriel.peso}, Altura: {Gabriel.altura}')
while Gabriel.idade < 80:
    Gabriel.envelhecer()
    Gabriel.engordar()
    Gabriel.emagrecer()
    Gabriel.crescer()
    print(f'Nome: {Gabriel.nome}, Idade: {Gabriel.idade}, Peso: {Gabriel.peso}, Altura: {round(Gabriel.altura,2)}')


