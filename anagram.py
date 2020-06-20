
def countss(string): 
   
    n = len(string) 
    s = dict() 
    answer=0
    
    for i in range(n-1): 
        sub = '' 
        for j in range(i, n): 
            sub = ''.join(sorted(sub + string[j])) 
            s[sub] = s.get(sub, 0) 
           
            s[sub] += 1
  
    
    for  a in s.items(): 
        answer += (a*(a-1))//2
    return answer 
  
string=input()
count = countss(string)
print(count) 
  