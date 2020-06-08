# ExponentialMinimunSimulation
This is a project that will simulate the behaviour of a closed system with M nodes, and K indistinguishable elements spread through the M nodes. Where every node can only serve one element at a time, and if there is more than one element in a given node, the rest must wait in a queue for the node to serve the first elemnt of the queue. 
Also, Every node has an instrisic exponential distributed random variable, that gives the time that it will take to this node to serve one customer. After a customer is served, it will move to one of the other M-1 nodes, where there is a fixed probability for moving from node A to node B, and the sum of all the probabilities for moving from node A to the other nodes is equal to 1.

