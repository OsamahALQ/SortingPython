import math



def closest_enemies(x,y):
    # Ecludian Distanct 
    
    ecl = []
    for i in range(len(y)):

        ecl.append(math.sqrt(pow((x[0]-(y[i])[0]),2)+(pow(x[1]-(y[i])[1],2))))
    
    
    
    # Coctail Sort 
    swapped = True
    z = len(ecl) - 2
    while swapped:
        for i in range(0,z,1):
            if ecl[i] > ecl[i+1]:
                ecl[i],ecl[i+1] = ecl[i+1],ecl[i]
                swapped = True
        
        swapped = False
        for i in range(z,0,-1):
            if ecl[i] > ecl[i+1]:
                ecl[i],ecl[i+1] = ecl[i+1],ecl[i]
                swapped = True
    return ecl

def main():

    a = (4,5)
    b = [(1,2),(4,6),(5,9),(5,7),(12,6),(14,13),(0,0),(-9,-1),(4,6),(5,7)]
    final_Positions = closest_enemies(a,b)
    print("hero position :" + str(a)+"\n")
    print("Enemy positions :" + str(b)+"\n")
    z=[]
    for i in range(len(b)):
        z.append(math.sqrt(pow((a[0]-(b[i])[0]),2)+(pow(a[1]-(b[i])[1],2))))
    print("distance of enemies and hero : " +str(z) + "\n")

    print("distance of enemies and hero after coctail sort :"+ str(final_Positions)+"\n" )




main()