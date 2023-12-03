class IntJoukko:    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = self.validoi_syöte(kapasiteetti, "Väärä kapasiteetti")
        self.kasvatuskoko = self.validoi_syöte(kasvatuskoko, "Väärä kasvatuskoko")

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def validoi_syöte(self, syöte, virhe_viesti):
        if not isinstance(syöte, int) or syöte < 0:
            raise Exception(str(virhe_viesti))
        return syöte

    def _luo_lista(self, koko):
        return [0] * koko

    def sisaltaa(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                return True
        
        return False

    def lisaa(self, n):
        if not self.sisaltaa(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.lukujono):
                self.lukujono.extend([None]*self.kasvatuskoko)
            
            return True
        return False

    def poista(self, n):
        if n in self.lukujono:
            self.lukujono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, a, b):
        b = a

    def koko(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        lista = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(lista)):
            lista[i] = self.lukujono[i]

        return lista

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_lista = a.to_int_list()
        b_lista = b.to_int_list()

        def _lisaa_lista_lukujonoon(lukujono, lista):
            for i in range(0, len(lista)):
                lukujono.lisaa(lista[i])

        _lisaa_lista_lukujonoon(x, a_lista)
        _lisaa_lista_lukujonoon(x, b_lista)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_lista = a.to_int_list()
        b_lista = b.to_int_list()

        for i in range(0, len(a_lista)):
            for j in range(0, len(b_lista)):
                if a_lista[i] == b_lista[j]:
                    y.lisaa(b_lista[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_lista = a.to_int_list()
        b_lista = b.to_int_list()

        for i in range(0, len(a_lista)):
            if not a_lista[i] in b_lista:
                z.lisaa(a_lista[i])

        return z

    def __str__(self):
        return "{" + ", ".join(str(i) for i in self.lukujono[:self.alkioiden_lkm]) + "}"