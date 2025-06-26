from typing import List

class MedicoEspecialidadSubject:
    def __init__(self):
        self.observadores: List = []

    def agregar_observador(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminar_observador(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)

    def notificar(self, relacion):
        for observador in self.observadores:
            observador.actualizar(relacion)
