import networkx as nwx 

def graphe (*args):

    argCount = len(args)
    G = nwx.Graph()
    i=0  
    if argCount > 0 :
        liste =[]
        for elem in args :
            liste.append(elem)
            
       
        if len(liste)>1:
            while i<(len(liste)-1):
                G.add_node(liste[i])
                G.add_edge (liste[i],liste[i+1])
                i=i+1
        nwx.draw(G)   
        
        
    else:
        print("Acucun element")
        
    
#TEST
graphe(60896, 60895 , 60894, 60891 ,60893, 70002, 70003 , 60892, 60891, 70003)   
    

    
    
    
    
    
