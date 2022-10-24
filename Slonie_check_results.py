# Słonie - Olimpiada Informatyczna (OI), Etap I, 20.10–17.11.2008
# The algorithm takes the input from the list of files named slo(...).in
# This version of algorithm is made just to compare the results with the slo(..).out files (not all of them contained in my repository)

import glob

in_files = [] #list of input files
for file in glob.glob("slo*.in"): # * means any symbol in various amount
    in_files.append(file) 
    
out_files = [] #list of output files
out_results = [] #list of results from the output files

for file in glob.glob("slo*.out"):
    out_files.append(file)
    
for f in range (0, len(out_files)): #read the lines of a textfile for all the files

    out_file = open(str(out_files[f]), "r")
    out_lines = out_file.readlines()
    out_file.close() #close the file to not interrupt
    out_line_n = out_lines[0].split()
    out_n = []
    
    for i in out_line_n: #make it integer
        out_n.append(int(i))
        out_result = int(out_n[0])
        out_results.append(out_result)
    
in_names = []
my_results = []
    
for f in range (0, len(in_files)): #open files and read the lines

    file = open(str(in_files[f]), "r")
    lines = file.readlines()
    file.close()
    
    line_n = lines[0].split() #split the lines
    line_masy = lines[1].split()
    line_a = lines[2].split()
    line_b = lines[3].split()
        
    n = []
    for i in line_n: #splitted lines into integers (a and b -1 to make their lowest value =0)
        n.append(int(i))
        N = int(n[0])
    masy = []
    for i in line_masy:
        masy.append(int(i))
    a = []
    for i in line_a:
        a.append(int(i)-1)
    b = []
    for i in line_b:
        b.append(int(i)-1)
    
    p = [0] * N #permutation
    swapd = [False] * N #swapped?
    minA = min(masy) #the lightest of them all
    
    #permutation construction p
    for i in range (0,N):
        p[b[i]] = a[i]
    
    result = 0;
    for ini in range (0,N):
        
        if swapd[ini] == False:
            minC = 10e9
            sumaC = 0
            now = ini
            lenC = 0
            lim = 4
            
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
            
    in_names.append(in_files[f])
    my_results.append(result)
    
    print ("\n" + in_files[f] + " " + str(result))

check = [] #compare the results with .out files
for c in range (0, len(out_results)):
    check.append(out_results[c] - my_results[c])
    
for ch in range (0, len(check)): #indicate the wrong result (when difference is not 0)
    if check[ch] !=0:
        print ("\n   result of " + in_names[ch] + " is incorrect")