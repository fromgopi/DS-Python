from src.graphs.BFS import BFS
from src.graphs.Graph import Graph


class BSFDemo:
    if __name__ == '__main__':
        g = {'Frankfurt': {'Mannheim': 85, 'Wurzburg': 217, 'Kassel': 173},
             'Mannheim': {'Frankfurt': 85, 'Karlsruhe': 80},
             'Karlsruhe': {'Augsburg': 250, 'Mannheim': 80},
             'Augsburg': {'Karlsruhe': 250, 'Munchen': 84},
             'Wurzburg': {'Erfurt': 186, 'Numberg': 103, 'Frankfurt': 217},
             'Erfurt': {'Wurzburg': 186},
             'Numberg': {'Wurzburg': 103, 'Stuttgart': 183, 'Munchen': 167},
             'Munchen': {'Numberg': 167, 'Augsburg': 84, 'Kassel': 502},
             'Kassel': {'Frankfurt': 173, 'Munchen': 502},
             'Stuttgart': {'Numberg': 183}
             }
        graph = Graph(g)

        bfs = BFS.min_num_edges_between_nodes(graph,'Frankfurt')
        print(bfs)
