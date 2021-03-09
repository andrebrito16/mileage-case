from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

carros= [
    { 
        'modelo': 'HB20',
        'velocidade_max': '180.0',
        'motor': '1.6',
        'marca': 'Hyundai'
    },

    { 
        'modelo': 'XC60',
        'velocidade_max': '175.0',
        'motor': '2.0',
        'marca': 'Volvo'
    },

    { 
        'modelo': 'Compass',
        'velocidade_max': '195.0',
        'motor': '2.0',
        'marca': 'Jeep'
    },

    { 
        'modelo': 'Fox',
        'velocidade_max': '160.0',
        'motor': '1.6',
        'marca': 'Volkswagen'
    },

    { 
        'modelo': 'Evoque',
        'velocidade_max': '185.0',
        'motor': '2.0',
        'marca': 'Land Rover'
    },

    { 
        'modelo': 'Polo',
        'velocidade_max': '195.0',
        'motor': '1.6',
        'marca': 'Volkswagen'
    },

]

#Variáveis dos gráficos


# Acessar informações de todos os carros
@app.route('/api/info')
def index_api():
    return jsonify(carros)

# Filtrar os carros pelo motor
@app.route('/api/motor', methods=["GET"])
def query_engine():
    req = request.form
    engine = request.args.get("tipo")
    print(engine)
    carros_motor = []
    for carro in carros:
        if carro['motor'] == engine:
            carros_motor.append(carro)
    
    if carros_motor == []:
        return render_template('index.html', carros=carros)

    
    return render_template('index.html', carros=carros_motor)


# Adicionar um carro
@app.route('/api/add', methods=["POST"])
def add():
    req = request.form
    modelo = req.get("model")
    velocidade_max = req.get("vmax")
    motor = req.get("engine")
    marca = req.get("marca")

    if modelo == "" or velocidade_max == "" or motor == "" or marca == "":
        return render_template('error.html')
    else:
        carros.append({
            'modelo': modelo,
            'velocidade_max': velocidade_max,
            'motor': motor,
            'marca': marca
        },)

        return render_template('index.html', carros=carros)

    
# Alterar o valor de motor de algum dos modelos
@app.route('/api/change', methods=["POST"])
def change():
    req = request.form

    modelo = req.get("model")
    novo_motor = req.get("engine")
    for carro in carros:
        if carro['modelo'] == modelo:
            carro['motor'] = novo_motor
            return render_template('index.html', carros=carros)

    return render_template('error.html')


# Deletar um dos modelos
@app.route('/api/delete', methods=["post"])
def delete():
    req = request.form
    modelo = req.get("model")
    for carro in carros:
        if carro['modelo'] == modelo:
            carros.remove(carro)
            return render_template('index.html', carros=carros)

    return render_template('error.html')

# Index html
@app.route('/')
def index():
    index_api()   
    return render_template('index.html', carros=carros)

# Gráficos
@app.route('/charts')
def charts():
    labels = [carro["modelo"] for carro in carros]
    values = [carro["velocidade_max"] for carro in carros]
    return render_template('charts.html', labels=labels, values=values)



if __name__ == '__main__': 
    app.run(debug=True)