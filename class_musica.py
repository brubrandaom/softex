class Musica:
    def __init__ (self, genero, titulo) -> None:
        self.__genero = genero
        self.__titulo = titulo
    def get_genero(self) -> str:
        return self.__genero
    def set_genero(self, novo_genero) -> None:
        self.__genero = novo_genero
    def get_titulo(self) -> str:
        return self.__titulo
    def set_titulo(self, novo_titulo) -> None:
        self.__titulo = novo_titulo

musica1 = Musica('Rock', 'Boys dont cry')

print(f'Genero inicial: {musica1.get_genero()}')
musica1.set_genero('Indie')
print(f'Genero alterado: {musica1.get_genero()}')
print(f'Titulo inicial: {musica1.get_titulo()}')
musica1.set_titulo('Ripples')
print(f'Titulo alterado: {musica1.get_titulo()}')


