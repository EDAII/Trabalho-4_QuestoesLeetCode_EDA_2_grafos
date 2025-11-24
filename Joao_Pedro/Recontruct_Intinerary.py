import collections
import heapq

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # Grafo como lista de adjacência, com min-heap para manter ordem lexicográfica
        grafo = collections.defaultdict(list)
        for origem, destino in tickets:
            heapq.heappush(grafo[origem], destino)

        rota = []

        def dfs(vertice):
            # enquanto houver destinos a partir do vértice atual
            while grafo[vertice]:
                proximo = heapq.heappop(grafo[vertice])
                dfs(proximo)
            rota.append(vertice)

        # começamos sempre em JFK
        dfs("JFK")
        return rota[::-1]  # invertemos pois construímos de trás para frente
