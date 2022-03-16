import pyautogui as pag

coordenadas = list()  # Cria uma lista

arquivo = open('coordenadas.txt', 'w')  # "Abre"/Cria o arquivo cooordenadas
arquivo.close()  # "Fecha" o arquivo

for i in range(3):
    pag.sleep(3)  # "Adormece" o código por 3 segundos para que haja tempo para posicionar o mouse onde quer saber a coordenada
    arquivo = open('coordenadas.txt', 'r')  # Abre o arquivo (leitura)
    coordenadas = arquivo.readlines()  # Retorna cada linha do arquivo como uma lista
    coordenadas.append(str(pag.position()))  # Adiciona a coordenada a lista "coordenadas"
    pag.sleep(3)  # Adormece o código por 3 segundos
    pag.alert("{}° coordenada salva!".format(i+1))  # Informa através de uma notificação que a coordenada foi salva na lista

    arquivo = open('coordenadas.txt', 'w')  # Abre novamente o arquivo (escrita)
    arquivo.writelines(coordenadas)    # Escreve o conteúdo da lista "coordenadas" no arquivo "coordenadas.txt".

arquivo.close()   # "Fecha" o arquivo
