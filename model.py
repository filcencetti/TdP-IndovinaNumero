import random

class Model(object):
    def __init__(self):
        self._Nmax = 100
        self._Tmax = 6
        self._T = self._Tmax
        self._segreto = None

    def reset(self):
        self._segreto = random.randint(0,self._Nmax)
        self._T = self._Tmax
        print(self._segreto)

        pass

    def play(self,guess):
        """
        Funzione che esegue uno step del gioco
        :param guess: int
        :return: 0 se vinto,
        -1 se il segreto è più piccolo
        1 se il segreto è più grande
        2 se ho perso

        """
        # dsa fuori ci arriva un tentativo e lo
        # confrontiamo con il segreto
        self._T -= 1
        if guess == self._segreto:
            return 0 # ho vinto!!

        if self._T == 0:
            return 2 # ho perso definitivamente

        if guess > self._segreto:
            return -1 # il segreto è più piccolo

        return 1 # il segreto è più grande

if __name__ == " main ":
    m = Model()
    m.reset()
    print(m.play(50))