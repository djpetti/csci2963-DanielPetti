#!/usr/bin/python3

"""
Words/Ladder Graph
------------------
Generate  an undirected graph over the 5757 5-letter words in the
datafile words_dat.txt.gz.  Two words are connected by an edge
if they differ in one letter, resulting in 14,135 edges. This example
is described in Section 1.1 in Knuth's book [1]_,[2]_.
References
----------
.. [1] Donald E. Knuth,
   "The Stanford GraphBase: A Platform for Combinatorial Computing",
   ACM Press, New York, 1993.
.. [2] http://www-cs-faculty.stanford.edu/~knuth/sgb.html
"""
# Authors: Aric Hagberg (hagberg@lanl.gov),
#          Brendt Wohlberg,
#          hughdbrown@yahoo.com

#    Copyright (C) 2004-2016 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

import itertools

import networkx as nx

#-------------------------------------------------------------------
#   The Words/Ladder graph of Section 1.1
#-------------------------------------------------------------------
def generate_graph(words):
    from string import ascii_lowercase as lowercase
    G = nx.Graph(name="words")
    lookup = dict((c,lowercase.index(c)) for c in lowercase)

    def edit_distance_one(word):
        for i in range(len(word)):
            # Compute set of anagrams.
            anagrams = itertools.permutations(word)

            for anagram in anagrams:
                # Convert to string.
                anagram = "".join(anagram)
                left, c, right = anagram[0:i], anagram[i], anagram[i+1:]
                j = lookup[c] # lowercase.index(c)
                for cc in lowercase[j+1:]:
                    yield left + cc + right
    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word) if cand in words)
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G

def words_graph():
    """Return the words example graph from the Stanford GraphBase"""
    import gzip
    fh=gzip.open('words_dat.txt.gz','r')
    words=set()
    for line in fh.readlines():
        line = line.decode()
        if line.startswith('*'):
            continue
        w=str(line[0:5])
        words.add(w)

    # Load the four-letter word file.
    fh=open('words4.dat')
    four_letter=set()
    for line in fh.readlines():
      if line.startswith('*'):
        continue
      w=str(line[0:4])
      four_letter.add(w)

    return (generate_graph(words), generate_graph(four_letter))

if __name__ == '__main__':
    from networkx import *
    G5, G4=words_graph()
    print("Loaded words_dat.txt containing 5757 five-letter English words.")
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          %(number_of_nodes(G5),number_of_edges(G5)))
    print("%d connected components" % number_connected_components(G5))

    for (source,target) in [('chaos','order'),
                            ('nodes','graph'),
                            ('pound','marks'),
                            ('moron','smart'),
                            ('cold', 'warm'),
                            ('love', 'hate')]:
        print("Shortest path between %s and %s is"%(source,target))
        if len(source) == 5:
          word_graph=G5
        else:
          word_graph=G4

        try:
            sp=shortest_path(word_graph, source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")
