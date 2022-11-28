# в словарях позволяет указывать значение по умолчанию
import math
import random
import time
from random import randint


class Graph:
    def __init__(self, vertices):  # конструктор в который мы будем передавать количество вершин
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):  # функция добавления ребра к узлам графа от вершины u до вершины v
        self.graph.append([u, v, w])

    def find(self, parent, i):  # находит индекс компонента данного узла
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x,
              y):  # метод объединения. два компонента в один учитывая два узла, которые принадлежат их соответствующим компонентам

        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] > rank[yroot]:
            parent[xroot] = yroot
        elif rank[yroot] > rank[xroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def randGraph(self, edges):
        S = []
        T = []
        e = 0
        for i in range(g.V):
            S.append(i)
    
    
        current_node = random.sample(S, 1).pop()
        S.remove(current_node)
        T.append(current_node)
    
        while S:
            neighbor_node = random.sample(S, 1).pop()
    
            if neighbor_node not in T:
                g.addEdge(current_node, neighbor_node, randint(1, 10))
                e += 1
                S.remove(neighbor_node)
                T.append(neighbor_node)
            current_node = neighbor_node
    
        i = 0
        while edges != e:
            g.addEdge(T[i], T[len(T) - 1 - i], randint(1, 10))
            i += 1
            e += 1
    
        print('Количество ребер: ', e)


    def MST(self):  # метод поиска минимального ост.дерева
        parent = []  # связанные компоненты
        rank = []
        cheapest = []  # набор весов, которые за меньший вес соединяют компоненты
        numTrees = self.V  # число связных компонентов
        MSTweight = 0  # вес минимального остова

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest = [-1] * self.V  # отрицательные веса не могут быть

        while numTrees > 1:  # выполняется до тех пор, пока число связных копонент не будет равно 1
            for i in range(len(self.graph)):
                u, v, w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                if set1 != set2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]
                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]

            for node in range(self.V):
                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        MSTweight += w
                        self.union(parent, rank, set1, set2)
                        #print("Дуга %d-%d с весом  %d включена в остов" % (u, v, w))
                        numTrees -= 1
            cheapest = [-1] * self.V
        print("Вес минимального остова равен: ", MSTweight)




if __name__ == '__main__':
    v = 1000
    n = 1
    edges = v - 1 + v / 2
    
    for b in range(1, 6):
    
        g = Graph(v * n)
        g.randGraph(edges)
    
        # for i in range(v):
        #     g.addEdge(T[i], T[v - 1 - i], randint(1, 2))
        #     nodes += 1
    
        # i = 0
        # while nodes * 2 != nodes2:
        #     g2.addEdge(T2[i], T2[(v * 2) - 1 - i], randint(1, 2))
        #     i += 1
        #     nodes2 += 1
    
        print(b, ': ')
        tic = 0
        tic = time.perf_counter()
        g.MST()
        toc = 0
        toc = time.perf_counter()
    
        print(f"Вычисление заняло {toc - tic:0.4f} секунд")
        print('Количество вершин: ', v * n)
    
        tic2 = 0
        n *= 2
        edges *= 2

 

