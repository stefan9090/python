import math
import copy
INFINITY = math.inf

class myqueue(list):
    def __init__(self,a=[]):
        list.__init__(self,a)
    def dequeue(self):
        return self.pop(0)
    def enqueue(self,x):
        self.append(x)

class Vertex:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return str(self.data)
    def __lt__(self, other): 
        return self.data < other.data

def vertices(G):
    return sorted(G)

def edges(G):
    return [(u,v) for u in vertices(G) for v in G[u]]

v = [Vertex(i) for i in range(8)]

G1 = {v[0]:[v[5], v[4]],
     v[1]:[v[4], v[5], v[6]],
     v[2]:[v[4], v[5], v[6]],
     v[3]:[v[7]],
     v[4]:[v[0], v[1], v[2], v[5]],
     v[5]:[v[0], v[1], v[2], v[4]],
     v[6]:[v[1], v[2]],
     v[7]:[v[3]]}

G2 = {v[0]:[v[5], v[4]],
     v[1]:[v[4], v[5], v[6]],
     v[2]:[v[4], v[5], v[6]],
     v[4]:[v[0], v[1], v[2], v[5]],
     v[5]:[v[0], v[1], v[2], v[4]],
     v[6]:[v[1], v[2]]}

G3 = {v[0]:[v[5], v[4]],
     v[1]:[v[4], v[6]],
     v[2]:[v[5]],
     v[3]:[v[7]],
     v[4]:[v[0], v[1]],
     v[5]:[v[0], v[2]],
     v[6]:[v[1]],
     v[7]:[v[3]]}

G4 = {v[0]:[v[1], v[3]],
     v[1]:[v[0], v[2]],
     v[2]:[v[1], v[3], v[4]],
     v[3]:[v[0], v[2]],
     v[4]:[v[2], v[5], v[6]],
     v[5]:[v[4], v[6]],
     v[6]:[v[4], v[5], v[7]],
     v[7]:[v[6]]}

euler = {v[0]:[v[1], v[2]],
     v[1]:[v[0], v[3]],
     v[2]:[v[0], v[3]],
     v[3]:[v[6], v[2], v[4], v[1]],
     v[4]:[v[3], v[6], v[5], v[7]],
     v[5]:[v[4], v[6]],
     v[6]:[v[3], v[4], v[5], v[7]],
     v[7]:[v[6], v[4]]}

stronglyConnected = {v[0]:[v[1]],
                     v[1]:[v[2]],
                     v[2]:[v[0]]}

notStronglyConnected = {v[0]:[v[1]],
                     v[1]:[v[2]],
                     v[2]:[v[0]],
                     v[4]:[v[1]]}

def make_graph(v):
    euler = {v[0]:[v[1], v[2]],
     v[1]:[v[0], v[3]],
     v[2]:[v[0], v[3]],
     v[3]:[v[6], v[2], v[4], v[1]],
     v[4]:[v[3], v[6], v[5], v[7]],
     v[5]:[v[4], v[6]],
     v[6]:[v[3], v[4], v[5], v[7]],
     v[7]:[v[6], v[4]]}
    return euler

test = {v[0]:[v[1]],
     v[1]:[v[0]]}

def BFS(G,s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY
    q = myqueue()
    q.enqueue(s) 
    while q:
        u = q.dequeue() 
        for v in G[u]:
            if v.distance == INFINITY:
                v.distance = u.distance + 1
                v.predecessor = u
                q.enqueue(v)

def no_cycles(G):
    V = vertices(G)
    s = V[0]
    s.predecessor = None
    s.distance = 0
    usedVertices = []
    for v in V:
        if v != s:
            v.distance = INFINITY
    q = myqueue()
    q.enqueue(s) 
    while q:
        u = q.dequeue()
        if v.distance == INFINITY:
            v.distance = u.distance + 1
            v.predecessor = u
            q.enqueue(v)
        elif v.distance >= u.distance:
            return False
    return True

#print(no_cycles(G1))

def path_BFS(G,u,v):
    BFS(G,u)
    a = []
    if hasattr(v,'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a
"""
def is_connected(G):
    V = vertices(G)
    s = G[V[0]][0]
    s.predecessor = None
    s.distance = 0
    usedVertices = []
    for v in V:
        if v != s:
            v.distance = INFINITY
    q = myqueue()
    q.enqueue(s) 
    while q:
        u = q.dequeue()
        usedVertices.append(u)
        for v in G[u]:
            
            if v.distance == INFINITY:
                v.distance = u.distance + 1
                v.predecessor = u
                q.enqueue(v)
    return len(V)==len(usedVertices)
"""
def is_connected(G):
    V = vertices(G)
    BFS(G, V[0])
    for v in G:
        if v.distance == INFINITY:
            return False
    return True 



def isConnected(G, s, e):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY
    q = myqueue()
    q.enqueue(s) 
    while q:
        u = q.dequeue()
        if u == e:
            return True
        for v in G[u]:
            if v.distance == INFINITY:
                v.distance = u.distance + 1
                v.predecessor = u
                q.enqueue(v)
    return False
    
def get_bridges(G):
    V = vertices(G)
    s = G[V[0]][0]
    u = s
    bridges = []
    for u in V:
        for v in G[u]:
            index = G[u].index(v)
            buffer = G[u][index]
            del G[u][index]
            if not isConnected(G, u, v):
                bridges.append((u, v))
            G[u].insert(0, buffer)
    return bridges

def getBridges(G, s):
    V = vertices(G)
    u = s
    bridges = []
    for u in V:
        for v in G[u]:
            index = G[u].index(v)
            buffer = G[u][index]
            del G[u][index]
            if not isConnected(G, u, v):
                bridges.append((u, v))
            G[u].insert(0, buffer)
    return bridges


def reverse(G):
    V = vertices(G)
    reversedG = {}
    for v in V:
        reversedG[v] = []  
    for base in V:
        for sub in V:
            if base in G[sub]:
                reversedG[base].append(sub)
    return reversedG

def is_strongly_connected(G):
    if is_connected(G):
        reversedG = reverse(G)
        if is_connected(reversedG):
            return True
    return False

def is_euler_graph(G):
    V = vertices(G)
    for i in range(len(V)-1):
        if len(G[V[i]])%2:
            return False
    return True

def get_euler_circuit(G, s):
    path = [s]
    V = vertices(G)
    while len(edges(G))!=0:
        for a in G[s]:
            if a not in getBridges(G, s):
                t = a
                break
        path.append(t)   
        G[t].remove(s)
        G[s].remove(t)
        s = t
    return path
"""
def get_euler_circuit(G, s):
    path = [s]
    V = vertices(G)
    while len(edges(G))!=0:
        for a in G[s]:
            if not isBridge(G, s, a):
                t = a
                break
        path.append(t)   
        G[t].remove(s)
        G[s].remove(t)
        print(path)
        s = t
    return path
"""

#print(is_connected(G1))
#print(is_connected(G2))
#print(no_cycles(G2))
#print(no_cycles(G3))
#for V in v:
#    print(get_euler_circuit(make_graph(v),V))

print(get_euler_circuit(euler, v[1]))

#print(is_euler_graph(euler))
#print(get_euler_circuit(euler, v[4]))
#print(5%2)
