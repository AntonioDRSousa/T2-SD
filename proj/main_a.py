import sys, os
import time
import p0
import p1
import p2
import script

from pyDF import *

nprocs = int(sys.argv[1])
stride = float(sys.argv[2])

graph = DFGraph()
sched = Scheduler(graph, nprocs, mpi_enabled = False)


SP = Node(script.main, 0)
P0 = Node(p0.processo_envio_p0, 1)
P1 = Node(p1.processo_p1, 1)
P2 = Node(p2.processo_p2, 1)

graph.add(SP)
graph.add(P0)
graph.add(P1)
graph.add(P2)

P0.add_edge(SP, 0)
P1.add_edge(P0, 0)
P2.add_edge(P1, 0)

t0 = time.time()
sched.start()
t1 = time.time()

print("Execution time "+str(t1-t0))
