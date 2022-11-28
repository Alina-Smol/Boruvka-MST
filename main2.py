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


def randGraph(v, g):
    S = []
    T = []
    nodes = []
    for i in range(v):
        S.append(i)
        nodes.append(i)

    current_node = random.sample(S, 1).pop()
    S.remove(current_node)
    T.append(current_node)
    v = 0
    while S:
        neighbor_node = random.sample(nodes, 1).pop()

        if neighbor_node not in T:
            g.addEdge(current_node, neighbor_node, randint(1, 2))
            v += 1
            S.remove(neighbor_node)
            T.append(neighbor_node)
        current_node = neighbor_node
    return T, g, v

if __name__ == '__main__':
    for b in range(1, 6):
        if b == 1:
            g = Graph(10)
            v = 10
        if b == 2:
            g = Graph(50)
            v = 50
        if b == 3:
            g = Graph(60)
            v = 60
        if b == 4:
            g = Graph(150)
            v = 150
        if b == 5:
            g = Graph(500)
            v = 500

        g2 = Graph(v * 2)

        T, g, nodes = randGraph(v, g)
        T2, g2, nodes2 = randGraph(v * 2, g2)
        for i in range(v):
            g.addEdge(T[i], T[v - 1 - i], randint(1, 2))
            nodes += 1

        i = 0
        while nodes * 2 != nodes2:
            g2.addEdge(T2[i], T2[(v * 2) - 1 - i], randint(1, 2))
            i += 1
            nodes2 += 1

        tic = 0
        tic = time.perf_counter()
        g.MST()
        toc = 0
        toc = time.perf_counter()

        tic2 = 0
        tic2 = time.perf_counter()
        g2.MST()
        toc2 = 0
        toc2 = time.perf_counter()
        print('b: ')
        print(f"Вычисление заняло {toc - tic:0.4f} секунд")
        print('Количество ребер: ', v)
        print('Количество вершин: ', nodes)

        print(f"Вычисление заняло {toc2 - tic2:0.4f} секунд")
        print('Количество ребер: ', v * 2)
        print('Количество вершин: ', nodes2)
        print('---------------------------------------------------')




