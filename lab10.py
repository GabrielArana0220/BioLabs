import numpy as np
from io import StringIO

from Bio import Phylo

import matplotlib.pyplot as plt


names = ["canis_l", "danio_r", "gorilla", "homo_s", "mus_m", "pan_t", "xenopus"]

def matrix_Q(D):
    n = len(D)

    row_sum = D.sum(axis=1)

    Q = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            if i == j:
                Q[i,j] = 0
            else:
                Q[i,j] = ((n-2)*D[i,j] - row_sum[i] - row_sum[j])
    return Q



upper = np.array([
    [0,12959,7347,9015,6981,7374,10292],
    [0,0,12663,11190,11927,13068,12999],
    [0,0,0,4068,7209,2197,11142],
    [0,0,0,0,9037,3738,12735],
    [0,0,0,0,0,7346,10834],
    [0,0,0,0,0,0,10709],
    [0,0,0,0,0,0,0]
])

D = upper + upper.T

print(D)

iteration = 1

while len(names) > 2:

	print("\nITERACION: ", iteration)
	print()
	print()

	Q = matrix_Q(D)

	print("Q:")
	print(Q)

	n = len(D)

	min_val = np.inf
	pair = None

	for i in range(n):
		for j in range(i+1,n):
			if Q[i,j] < min_val:
				min_val = Q[i,j]
				pair = (i,j)

	i,j = pair
	
	print(
		f"Se unen: {names[i]} y {names[j]}")



	ri = D[i].sum()
	rj = D[j].sum()

	Li = 0.5 * D[i,j]+(ri-rj)/2*(n-2)
	Lj = abs(D[i,j] - Li)

	new_dist = []

	for k in range(n):

		if k != i and k != j:

			d_uk = ( D[i,k] + D[j,k] - D[i,j]) / 2

			new_dist.append(d_uk)

	keep = [
		k for k in range(n)
		if k != i and k != j]

	D_reduced = D[np.ix_(keep, keep)]

	m = len(D_reduced)

	D_new = np.zeros((m + 1, m + 1))

	D_new[:m, :m] = D_reduced

	for idx, dist in enumerate(new_dist):
		D_new[idx, m] = dist
		D_new[m, idx] = dist

	D_new[m, m] = 0

	new_name = (
    f"({names[i]}:{Li:.2f},"
    f"{names[j]}:{Lj:.2f})")

	names = [names[k] for k in keep]
	names.append(new_name)

	D = D_new

	print("\nNueva matriz D:")
	print(D)

	print("\nNodos actuales:")
	print(names)

	iteration += 1

final_tree = (
    f"({names[0]}:{D[0,1]/2:.2f},"
    f"{names[1]}:{D[0,1]/2:.2f});"
)
print("Arbol Final")

print(final_tree)

tree = Phylo.read(
    StringIO(final_tree),
    "newick"
)

plt.figure(figsize=(12,8))
Phylo.draw(tree, do_show=False)
plt.show()
