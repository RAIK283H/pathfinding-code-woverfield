# Pathfinding Starter Code

## Customer Requirements

- Random Player Pathing Algorithm:
- The Random player shall have a randomly assigned path which begins with the start node,
  ends with the exit node, and hits the target along the path. The path shall be a valid
  traversal such that each sequential pair of nodes in the path are connected by an edge.

- New Statistic for the Scoreboard:
- In addition to existing statistics, the scoreboard should track and display a new statistic.

## Random Pathing Algorithm

My random pathing algorithm generates a random index from the current node's adjacency list to figure out the next node and does this until it reaches the target node. Then it does it again until it reaches the exit. Creating a random path which will always hit the target and exit as required.

## New Stat: Total Objectives

My statistic, Total Objectives, tracks how many nodes the player has successfully visited during their traversal. Each time the player reaches a node (objective), the count increases.
