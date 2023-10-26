from src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.ass_prioritarios = qtdPrioritarios
        self.passageiro_n = []
        self.passageiro_p = []

    def getNumeroAssentosPrioritarios(self):
        return self.ass_prioritarios

    def getNumeroAssentosNormais(self):
        return self.capacidade-self.ass_prioritarios

    def getPassageiroAssentoNormal(self, lugar):
        if len(self.passageiro_n) > lugar:
            return self.passageiro_n[lugar]
        else:
            return None

    def getPassageiroAssentoPrioritario(self, lugar):
        if self.passageiro_p[lugar] == '=':
            return None
        else:
            return self.passageiro_p[lugar]

    def getVagas(self):
        return self.capacidade - len(self.passageiro_p) - len(self.passageiro_n)

    def subir(self, passageiro: Passageiro):
        if self.getVagas() > 0:
            if passageiro.ePrioridade():
                if len(self.passageiro_p) < self.ass_prioritarios:
                    self.passageiro_p.append(passageiro)
                    return True
                else:
                    self.passageiro_n.append(passageiro)
                    return True

            elif not passageiro.ePrioridade():
                if len(self.passageiro_n) < self.getNumeroAssentosNormais():
                    self.passageiro_n.append(passageiro)
                    return True
                else:
                    self.passageiro_p.append(passageiro)
                    return True
        else:
            return False

    def descer(self, nome):
        if self.passageiro_p or self.passageiro_n:
            if self.passageiro_n:
                for passageiros in self.passageiro_n:
                    if passageiros.getNome() == nome:
                        self.passageiro_n.remove(passageiros)
                        return True
            elif self.passageiro_p:
                for passageiros in self.passageiro_p:
                    if passageiros.getNome() == nome:
                        self.passageiro_p.remove(passageiros)
                        return True
            return False
        return False

    def toString(self):
        a = []
        cont1 = 0
        cont2 = 0
        for lugar in self.passageiro_p:
            a.append(f'@{lugar.getNome()}')
            cont1 += 1
        for s in range(self.ass_prioritarios - cont1):
            a.append('@')
        for lugar in self.passageiro_n:
            a.append(f'={lugar.getNome()}')
            cont2 += 1
        for s in range(self.getNumeroAssentosNormais() - cont2):
            a.append('=')
        a.append('')
        b = str(a)
        b = b.replace("'", "")
        b = b.replace(",", "")
        return b
