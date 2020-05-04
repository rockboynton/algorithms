import copy
from collections import defaultdict

class DiGraph:
    """
    Implements a directed graph.
    
    Vertices can be any hashable object (e.g., number, string, tuple).
    
    The graph is stored using a dictionary.  The vertices are keys.
    The value for each vertex is a set of vertices.  An edge from vertex
    u to vertex v is present in the graph if v in self._edges[u].
    """
    
    def __init__(self):
        self._edges = defaultdict(set)
        
    def add_vertex(self, v):
        """
        Adds the given vertex v. If v is already in the
        graph, it isn't added again.
        """
        self._edges[v]
        
    def add_edge(self, u, v):
        """
        Adds an edge from vertex u to vertex v.  If the edge is
        already in the graph, if it isn't added again.  If u or
        v are not present in the graph, they are added.
        """
        self._edges[v]
        self._edges[u].add(v)
        
    def vertex_exists(self, u):
        """
        Returns true if u is in the graph, false otherwise.
        """
        return u in self._edges
        
    def edge_exists(self, u, v):
        """
        Returns true if there is an edge from u to v in the graph, false otherwise.
        If u or v are not in the graph, false is returned.
        """
        return v in self._edges[u]
    
    def get_outgoing_edges(self, u):
        """
        Returns a collection of edges starting at vertex u.
        """
        return self._edges[u]
    
    def count_vertices(self):
        """
        Counts the number of vertices in the graph
        """
        return len(self._edges)
        
    def count_edges(self):
        """
        Counts the number of edges in the graph
        """
        return sum(map(len, self._edges.values()))

    def edge_set(self):
        """Get a set of all edges in the graph.

        Each edge is represented as a tuple of (start, end)

        Returns:
            set<tuple<vertex, vertex>>: Set of all edges
        """
        edges = set()
        for start_vertex, edge_set in self._edges.items():
            for end_vertex in self._edges[start_vertex]:
                edges.add((start_vertex, end_vertex))

        return edges