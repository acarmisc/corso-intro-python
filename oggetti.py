from datetime import datetime


class Marca:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "<Marca %s>" % self.nome


class Automobile:

    def __init__(self, nome, anno, marca, consumo):
        anno = int(anno)
        self.nome = nome
        self.anno = anno
        self.carburante = 0
        self.marca = Marca(marca)
        self.eta = datetime.now().year - anno
        self.consumo = int(consumo)

    def __repr__(self):
        return "<Automobile %s>" % self.nome

    def rifornisci(self, litri):
        self.carburante += litri
    
    def consuma(self):
        self.carburante -= self.consumo

if __name__ == '__main__':
    import time
    nome = raw_input("nome della macchina: ")
    anno = raw_input("anno di fabbricazione (aaaa): ")
    marca = raw_input("marca: ")
    consumo = raw_input("consumo: ")
    mia_auto = Automobile(nome, anno, marca, consumo)
    print "Quindi possiedi una %s %s" % (mia_auto.marca.nome, mia_auto.nome)

    print "Carburante: %s litri" % mia_auto.carburante
    
    mia_auto.rifornisci(30)
    print "Carburante: %s litri" % mia_auto.carburante

    secondi = 20
    while secondi > 0:
        mia_auto.consuma(10)
        if mia_auto.carburante <= 0:
            print "Finita la benza!"
            break
     
        secondi -= 1
        time.sleep(1)
        print "Carburante: %s litri" % mia_auto.carburante
    
