function mdc(a,b){
    //algoritmo de euclides para mdc
    while(b){
        temp = b;
        b = a%b;
        a = temp;
    }
    return a;
}

function solveEquation(a,b,m){
    //retorna x para: a*x ≡ b (mod m)
    //ou -1 se não houver solução
    a = a%m;
    b = b%m;

    d = mdc(a,m);

    //checa se tem solução
    if(b%d) return -1;


}

function bezout(a,b){
    //retorna os coeficientes de bezout mdc(a,b) = as + bt
    //no formato [mdc(a,b), s, t]

    if(b==0) return [a,1,0];

    prevStep = bezout(b,a%b);
    r = prevStep[0];
    s = prevStep[2];
    t = prevStep[1] - Math.floor(a/b) * prevStep[2];

    return [r,s,t];
}


function printBezout(a,b){
    res = bezout(a,b);
    r = res[0];
    s = res[1];
    t = res[2];
    console.log("mdc("+a+","+b+") = "+r+" = " + a + "*" + s + " + " + b + "*" + t);
}

printBezout(237,13)
printBezout(13,237)