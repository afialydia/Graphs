from util import Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError('ERROR: No such Vertex exist.')


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for pair in ancestors: #< instead of for pair do for parent , child for more readability of code
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        g.add_edge(pair[1],pair[0])
    
    q = Queue()

    q.enqueue([starting_node]) # <-   enqueue a path to starting node

    visited = set() #<-  creating a set to store visited

    earliest_ancestor = -1 #<-  no parents set to -1 initializing parents

    while q.size() > 0:
        path = q.dequeue()#<-  gets the first path in the queue
        v = path[-1]#<-  gets last node in the path


        if v not in visited:#<- check if visited and if not do the following
            visited.add(v)

            if((v < earliest_ancestor) or (len(path)>1)): #<-checks if path(v) is less than parent meaning if there was no path it would be the parent or length is longer than 1
                earliest_ancestor = v #sets ancestor

            for neighbor in g.get_neighbors(v): #  copy's path and enqueues to all its neighbors

                copy = path.copy()
                copy.append(neighbor)
                q.enqueue(copy)
                
    return earliest_ancestor
            

