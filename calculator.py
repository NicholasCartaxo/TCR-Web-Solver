def mdc(a, b):
    #algoritmo de euclides para mdc
    while(b):
        a,b = b, a%b
    return a

def solveEquation(a,b,m):
    #recebe uma equação na forma a*x ≡ b (mod m)
    #retorna y em x ≡ y (mod m)
    #ou -1 se não houver solução
    a = a%m
    b = b%m

    d,r,s = bezout(a,m)

    #checa se tem solução
    if b%d: return -1

    return (r*b//d) % m

def solveInverse(a,m):
    #recebe uma equação na forma a*x ≡ 1 (mod m)
    #retorna x ou -1, se não houver solução
    return solveEquation(a,1,m)
    
def bezout(a,b):
    #retorna os coeficientes de bezout mdc(a,b) = as + bt
    #no formato [mdc(a,b), s, t]

    if b==0: return [a,1,0]

    prevStep = bezout(b,a%b)
    r = prevStep[0]
    s = prevStep[2]
    t = prevStep[1] - a//b * prevStep[2]

    return [r,s,t]

def solveTCR(equations):
    #recebe uma lista de listas, no formato [[a,b,m],[a,b,m],...]
    #em que cada lista informa ax ≡ b (mod m)
    # retorna a solução para o TCR no formato M,x,[[b,c,n,d],[b,c,n,d]]
    #em que x é a resposta e, [b,c,n,d] são, a congruência canônica de x, e os valores para o cálculo do TCR, para cada equação
    
    numEq = len(equations)
    M = 1
    mdcTotal = 0
    ret = [[0]*4]*numEq
    
    #equações na forma [[a,m],...]
    #na forma x ≡ a (mod m)
    canonicos = [[0]*2]*numEq
    
    for i in range(numEq):
        a,b,m = equations[i]
        canonicos[i] = [solveEquation(a,b,m),a]
        if canonicos[i][0] == -1 : return "A equação " + (i+1) + " não tem forma canônica!"
        M*= m
        mdcTotal = mdc(mdcTotal,equations[i][2])
    
    if mdcTotal != 1 : return "Os módulos não são coprimos entre si!"
    
    for i in range(numEq):
        a,m = canonicos[i]
    
    
    x = 0
    return M,x,ret
        
    

print(solveTCR([[1,2,3],[1,2,3]]))
