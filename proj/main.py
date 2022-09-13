import sys, os

from p0, p1, p2 import *

def p0(args):
    msg, us_in, us_out = args
    return processo_envio_p0(msg, us_in, us_out)

def p1(args):
    msg, pub_key, signature, pos_us = args
    return processo_p1(msg, pub_key, signature, pos_us)

def p2(args):
    crypto, signature, pos_us = args
    return processo_p2(crypto, signature, pos_us)


def print_line(args):
    x = args[0]

nprocs = int(sys.argv[1])

graph = DFGraph()
sched = SchedulerWS(graph, nprocs, mpi_enabled = False)

req_node, resp_node = sched.set_wservice(("localhost", 8000))

node0 = FilterTagged(p0, 1)
node1 = FilterTagged(p1, 1)
node2 = FilterTagged(p2, 1)

graph.add(req_node)

graph.add(node0)
graph.add(node1)
graph.add(node2)

graph.add(resp_node)


req_node.add_edge(node0, 0)
node0.add_edge(node1, 0)
node1.add_edge(node2, 0)
node2.add_edge(resp_node, 0)

sched.start()
 
