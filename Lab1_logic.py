import math

cameron_total = 0
allison_total = 0
diego_total = 0

def add(status):
    global cameron_total, allison_total, diego_total
    if(int(status) == 1):
        cameron_total += 1
    elif(int(status) == 2):
        allison_total += 1
    elif(int(status) == 3):
        diego_total +=1
        
def results():
    return f"Cameron Total: {cameron_total}\nAllison Total: {allison_total}\nDiego Total: {diego_total}"
            
        
