# Graphs

## What is a Graph?

- collection of data represented:
  - nodes
  - connections between those nodes
- Components:
  - nodes/vertices: represents objects in a data set
  - connections between vertices, can be bidirectional
  - weight: cost to travel across an edge, not all edges are created equal, optional component
- a graph is represented in data by:
  - a set of vertices, the nodes themselves
  - a set of edges (to show where relationships occur, and their weight)
- how the edges behave determines what a graph is called
- there is no hierarchy of nodes

## Uses Cases

- anything that can be described as a network or meets the criteria of a network can be modeled using graphs
- Social network, Transit systems, or traveling plans

## Examples

- Directed Graphs: can only move in one direction along edges (similar to a looped linked list)
- Undirected Graph: allows movement in both directions across an edge (similar to a looped doubly linked list)
- Cyclic Graph: edges allow you to revisit one at least one edge
- ACyclic Graph: vertices can only be visited once
  - does that mean all acyclic graphs are not undirected?

## Adjacency Matrix

- two dimensional array that has built-in edge weights
- each inner array represents a node, and each array element represents its relationship to other nodes
- graphs are dense when they have a high number of edges per vertex (as in many relationships per node)

## Breadth First Search

- useful for finding the shortest path on an unweighted graph
- searches across, instead of searching down
- it explores each node that are X distance from the origin node, before moving to X + 1 distance
- does not re-explore or re-search nodes so it never revisits nodes
- useful in social networking applications for finding mutual friends
