class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def inserir_elemento_posicao (self, elemento, posicao):
        vetor_inicio = self.__elementos[:posicao] + [None] #1, 2, [None]
        vetor_final = self.__elementos[posicao:] #3
        vetor_inicio[len(vetor_inicio) - 1] = elemento #1, 2, 4
        self.__elementos = vetor_inicio + vetor_final #1, 2, 4 , 3
        self.__posicao += 1


    def inserir_elemento_final(self, elemento):
        if self.__posicao >= len(self.__elementos):
            #[None], [None], [None]
            self.__elementos= self.__elementos + [None]
            # [None], [None], [None], [None]
        #1, 2
        # metodo identifica que a proxima posição é a 2
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]
