import sys, os

from pyDF import *

from p0 import *
from p1 import *
from p2 import *

def p0(args):
    msg, us_in, us_out = args[0]
    return processo_p0(msg, us_in, us_out)

def p1(args):
    pub_key, priv_key, msg, us_in, us_out = args[0]
    return processo_p1(pub_key, priv_key, msg, us_in, us_out)

def p2(args):
    crypto, signature, pub_key, us_in, us_out = args[0]
    return processo_p2(crypto, signature, pub_key, us_in, us_out)


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
 
