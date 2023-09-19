
class Datas:

    def __init__(self, dia, mes, ano):
        print("Contruindo uma data... {}".format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("Hoje é {}/{}/{}".format(self.dia, self.mes, self.ano))