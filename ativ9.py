import csv
import math
class grafo:
   def __init__(self, matriz,ids):
    self.matriz = matriz
    self.ids = ids


def lerCSV(caminho):
    matriz = []
    with open(caminho) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        ids = csv_reader.__next__()
        ids.pop(0)
        for row in csv_reader:
            aux = []
            for a in row[1:]:
                if(a=="i"):
                    aux.append(math.inf)
                else:
                    aux.append(int(a))
            matriz = matriz + [aux]
    return grafo(matriz, ids)


def dijkstra(s, grafo):
    d = []*len(grafo.matriz)
    v = [False]*len(grafo.matriz)
    p = [-1]*len(grafo.matriz)
    for i in range(len(grafo.matriz)):
        if(i == s):
            d.append(0)
        else:
            d.append(math.inf)
    while(v.count(False)):
        menor = math.inf
        for i in range(len(grafo.matriz)):
            if(d[i]<menor and v[i] == False):
                k = i
                menor = d[i]
        if(menor == math.inf):
            break
        v[k] = True
        for j in range(len(grafo.matriz)):
                if(grafo.matriz[k][j]!=math.inf and v[j] == False):
                    sum = d[k] + grafo.matriz[k][j]
                    if(sum<d[j]):
                        d[j] = sum
                        p[j] = k
    printDistances(d, p, s, grafo)

def printDistances(distance, previous, s, grafo):
    print("**********************************************")
    print("Distancias a partir do vertice ", grafo.ids[s], end="\n\n")
    for i in range (len(distance)):
        route = []
        aux = previous[i]
        while(aux != -1):
            route.append(aux)
            aux = previous[aux]
        route.reverse()
        print("Vertice ", grafo.ids[i]," = ", distance[i])
        for r in route:
            print(grafo.ids[r], " => ", end="")
        print(grafo.ids[i])
        print("-----------------------------------------------")




                
#9.1
#grafo1 = lerCSV("Ativ 9\Atividade 9 - Grafos - 9.1.csv")
#dijkstra(4, grafo1)
#9.2
#grafo2 = lerCSV("Ativ 9\Atividade 9 - Grafos - 9.2.csv")
#dijkstra(1, grafo2)
#9.3
grafo3 = lerCSV("Ativ 9\Atividade 9 - Grafos - 9.3.csv")
dijkstra(5, grafo3)

