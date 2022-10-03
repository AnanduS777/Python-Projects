

def fileOp(doc):
    try:
        file1=open(doc,"r")
        f=0
        
        for x in file1:
            data=x.split()
            
        for i in data:
            f=f+1
            
        return f
    
    except:
        return -1
