import random

def ordenamiento_por_insercion(lista):

    # el for va guardando cada valor en memoria 
    # del siguiente numero en la lista, porque el
    # for se inicializo desde 1
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        # este while esta validando que los numeros sea positivos (mayores a cero)
        # y que (posicion actual - 1) sea mayor quela siguiente y si eso se cumple 
        # se intercamia los valores dejando el menor enla posicion anterior, cabe destacar que se
        # coloca la"posicion actual - 1" ya que los vectores inicializa en 0 y en el for 
        # lo comenzamos en 1
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista

if __name__=='__main__':
    tamana_de_lista = int(input('de que tamaño quieres la lista: '))

    lista = [random.randint(0, 100) for i in range(tamana_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)