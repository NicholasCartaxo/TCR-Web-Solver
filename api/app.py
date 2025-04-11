from flask import Flask, render_template, request
from calculator import solveTCR

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    valores1 = request.form.getlist('valor1[]')
    valores2 = request.form.getlist('valor2[]')
    modulos = request.form.getlist('modulo[]')

    for i in range(len(valores1)):
        if not valores1[i].isnumeric() or not valores2[i].isnumeric() or not modulos[i].isnumeric():
            return "Entrada(s) não numérica(s)"


    valoresParaCalculo = [[int(valores1[i]),int(valores2[i]),int(modulos[i])] for i in range(len(valores1))]

    mTotal,x,resultados = solveTCR(valoresParaCalculo)  

    s = "".join([f"c{i+1} = {resultados[i][0]}; N{i+1} = {resultados[i][1]}; d{i+1} = {resultados[i][2]}<br>" for i in range(len(resultados))])
    resultadoFormatado = f"x = {x} mod {mTotal}<br>" + s

    return resultadoFormatado

if __name__ == '__main__':
    app.run(debug=True)