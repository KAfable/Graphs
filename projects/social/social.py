import random
from util import Stack, Queue


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """ Creates a bi-directional friendship """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """ Create a new user with a sequential integer ID """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """ Takes a number of users and an average number of friendships as arguments
        Creates that number of users and a randomly distributed friendships between those users. The number of users must be greater than the average number of friendships. """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+ 1}")

        # Create friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)

        # create n friendships where n = avg_friendships * num_users // 2
        # divided over 2 because there are two friendships per connection (both ways)
        for i in range(num_users * avg_friendships // 2):
            (friend, other_friend) = possible_friendships[i]
            self.add_friendship(friend, other_friend)

    def get_all_social_paths(self, user_id):
        """ Takes a user's user_id as an argument. Returns a dictionary containing every user in that user's extended network with the shortest friendship path between them. The key is the friend's ID and the value is the path."""

        # use BFT to get to each person in the connected component
        # use BFS to get to the shortest path to each component

        def get_shortest_path(origin, destination):
            """Helper function that gets the shortest path to a destination node via BFS"""
            q2 = Queue()
            q2.enqueue([origin])
            visited = set()

            while q.size() > 0:
                path = q2.dequeue()
                vertex = path[-1]
                if vertex not in visited:
                    visited.add(vertex)
                    if vertex == destination:
                        return path
                    else:
                        for neighbor in self.friendships[vertex]:
                            q2.enqueue([*path, neighbor])
            return (origin, destination)

        q = Queue()
        q.enqueue(self.friendships[user_id])
        visited = {}  # Note that this is a dictionary, not a set
        while q.size() > 0:
            friendships = q.dequeue()
            # print(f'current friendships: {friendships}')
            # for each friend in friendships
            for friend in friendships:
                # friendships is a set of integers
                if friend not in visited and friend != user_id:
                    visited[friend] = get_shortest_path(user_id, friend)
                    q.enqueue(self.friendships[friend])
                # looks like you'll have to do a traversal of that connected component
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(f'Connections: \n{connections}')
