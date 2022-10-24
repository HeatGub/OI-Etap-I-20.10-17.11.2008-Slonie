# Słonie - Olimpiada Informatyczna (OI), Etap I, 20.10–17.11.2008
# The algorithm takes the input from the console (4 lines of integers), and displays the result in the console.

#Input data and its' conversion to integers
N = int(input()) #amount of elephants
masy = list(map(int, input().split())) #masses of elephants
a = list(map(int, input().split())) #original order
b = list(map(int, input().split())) #desired order

#Every element of a and b orders -1 (to make the lowest value = 0)
a = [ai - 1 for ai in a]
b = [bi - 1 for bi in b]
    
p = [0] * N #permutation
swapd = [False] * N #swapped?
minA = min(masy) #the lightest of them all

#permutation construction
for i in range (0,N):
    p[b[i]] = a[i]

result = 0; #declare the result variable
for ini in range (0,N):
    
    if swapd[ini] == False:
        minC = 10e9
        sumaC = 0
        now = ini
        lenC = 0 
        
        while 4>2: #always true - infinite loop (till break)
            minC = min(minC, masy[now]) #the lightest in the cycle
            sumaC = sumaC + masy[now] #sum of masses in the cycle
            now = p[now]
            swapd[now] = True 
            lenC = lenC +1 #length of the cycle

            if now == ini:
                break
            
        met1 = sumaC + (lenC-2)*(minC)
        met2 = sumaC + minC + (lenC+1)*minA
        result = result + min(met1, met2) #choose the best method
        
# display the final result
print (result)