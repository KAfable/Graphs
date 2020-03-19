from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# stack of room objects
# s = Stack()
# s.push(player.current_room.id)
# visited = set()
# the order of these directions could greatly affect the time based on the map


# def get_path(origin_id, destination_id):
#     '''Helper function that returns an array of directions to get to destination room via BFS.'''
#     q = Queue()
#     q.enqueue([origin_id])
#     directions = []
#     visited = set()
#     while q.size() > 0:
#         path = q.dequeue()
#         current = path[-1]
#         if current not in visited:
#             visited.add(current)
#             if current

# let's use DFT to travel print out all rooms in any order
stack = Stack()
stack.push(player.current_room)
visited = []

# While the stack is not empty
while stack.size() > 0:
    current = stack.pop()
    if current.id not in visited:
        visited.append(current.id)
        # how do you get neighbors?
        directions = current.get_exits()
        for d in directions:
            room = current.get_room_in_direction(d)
            stack.push(room)
print(len(visited))


# destination = s.pop()
# # TODO function get path to travel here
# # TODO loop through path to get here
# if destination not in visited:
#     # mark it as visited
#     visited.add(destination)
#     # add its neighbors to stack and keep exploring
#     directions = destination.get_exits()
#     for d in directions:
#         s.push(destination.get_room_in_direction(d))
# else:
#     pass
#     #

# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(
#         f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
