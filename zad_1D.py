lista=list(range(1, 11))
def co_drugi_element(lista):
    for i in range(1, len(lista), 2):
        print(lista[i])
co_drugi_element(lista)
