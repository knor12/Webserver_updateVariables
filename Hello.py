from flask import Flask, render_template, request, jsonify
import threading
from variablesWorker import * 
# Example variable value

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
   if request.method == 'POST':
   
      return render_template('layout.html', name = 'nk')
   if   request.method == 'GET':
      return  render_template('layout.html', name = 'nk')
   

@app.route("/get_variable1")
def get_variable1():
    print("route variable_value1= "+str(getVariable("variable1")))
    return jsonify(getVariable("variable1"))

@app.route("/get_variable2")
def get_variable2():
    print("route variable_value2= "+str(getVariable("variable2")))
    return jsonify(getVariable("variable2"))

@app.route("/get_variable3")
def get_variable3():
    print("route variable_value3= "+str(getVariable("variable3")))
    return jsonify(getVariable("variable3"))     

if __name__ == '__main__':

   #launch thread for updating vaiables
   x = threading.Thread(target=UpdateVariable, args=(1,))
   x.start()


   app.debug = True
   app.run()