import sys, os
from pyDF import *
from glob import glob
from mutagen.mp3 import EasyMP3 as load_mp3

def convert(args):
    path = args[0]
    mp3 = load_mp3(path)
    return (mp3.get("artist", ""), mp3.get("title", ""))

def print_line(args):
    tags = args[0]
    print(f"{tags[0]} - {tags[1]}")

nprocs = int(sys.argv[1])

graph = DFGraph()
sched = Scheduler(graph, nprocs, mpi_enabled = False)

files = glob(f"{sys.argv[2]}/*.mp3")

src = Source(files)
processing = FilterTagged(convert, 1)
printer = Serializer(print_line, 1)

graph.add(src)
graph.add(processing)
graph.add(printer)

src.add_edge(processing, 0)
processing.add_edge(printer, 0)

sched.start()
 
