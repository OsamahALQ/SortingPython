def cachedfibonacci(x,m):
    if x < 0: 
        return "Not Valid"
    if x == 0:
        return 0
    elif x == 1:
        m[1] = 1
        return x
    else:
        if x in m:
            return m[x]
        z = cachedfibonacci(x-1,m) + cachedfibonacci(x-2,m)
        m[x] = z
        return z

def main():
    
    m = dict()
    m = {}

    x = 6
    print ("x = " + str(x))
    print ("Expected Value = 8")
    print ("Actual Value = " + str(cachedfibonacci(x,m)))
    x = 20
    print ("x = " + str(x))
    print ("Expected Value = 6765")
    print ("Actual Value = " + str(cachedfibonacci(x,m)))
    x = 1
    print ("x = " + str(x))
    print ("Expected Value = 1")
    print ("Actual Value = " + str(cachedfibonacci(x,m)))
    x = 100
    print ("x = " + str(x))
    print ("Expected Value = 354224848179261915075")
    print ("Actual Value = " + str(cachedfibonacci(x,m)))
    x = 50
    print ("x = " + str(x))
    print ("Expected Value = 12586269025")
    print ("Actual Value = " + str(cachedfibonacci(x,m)))
    x = 0
    print ("x = " + str(x))
    print ("Expected Value = 0")
    print ("Actual Value = " + str(cachedfibonacci(x,m)))
    x = -1
    print ("x = " + str(x))
    print ("Expected Value = Not Valid")
    print ("Actual Value = " + str(cachedfibonacci(x,m)))
   
   


main()