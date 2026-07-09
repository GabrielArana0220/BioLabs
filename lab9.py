def k_mers(seq, num):
	kmers = []
	for i in range(len(seq)-num+1):
		kmer = ""
		for j in range(i, num+i):
			kmer = kmer + seq[j]
		kmers.append(kmer)
	return kmers

def prefixsuffix(kmers):

	presuf = []

	for i in range(len(kmers)):
		prefix = ""
		for j in range(0,len(kmers[i])-1):
			prefix = prefix + kmers[i][j]
		suffix = ""
		for j in range(1,len(kmers[i])):
			suffix = suffix + kmers[i][j]

		presuf.append([prefix,suffix])
	return presuf


def adyacent_list(list_of_pairs):
	graph = []
	begin = []
	for i in range(len(list_of_pairs)):
		aux = list_of_pairs[i][0]
		aux_des = []
		aux_aux_des = []
		if aux in begin:
			continue
		for j in range(len(list_of_pairs)):
			if list_of_pairs[j][0] == aux:
				#aux_aux_des = [list_of_pairs[j][1]]
				if list_of_pairs[j][1] not in aux_aux_des:
					aux_des.append([list_of_pairs[j][1],1])
					aux_aux_des.append(list_of_pairs[j][1])
				else:
					for k in range(len(aux_des)):
						if aux_des[k][0] == list_of_pairs[j][1]:
							aux_des[k][1]+=1
		graph.append([aux,aux_aux_des])
		begin.append(aux)

	return graph

fragments = ["ATGGCAGATTAGTGCAATGG", "GGAGGCTTCGGAAACTGACT", "AGATTAGTGCAATGGCTTCA", 
  "ATGGCTTCAATTTTAGGTTC", "GTTCTATGCTTGGAGGCTTC", "TTCAATTTTAGGTTCTATGC", "TTTAGGTTCTATGCTTGGAG",
   "ATGCTTGGAGGCTTCGGAAA", "GTGCAATGGCTTCAATTTTA"]

lista = []
#for i in fragments:
#	lista = lista + k_mers(i,3)


def recorrido(grafo, inicio):
    visitados = set()
    recorrido = []

    def dfs(v):
        visitados.add(v)
        recorrido.append(v)

        for vecino in grafo.get(v, []):
            if vecino not in visitados:
                dfs(vecino)

    dfs(inicio)

    return recorrido

def reconstruir_seq(ruta):
	a = ""
	a = a + ruta[0]
	for i in range(1,len(ruta)):
		a = a + ruta[i][len(ruta[i])-1]
	return a

posible = [3,4,5,6,7,9]

for i in posible:
	lista = []
	for j in fragments:
		lista = lista+k_mers(j,i)
	#lista = k_mers(i,3)

	print("==========K_MERS===============")
	print()
	print(i)
	print()
	graph = adyacent_list(prefixsuffix(lista))

	#print(lista)

	graph_dict = {}

	for i in range(len(graph)):
		graph_dict[graph[i][0]] = graph[i][1]

	print("==============GRAFO RESULTANTE==============")
	print()

	for i in range(len(graph)):
		print(graph[i])

	print()
	print("=============RECORRIDO RECONSTRUIDO==============")
	ruta = recorrido(graph_dict, graph[0][0])

	print("Recorrido:")
	print(ruta)
	print("Reconstruido:")
	print(reconstruir_seq(ruta))

	print()
	print()
	print()
	#print(graph_dict)

#def recorrer_graph(dict):


#print(adyacent_list(prefixsuffix(k_mers(fragments[0],6))))

