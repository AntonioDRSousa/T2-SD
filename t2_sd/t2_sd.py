import sys, os
from pyDF import *

def convert(args):
    pass

def print_line(args):
	line = args[0]
	print("-- {} --".format(line[:-1]))

nprocs = int(sys.argv[1])

graph = DFGraph()
sched = Scheduler(graph, nprocs, mpi_enabled = False)

fp = open(sys.argv[2], "r")

src = Source(fp)
processing = Node(convert, 1)
printer = Serializer(print_line, 1)

printer.pin(0)
graph.add(src)
graph.add(processing)
graph.add(printer)

src.add_edge(processing, 0)
processing.add_edge(printer, 0)

sched.start()
 
