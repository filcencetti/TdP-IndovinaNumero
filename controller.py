from view import View
from model import Model
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNMax(self):
        return self._model._NMax

    def getTMax(self):
        return self._model._TMax

    def reset(self, e):
        self._model.reset()
        self._view._txtOutT.value = self._model._T
        self._view._lv.controls.clear()
        self._view._btnPlay.disabled = False
        self._view._txtIn.disabled = False
        self._view._lv.controls.append(
            ft.Text("Indovina a quale numero sto pensando???"))
        self._view.update()

    def play(self,e):
        tentivoStr = self._view._txtIn.value
        self._view._txtIn.value = ""
        self._view._txtOutT.value = self._model._T - 1
        if tentivoStr == "":
            self._view._lv.controls.append(ft.Text("Attenzione! Inserisci un valore numerico da testare",
                                                   color="red"))
            self._view.update()
            return
        try:
            tentativoInt = int(tentivoStr)
        except ValueError:
            self._view._lv.controls.append(
                ft.Text("Attenzione! il valore inserito non è un intero",
            color="red"))
            return

        res = self._model.play(tentativoInt)

        if res == 0: # ho vinto
            self._view._lv.controls.append(
                ft.Text(f"Fantastico! Hai vinto! Il segreto era {tentativoInt}",
                        color = "green"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return

        elif res == 2: # ho finito tutte le vite
            self._view._lv.controls.append(
            ft.Text(f"Mi dispiace, ha finito le vite. "
                    f"Il segreto era {self._model._segreto}",
                    color="green"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return

        elif res == -1: # il mio segreto è più piccolo
            self._view._lv.controls.append(
                ft.Text(f"Il segreto è più piccolo di {tentativoInt}.")
            )
            self._view.update()
        else: # il segreto è più grande
            self._view._lv.controls.append(
                ft.Text(f"Il segreto è più grande di {tentativoInt}")
                )
            self._view.update()


    # con i setter nessuno può modificare NMax e TMax
    @property
    def NMax(self):
        return self._NMax

    @property
    def TMax(self):
        return self._TMax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto
