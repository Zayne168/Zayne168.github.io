import networkx as nx
import numpy as np
import random
import math
import scipy
import csv

def degree_distribution(G):
	degree_dist = list()
	for node in G.nodes():
		degree_dist.append(G.degree(node))
	degree_dist.sort()
	avg_degree = sum(degree_dist) / len(degree_dist)
	print("Average degree: ", avg_degree)
	print("Max degree: ", max(degree_dist))
	print("Min degree: ", min(degree_dist))

def printDiam(G):
	G_is_conn = nx.is_connected(G)
	if G_is_conn:
		print("Diameter: ", nx.diameter(G))
	else:
		print("disconnected")
		
def degree_distribution_shape(G):
	degrees = np.array([d for _, d in G.degree()], dtype=float)
	mean_deg = degrees.mean()
	var_deg = degrees.var()
	std_deg = degrees.std()
	skew_deg = scipy.stats.skew(degrees)

	if mean_deg == 0:
		print("Degree distribution shape: Uniform")
		return "Uniform"

	coeff_var = std_deg / mean_deg
	poisson_error = abs(var_deg - mean_deg) / mean_deg
	top_1_pct = max(1, int(0.01 * len(degrees)))
	tail_share = np.sort(degrees)[-top_1_pct:].sum() / degrees.sum()

	if coeff_var < 0.20:
		shape = "Uniform"
	elif poisson_error < 0.35 and skew_deg < 1.0 and tail_share < 0.08:
		shape = "Poisson"
	else:
		shape = "heavy-tailed"

	print(shape)


def printGraphStats(G):
	printDiam(G)
	degree_distribution(G)
	degree_distribution_shape(G)
	c_ave = nx.average_clustering(G, nodes=None, weight=None, count_zeros=True)
	print("Average clustering coefficient: ", c_ave)
	print()

def PartA():
	print("**************")
	print("AVG DEGREE = 10")
	print("**************")

	n = 10000
	G1 = nx.random_geometric_graph(n, 0.01784)
	G2 = nx.gnp_random_graph(n, 0.0010001)
	G3 = nx.watts_strogatz_graph(n, 10, 0.2)
	G4 = nx.barabasi_albert_graph(n, 5)
	nx.write_gml(G1, f"GraphDeg10/rgg_{n}.gml")
	nx.write_gml(G2, f"GraphDeg10/erg_{n}.gml")
	nx.write_gml(G3, f"GraphDeg10/wsg_{n}.gml")
	nx.write_gml(G4, f"GraphDeg10/bag_{n}.gml")
	print("Graph 1: Random Geometric Graph")
	printGraphStats(G1)
	print("Graph 2: Erdos-Renyi Graph")
	printGraphStats(G2)
	print("Graph 3: Watts-Strogatz Graph")
	printGraphStats(G3)
	print("Graph 4: Barabasi-Albert Graph")
	printGraphStats(G4)

	n = 20000
	G5 = nx.random_geometric_graph(n, 0.01262)
	G6 = nx.gnp_random_graph(n, 0.00050003)
	G7 = nx.watts_strogatz_graph(n, 10, 0.2)
	G8 = nx.barabasi_albert_graph(n, 5)
	nx.write_gml(G5, f"GraphDeg10/rgg_{n}.gml")
	nx.write_gml(G6, f"GraphDeg10/erg_{n}.gml")
	nx.write_gml(G7, f"GraphDeg10/wsg_{n}.gml")
	nx.write_gml(G8, f"GraphDeg10/bag_{n}.gml")
	print("Graph 5: Random Geometric Graph")
	printGraphStats(G5)
	print("Graph 6: Erdos-Renyi Graph")
	printGraphStats(G6)
	print("Graph 7: Watts-Strogatz Graph")
	printGraphStats(G7)
	print("Graph 8: Barabasi-Albert Graph")
	printGraphStats(G8)

	n = 50000
	G9 = nx.random_geometric_graph(n, 0.00798)
	G10 = nx.gnp_random_graph(n, 0.0002)
	G11 = nx.watts_strogatz_graph(n, 10, 0.2)
	G12 = nx.barabasi_albert_graph(n, 5)
	nx.write_gml(G9, f"GraphDeg10/rgg_{n}.gml")
	nx.write_gml(G10, f"GraphDeg10/erg_{n}.gml")
	nx.write_gml(G11, f"GraphDeg10/wsg_{n}.gml")
	nx.write_gml(G12, f"GraphDeg10/bag_{n}.gml")
	print("Graph 9: Random Geometric Graph")
	printGraphStats(G9)
	print("Graph 10: Erdos-Renyi Graph")
	printGraphStats(G10)
	print("Graph 11: Watts-Strogatz Graph")
	printGraphStats(G11)
	print("Graph 12: Barabasi-Albert Graph")
	printGraphStats(G12)


	print("**************")
	print("AVG DEGREE = 20")
	print("**************")

	n = 10000
	G1 = nx.random_geometric_graph(n, 0.02523)
	G2 = nx.gnp_random_graph(n, 0.0020002)
	G3 = nx.watts_strogatz_graph(n, 20, 0.2)
	G4 = nx.barabasi_albert_graph(n, 10)
	nx.write_gml(G1, f"GraphDeg20/rgg_{n}.gml")
	nx.write_gml(G2, f"GraphDeg20/erg_{n}.gml")
	nx.write_gml(G3, f"GraphDeg20/wsg_{n}.gml")
	nx.write_gml(G4, f"GraphDeg20/bag_{n}.gml")
	print("Graph 1: Random Geometric Graph")
	printGraphStats(G1)
	print("Graph 2: Erdos-Renyi Graph")
	printGraphStats(G2)
	print("Graph 3: Watts-Strogatz Graph")
	printGraphStats(G3)
	print("Graph 4: Barabasi-Albert Graph")
	printGraphStats(G4)

	n = 20000
	G5 = nx.random_geometric_graph(n, 0.01784)
	G6 = nx.gnp_random_graph(n, 0.001)
	G7 = nx.watts_strogatz_graph(n, 20, 0.2)
	G8 = nx.barabasi_albert_graph(n, 10)
	nx.write_gml(G5, f"GraphDeg20/rgg_{n}.gml")
	nx.write_gml(G6, f"GraphDeg20/erg_{n}.gml")
	nx.write_gml(G7, f"GraphDeg20/wsg_{n}.gml")
	nx.write_gml(G8, f"GraphDeg20/bag_{n}.gml")
	print("Graph 5: Random Geometric Graph")
	printGraphStats(G5)
	print("Graph 6: Erdos-Renyi Graph")
	printGraphStats(G6)
	print("Graph 7: Watts-Strogatz Graph")
	printGraphStats(G7)
	print("Graph 8: Barabasi-Albert Graph")
	printGraphStats(G8)

	n = 50000
	G9 = nx.random_geometric_graph(n, 0.01128)
	G10 = nx.gnp_random_graph(n, 0.0004)
	G11 = nx.watts_strogatz_graph(n, 20, 0.2)
	G12 = nx.barabasi_albert_graph(n, 10)
	nx.write_gml(G9, f"GraphDeg20/rgg_{n}.gml")
	nx.write_gml(G10, f"GraphDeg20/erg_{n}.gml")
	nx.write_gml(G11, f"GraphDeg20/wsg_{n}.gml")
	nx.write_gml(G12, f"GraphDeg20/bag_{n}.gml")
	print("Graph 9: Random Geometric Graph")
	printGraphStats(G9)
	print("Graph 10: Erdos-Renyi Graph")
	printGraphStats(G10)
	print("Graph 11: Watts-Strogatz Graph")
	printGraphStats(G11)
	print("Graph 12: Barabasi-Albert Graph")
	printGraphStats(G12)

def resilienceBetwenness(G, name):
	G=G.copy()
	step = 0
	filename = f"{name}_betweenness.csv"

	with open(filename,"w",newline="") as f:
		writer = csv.writer(f)
		writer.writerow(["Fraction Removed", "LCC Size", "Number of Components"])
		while G.number_of_nodes() > 0:
			lccSize = len(max(nx.connected_components(G), key=len))
			componentCount = nx.number_connected_components(G)
			fractionRemoved = step/5000
			print(f"Fraction Removed: {fractionRemoved:.4f} LCC:{lccSize} #CC:{componentCount}")
			
			bc_dict = dict(nx.betweenness_centrality(G))
			sorted_bcs = sorted(bc_dict.items(), key=lambda x: x[1], reverse=True)
			max_bs_node = sorted_bcs[0][0]

			writer.writerow([f"{fractionRemoved:.4f}", lccSize, componentCount])
			#print(max_bs_node)
			G.remove_node(max_bs_node)
			step+=1
	
def resilienceRandom(G,name):
	G=G.copy()
	step=0
	filename = f"{name}_random.csv"
	with open(filename,"w",newline="") as f:
		writer = csv.writer(f)
		writer.writerow(["Fraction Removed", "LCC Size", "Number of Components"])
		while G.number_of_nodes() > 0:
			lccSize = len(max(nx.connected_components(G), key=len))
			componentCount = nx.number_connected_components(G)
			fractionRemoved = step/5000
			print(f"Fraction Removed:{fractionRemoved:.4f} LCC:{lccSize} #CC:{componentCount}")
			
			random_node = random.choice(list(G.nodes()))
			writer.writerow([f"{fractionRemoved:.4f}", lccSize, componentCount])
			#print(random_node)
			G.remove_node(random_node)
			step+=1

def PartB():
	n = 2500
	G1 = nx.random_geometric_graph(n, 0.03192)
	G2 = nx.gnp_random_graph(n, 0.0032013)
	G3 = nx.watts_strogatz_graph(n, 8, 0.2)
	G4 = nx.barabasi_albert_graph(n, 4)
	graphs = {
		"RGG": G1,
		"ER": G2,
		"WS": G3,
		"BA": G4
	}
	print("Random Attack")
	for name, graph in graphs.items():
		#print(name)
		resilienceRandom(graph, name)


	print("Betweenness Attack")
	for name, graph in graphs.items():
		#print(name)
		resilienceBetwenness(graph, name)
PartA()
PartB()
