def pedirNum():
    i = 0
    lista = []

    while i < 5:
        numero = int(input('Ingrese un numero para añadirlo a la lista: \n'))
        lista.append(numero)
        i += 1

    return lista


def ordendelistaAscendente(input_list):
    listaOrdenada = []
    copiaLista = input_list.copy()
    while copiaLista:
        minimo = min(copiaLista)  
        listaOrdenada.append(minimo)
        copiaLista.remove(minimo)
    return listaOrdenada


def ordendelistaDescendente(input_list):
    listaOrdenada = []
    copiaLista = input_list.copy()
    while copiaLista:
        maximo = max(copiaLista)  
        listaOrdenada.append(maximo)
        copiaLista.remove(maximo)
    return listaOrdenada


listaInicial = pedirNum()
listaDescendente = ordendelistaDescendente(listaInicial)
listaAscendente = ordendelistaAscendente(listaInicial)

print(f'')
print(f'''
      {'*' * 80}
      La lista incial es: {listaInicial}
      La lista ascendente es: {listaAscendente}
      La lista descendente queda: {listaDescendente}
      {'*' * 80}
      ''')