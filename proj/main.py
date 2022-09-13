import sys, os

from p0, p1, p2 import *

def convert(args):
    path = args[0]

def print_line(args):
    tags = args[0]
    print(f"{tags[0]} - {tags[1]}")

nprocs = int(sys.argv[1])

graph = DFGraph()
sched = SchedulerWS(graph, nprocs, mpi_enabled = False)
req_node, resp_node = sched.set_wservice(("localhost", 8000))

src = Source(files)
processing = FilterTagged(convert, 1)
printer = Serializer(print_line, 1)

graph.add(src)
graph.add(processing)
graph.add(printer)

src.add_edge(processing, 0)
processing.add_edge(printer, 0)

sched.start()
 
