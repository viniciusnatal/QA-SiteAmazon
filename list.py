class Iphone(object):
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    def __repr__(self):
        return "Nome do iPhone: %s,\nValor do iPhone:%s" % (self.__nome, self.__valor)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_valor(self):
        return self.__valor

    def set_nome(self, valor):
        self.__valor = valor