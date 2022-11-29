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

    def randGraph(self, edges):
        S = []
        T = []
        for i in range(self.V):
            S.append(i)
        current_node = random.sample(S, 1).pop()
        S.remove(current_node)
        T.append(current_node)
        while S:
            neighbor_node = random.sample(S, 1).pop()
            if neighbor_node not in T:
                self.addEdge(current_node, neighbor_node, randint(1, 10))
                S.remove(neighbor_node)
                T.append(neighbor_node)
            current_node = neighbor_node

        for i in range(edges):
            is_new_edge = False
            while not is_new_edge:
                is_new_edge = True
                current_node = random.randint(0, self.V - 1)
                neighbor_node = random.randint(0, self.V - 1)
                for edge in self.graph:
                    if (edge[0] == current_node and edge[1] == neighbor_node) or (
                            edge[0] == neighbor_node and edge[1] == current_node):
                        is_new_edge = False
                        break
            self.addEdge(current_node, neighbor_node, randint(1, 10))



if __name__ == '__main__':

    n = 1000
    edges = n - 1
    k = 1

    for i in range(5):
        graph = Graph(n * k)
        graph.randGraph(edges * k - (k - 1))

        begin = time.perf_counter()
        graph.MST()
        end = time.perf_counter()
        print(f"Вычисление заняло {end - begin:0.4f} секунд")
        print('Количество ребер: ', len(graph.graph))
        print('Количество вершин: ', graph.V)
        print('----------------------------------')
        k *= 2

