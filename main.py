# в словарях позволяет указывать значение по умолчанию
import math
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
                        print("Дуга %d-%d с весом  %d включена в остов" % (u, v, w))
                        numTrees -= 1
            cheapest = [-1] * self.V
        print("Вес минимального остова равен: ", MSTweight)


if __name__ == '__main__':
    for n in range(1, 8):
        print(n, ': \n')
        if n == 1:
            nodes = 10
            g = Graph(10)
            print('nodes:', nodes)
        if n == 2:
            nodes = 10
            g = Graph(10)
            print('nodes:', nodes)
        if n == 3:
            nodes = 100
            g = Graph(100)
            print('nodes:', nodes)
        if n == 4:
            nodes = 2*100
            g = Graph(2*100)
            print('nodes:', nodes)
        if n == 5:
            nodes = 300
            g = Graph(300)
            print('nodes:', nodes)
        if n == 6:
            nodes = 500
            g = Graph(500)
            print('nodes:', nodes)
        if n == 7:
            nodes = 1000
            g = Graph(1000)
            print('nodes:', nodes)

        mas = [[0 for i in range(nodes)] for j in range(nodes)]

        for i in range(0, nodes):
            b = True
            for j in range(0, nodes):
                if i == j:
                    mas[j][i] = 0
                    if b and j == nodes - 1:
                        if i == 0:
                            mas[i][nodes - 1] = 1
                        else:
                            mas[j][0] = 1
                else:
                    mas[j][i] = randint(0, 1)
                    if mas[j][i] != 0 and b:
                        b = False
                    if b and j == nodes - 1:
                        k = randint(0, nodes - 1)
                        if i == 0:
                            mas[i][nodes - 1] = 1
                        else:
                            mas[j][0] = 1

        v = 0
        for i in range(0, nodes):
            for j in range(0, nodes):
                if mas[i][j] != 0:
                    v += 1
                    g.addEdge(i, j, mas[i][j])

        tic = 0
        tic = time.perf_counter()
        g.MST()
        toc = 0
        toc = time.perf_counter()
        print(f"Вычисление заняло {toc - tic:0.4f} секунд")
        print('Количество ребер: ', v)
        print('Количество вершин: ', nodes)
        print('---------------------------------------------------')
