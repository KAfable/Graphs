# Sprint Challenge

## Goal

- traversal of 2000 moves or less to hit every single room

## Brainstorm

- looking for the first traversal path seems to be using DFT
- getting the shortest traversal path seems like it would take longer using BFS
- maybe I should just start with BFS
- the main issue seems like we won't have a traditional stack or queue
- that's because you have to keep track of where you have explored first

## Getting Neighbors

- What does logging into traversal path look like?
- might need a helper function in reading the traversal part

## Rooms

- rooms is a dictionary of {room_id : room value} pairs
- a room is an array of [coordinates, neigbhors]
- coordinates are a tuple of (x, y) values
- neighbors are a dictionary of {direction: room_id}

## Backtracking

- the big issue is when you encounter a situation where you need to backtrack
- you can't use BFS here?
