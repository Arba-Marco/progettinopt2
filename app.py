from flask import Flask, url_for, redirect, request ,render_template

 #inizializza l'app Flask
app = Flask(__name__)

#rotta principale

lista =[]


#avvio dell'app Flask

@app.route('/')
def home():
   return render_template('index.html',lista=lista)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
   elemento = request.form['elemento']
   if elemento:
      lista.append(elemento)
   return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
   if 0 <= indice < len(lista):
      lista.pop(indice)
   return redirect(url_for('home'))

@app.route('/svuota_lista', methods=['POST'])
def svuota_lista():
   lista.clear()
   return redirect(url_for('home'))

if __name__ == '__main__':
 app.run(debug=True)    
    