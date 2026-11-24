import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        distancia = 0
        for i, peca in enumerate(state.tiles):
            if peca != 0:
                j = GOAL_STATE.index(peca)
                distancia += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
        return distancia

    def search(self, initial: State) -> SearchResult:
        contador = 0
        fronteira = [(self.heuristic(initial), contador, initial)]
        visitados = set()
        expandidos = 0
        gerados = 1
        max_fronteira = 1

        while fronteira:
            _, _, atual = heapq.heappop(fronteira)

            if atual in visitados:
                continue
            visitados.add(atual)

            if atual.is_goal:
                return SearchResult(
                    solution=atual,
                    nodes_expanded=expandidos,
                    nodes_generated=gerados,
                    max_frontier_size=max_fronteira,
                    depth=atual.cost,
                )

            expandidos += 1
            for filho in atual.neighbors():
                if filho not in visitados:
                    contador += 1
                    f = filho.cost + self.heuristic(filho)
                    heapq.heappush(fronteira, (f, contador, filho))
                    gerados += 1

            max_fronteira = max(max_fronteira, len(fronteira))

        return SearchResult(
            solution=None,
            nodes_expanded=expandidos,
            nodes_generated=gerados,
            max_frontier_size=max_fronteira,
        )