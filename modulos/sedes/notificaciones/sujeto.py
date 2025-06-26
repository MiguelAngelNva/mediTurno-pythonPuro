class SedeSubject:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar(self, sede):
        for observador in self.observadores:
            observador.actualizar(sede)