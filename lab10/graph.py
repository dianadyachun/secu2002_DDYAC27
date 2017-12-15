import csv
import networkx as nx

#nodes are gangmembers and edge exists between two members if they co-offend
#nodes should be decorated with the ranking of the gang member
f = open('../../secu2002_master/data/london_gang.csv','r')
r = csv.DictReader (f,delimiter = ',')
alist=[]
for row in r:
    print row
    alist.append(row)

edge_connections = []
to_be_used_connection = []
counter=0
for row in alist:
    #print row
    for gangnumber, connection in row.items():
        #print gangnumber,connection
        if connection != 0:
            to_be_used_connection.append(connection)
            print connection
            #print to_be_used_connection
    counter+=1
#graph = nx.Graph()
#graph.add_node()

#graph.add_edge()