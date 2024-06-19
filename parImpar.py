lista_num =[2,3,7,12,16,27]
listaPar = []
listaImpar = []
def num_parImpar():
    for i in range (len (lista_num)):
        if i % 2 == 0:
            listaPar.append(i)
        else:
            listaImpar.append(i)
            
    print(f"Numeros Pares:", listaPar)
    print(f"Numeros Impares:", listaImpar)

num_parImpar()