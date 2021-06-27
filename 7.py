from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import random
print('А алгоритм Форда-Беллмана')
print('В алгоритм Дейкстры')
q = 1
r = 10 ** 6
x_n = []
T_A1 = []
T_B1 = []
T_A2 = []
T_B2 = []
for n in range(100, 1000+ 1, 100):
    x_n.append(n)
    m = 10*n

    G, W = [], dict()
    for k in range(n):
        G.append([])
    for k in range(m):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if (i != j) and (not ((i, j) in W)):
            G[i].append(j)
            W[(i, j)] = random.randint(q, r)


    T_A1.append(datetime.now())
    d = [np.inf] * n
    d[0] = 0
    for k in range(1, n):
        for j, i in W.keys():
            if d[j] + W[j, i] < d[i]:
                d[i] = d[j] + W[j, i]
    T_A1[len(T_A1) - 1] = (datetime.now() - T_A1[len(T_A1) - 1]).total_seconds()
    print(' n_A(а) =', n, 'T =', T_A1[len(T_A1) - 1])


    T_B1.append(datetime.now())
    d = [np.inf] * n
    d[0], min_d, min_v, used = 0, 0, 0, [False] * n
    while min_d < np.inf:
        i = min_v
        used[i] = True
        for j in G[i]:
            if d[i] + W[(i, j)] < d[j]:
                d[j] = d[i] + W[(i, j)]
        min_d = np.inf
        for j in range(n):
            if not used[j] and d[j] < min_d:
                min_d = d[j]
                min_v = j
    T_B1[len(T_B1) - 1] = (datetime.now() - T_B1[len(T_B1) - 1]).total_seconds()
    print(' n_B(а) =', n, 'T =', T_B1[len(T_B1) - 1])

    m = 100*n
    G, W = [], dict()
    for k in range(n):
        G.append([])
    for k in range(m):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if (i != j) and (not ((i, j) in W)):
            G[i].append(j)
            W[(i, j)] = random.randint(q, r)


    T_A2.append(datetime.now())
    d = [np.inf] * n
    d[0] = 0
    for k in range(1, n):
        for j, i in W.keys():
            if d[j] + W[j, i] < d[i]:
                d[i] = d[j] + W[j, i]
    T_A2[len(T_A2) - 1] = (datetime.now() - T_A2[len(T_A2) - 1]).total_seconds()
    print( ' n_A(б) =', n, 'T =', T_A2[len(T_A2) - 1])


    T_B2.append(datetime.now())
    d = [np.inf] * n
    d[0], min_d, min_v, used = 0, 0, 0, [False] * n
    while min_d < np.inf:
        i = min_v
        used[i] = True
        for j in G[i]:
            if d[i] + W[(i, j)] < d[j]:
                d[j] = d[i] + W[(i, j)]
        min_d = np.inf
        for j in range(n):
            if not used[j] and d[j] < min_d:
                min_d = d[j]
                min_v = j
    T_B2[len(T_B2) - 1] = (datetime.now() - T_B2[len(T_B2) - 1]).total_seconds()

    print(' n_B(б) =', n, 'T =', T_B2[len(T_B2) - 1])




plt.plot(x_n, T_A1)
plt.ylabel('t')
plt.xlabel('n')
plt.title('Алгоритм A а')
plt.show()

plt.plot(x_n, T_B1)
plt.ylabel('t')
plt.xlabel('n')
plt.title('Алгоритм В а')
plt.show()

plt.plot(x_n, T_A2)
plt.ylabel('t')
plt.xlabel('n')
plt.title('Алгоритм A б')
plt.show()

plt.plot(x_n, T_B2)
plt.ylabel('t')
plt.xlabel('n')
plt.title('Алгоритм В б')
plt.show()



