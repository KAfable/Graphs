"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """Add a vertex to the graph."""
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """Add a directed edge to the graph."""
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("Value does not exist")

    def get_neighbors(self, vertex_id):
        """Get all neighbors (edges) of a vertex."""
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("Value does not exist")

    def bft(self, starting_vertex):
        """ Print each vertex in breadth-first order beginning from starting_vertex."""
        # Create a queue
        queue = Queue()

        # Enqueue the starting vertex
        queue.enqueue(starting_vertex)

        # Create a set to store visited vertices
        visited = set()

        # While the queue is not empty
        while queue.size() > 0:
            # Dequeue to travel towards break case
            vertex = queue.dequeue()
            # if it hasn't been visited
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # enqueue all of its neighbors
                neighbors = self.get_neighbors(vertex)
                for vert in neighbors:
                    queue.enqueue(vert)
        print(visited)

    def dft(self, starting_vertex):
        """ Print each vertex in depth-first order beginning from starting_vertex."""
        # Create a stack
        stack = Stack()

        # Push the starting vertex
        stack.push(starting_vertex)

        # Create a set to store visited vertices
        visited = set()

        # While the stack is not empty
        while stack.size() > 0:
            # Dequeue
            current = stack.pop()
            # if it hasn't been visited
            if current not in visited:
                # Mark it as visited
                visited.add(current)
                # enqueue all of its neighbors
                neighbors = self.get_neighbors(current)
                for vert in neighbors:
                    stack.push(vert)
        print(visited)

    def dft_recursive(self, starting_vertex, visited=None):
        """ Print each vertex in depth-first order beginning from starting_vertex.
        This should be done using recursion. """
        if visited is None:
            visited = set()

        # check if that node has been visited already?
        if starting_vertex not in visited:
            # print and add to visited
            # print(starting_vertex)
            visited.add(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            # call dft on each neighbor below it
            for vert in neighbors:
                self.dft_recursive(vert, visited)
        else:
            print(visited)

    def dft_recursive2(self, starting_vertex):
        visited = set()

        def driver(visited, start):
            if start not in visited:
                visited.add(start)
                neighbors = self.get_neighbors(start)
                for vert in neighbors:
                    driver(visited, vert)
        driver(visited, starting_vertex)
        print(visited)

    def bfs(self, starting_vertex, destination_vertex):
        """ Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order. """
        # Create a queue
        queue = Queue()
        # Enqueue A PATH TO the starting vertex
        queue.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()

        # While the queue is not empty
        while queue.size() > 0:
            # Dequeue the first PATH
            path = queue.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            vertex = path[-1]
            # If it hasn't been visited...
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # CHECK IF IT'S THE TARGET
                if vertex == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                else:
                    # Enqueue A PATH TO all it's neighbors
                    for neighbor in self.get_neighbors(vertex):
                        # MAKE A COPY OF THE PATH AND ENQUEUE THE COPY
                        queue.enqueue([*path, neighbor])
        return visited

    def dfs(self, starting_vertex, destination_vertex):
        """Return a list containing a path from starting_vertex to destination_vertex in
            depth-first order. """
        # Create a queue
        s = Stack()
        # Enqueue A PATH TO the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()

        # While the queue is not empty
        while s.size() > 0:
            # Dequeue the first PATH
            path = s.pop()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            vertex = path[-1]
            # If it hasn't been visited...
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # CHECK IF IT'S THE TARGET
                if vertex == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                else:
                    # Enqueue A PATH TO all it's neighbors
                    for neighbor in self.get_neighbors(vertex):
                        # MAKE A COPY OF THE PATH AND ENQUEUE THE COPY
                        s.push([*path, neighbor])
        return visited

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """ Return a list containing a path from starting_vertex to destination_vertex in
        depth-first order. This should be done using recursion. """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path

    def dfs_recursive_b(self, starting_vertex, destination_vertex, visited=None):
        """ Return a list containing a path from starting_vertex to destination_vertex in
        depth-first order. This should be done using recursion. """
        # add visited and path, since those need to be passed in
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            if starting_vertex == destination_vertex:
                return [starting_vertex]
            for vertex in self.vertices[starting_vertex]:
                vertices = self.dfs_recursive(
                    vertex, destination_vertex, visited)
                if destination_vertex in vertices:
                    return [starting_vertex, *vertices]
        return []


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT')
    graph.dft(1)
    print('DFT - Recursive')
    graph.dft_recursive(1)
    print('DFT - Recursive 2')
    graph.dft_recursive2(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(f'BFS Start')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(f'DFS Start')
    print(graph.dfs(1, 6))
    print(f'DFS Recursive Start')
    print(graph.dfs_recursive(1, 6))
    print(f'DFS Recursive B Start')
    print(graph.dfs_recursive_b(1, 6))
