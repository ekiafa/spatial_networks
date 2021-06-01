# spatial_networks
Spatial networks and top k queries assignment in the context of Complex Data Management course [Complex Data Management](https://www.cs.uoi.gr/course/%CE%B4%CE%B9%CE%B1%CF%87%CE%B5%CE%AF%CF%81%CE%B9%CF%83%CE%B7-%CF%83%CF%8D%CE%BD%CE%B8%CE%B5%CF%84%CF%89%CE%BD-%CE%B4%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CF%89%CE%BD/)


<h3>Input files:</h3>
edges.txt : contains edges for the undirected graph that we need,and weights for each of them
nodes.txt : contains coordinates for each node in graph,needed for calculation of Euclidean distance in A-star algorithm

<h3>Programm files:</h3>
data.py : There is a script that allow us to organise our input files to a central construction
dijkstra_a_star.py : There are implementations about Dijkstra and A-star algorithms.A-star contains a expansion in evaluation equation.
nra.py :Variation of No-Random-Access algorithm with Dijkstra usage for data input.

<h3>Language:</h3>
Python 3.6.0

<h3>License:</h3>
MIT
