def mdc(a, b):
    #algoritmo de euclides para mdc
    while(b):
        a,b = b, a%b
    return a

def solveEquation(a,b,m):
    #recebe uma equação na forma a*x ≡ b (mod m)
    #retorna y em x ≡ y (mod m)
    #ou -1 se não houver solução
    
    if m<=0 : return -1
    
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
    # retorna a solução para o TCR no formato M,x,[[c,n,d],[c,n,d]]
    #em que x é a resposta e, [c,n,d] são, a congruência canônica de x, e os valores para o cálculo do TCR, para cada equação
    
    numEq = len(equations)
    mTotal = 1
    mdcTotal = 0
    ret = [[0]*3]*numEq
    
    #equações na forma [[a,m],...]
    #na forma x ≡ a (mod m)
    canonicos = [[0]*2]*numEq
    
    for i in range(numEq):
        a,b,m = equations[i]
        canonicos[i] = [solveEquation(a,b,m),m]
        if canonicos[i][0] == -1 : return f"A equação {i+1} não tem forma canônica!"
        if mdc(mTotal,m) != 1: return "Os módulos não são coprimos entre si dois a dois!"
        mTotal*= m
    
    x = 0
    for i in range(numEq):
        a,m = canonicos[i]
        c = a
        n = mTotal//m
        d = solveInverse(n,m)
        ret[i] = [c,n,d]
        x += c * n * d

    x %= mTotal
    return mTotal,x,ret