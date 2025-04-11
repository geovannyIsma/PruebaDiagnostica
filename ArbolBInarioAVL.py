class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1  # Altura inicial del nodo

class ArbolBinarioAVL:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz)

    def insertar(self, valor):
        self.raiz = self._insertar_en(self.raiz, valor)

    def _insertar_en(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar_en(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar_en(nodo.derecha, valor)

        # Actualizar la altura del nodo actual
        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda), self._obtener_altura(nodo.derecha))

        # Balancear el nodo
        return self._balancear(nodo)

    def _obtener_altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _obtener_factor_balance(self, nodo):
        if nodo is None:
            return 0
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha)

    def _rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        # Rotación
        x.derecha = y
        y.izquierda = T2

        # Actualizar alturas
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))
        x.altura = 1 + max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha))

        return x

    def _rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        # Rotación
        y.izquierda = x
        x.derecha = T2

        # Actualizar alturas
        x.altura = 1 + max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))

        return y

    def _balancear(self, nodo):
        balance = self._obtener_factor_balance(nodo)

        if balance > 1 and self._obtener_factor_balance(nodo.izquierda) >= 0:
            return self._rotacion_derecha(nodo)

        if balance > 1 and self._obtener_factor_balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)

        if balance < -1 and self._obtener_factor_balance(nodo.derecha) <= 0:
            return self._rotacion_izquierda(nodo)

        if balance < -1 and self._obtener_factor_balance(nodo.derecha) > 0:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)

        return nodo

    def recorrido_inorden(self):
        valores = []
        self._recorrido_inorden(self.raiz, valores)
        return valores

    def _recorrido_inorden(self, nodo, valores):
        if nodo is not None:
            self._recorrido_inorden(nodo.izquierda, valores)
            valores.append(nodo.valor)
            self._recorrido_inorden(nodo.derecha, valores)

    def imprimir_arbol(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        if nodo.derecha is not None:
            self.imprimir_arbol(nodo.derecha, nivel + 1)
        print(' ' * 4 * nivel + str(nodo.valor))
        if nodo.izquierda is not None:
            self.imprimir_arbol(nodo.izquierda, nivel + 1)
