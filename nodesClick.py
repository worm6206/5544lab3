import simplejson as json

ego_nodes = ["0","107","348","414","686","698","1684","1912","3437","3980"]


result = {"name":"FB","children":[]}


root = result["children"]

for ego in ego_nodes:
    root.append({"name":ego,"children":[]});

e = 0
parent0 = root
for ego in ego_nodes:
    root = root[e]["children"]
    filename = ("facebook/facebook/%s.circles"%ego)
    i = 0
    parent = root
    for line in open((filename)):
        root.append({"name":str(i),"children":[]})
        root = root[i]["children"]
        parent1 = root
        for n in line.split()[1:]:
            root.append({"name":str(n),"children":[]})
            root = parent1
        root = parent
        i = i+1
    e=e+1
    root = parent0
    
        


    
print json.dumps(result)


