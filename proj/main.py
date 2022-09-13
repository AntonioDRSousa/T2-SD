import sys, os

from p0, p1, p2 import *

def convert(args):
    msg = args[0]
    processo_p1(msg)

def print_line(args):
    x = args[0]

nprocs = int(sys.argv[1])

graph = DFGraph()
sched = SchedulerWS(graph, nprocs, mpi_enabled = False)
req_node, resp_node = sched.set_wservice(("localhost", 8000))

processing = FilterTagged(convert, 1)

graph.add(req_node)

graph.add(processing)

graph.add(resp_node)


req_node.add_edge(processing, 0)
processing.add_edge(resp_node,0)

sched.start()
 
