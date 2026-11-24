from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class DFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:
        fronteira = [initial]
        visitados = set()
        expandidos = 0
        gerados = 1
        max_fronteira = 1

        while fronteira:
            atual = fronteira.pop()

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
                    fronteira.append(filho)
                    gerados += 1

            max_fronteira = max(max_fronteira, len(fronteira))

        return SearchResult(
            solution=None,
            nodes_expanded=expandidos,
            nodes_generated=gerados,
            max_frontier_size=max_fronteira,
        )