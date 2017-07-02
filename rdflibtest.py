from rdflib import Graph

g = Graph()


g.parse("foaf.rdf")

for s,p,o in g:
    print (s,p,o)

