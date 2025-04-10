from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    valores1 = request.form.getlist('valor1[]')
    valores2 = request.form.getlist('valor2[]')
    modulos = request.form.getlist('modulo[]')

    valoresParaCalculo = []
    for i in range(len(valores1)):
        lista = []
        
        lista.append(valores1[i])
        lista.append(valores2[i])
        lista.append(modulos[i])
        
        valoresParaCalculo.append(lista)
        lista = []
    
    print(valoresParaCalculo)
    
    return f"{valoresParaCalculo}"

if __name__ == '__main__':
    app.run(debug=True)