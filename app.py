from flask import Flask, render_template,request,jsonify


app = Flask("__name__")


@app.route('/')
def home():
    
    return "welcome to the home page"



@app.route('/cal' , methods=['GET' , 'POST'])

def math_operations():
    
    if request.method == "GET":
        
        return render_template('index.html')
    else:
        operation = request.form['operation'].lower()
        number1 = request.form['number1']
        number2 = request.form['number2']
    
        if operation == "add":
        
            result = int(number1) + int(number2)
            syl = "+"
        
        
        
        elif operation == "multiplication":
        
            result = int(number1) *  int(number2)
            syl ="*"
      
        
        
        elif operation == "division":
        
            result = int(number1)/ int(number2)
            
            syl = "/"
        
     
        
        elif operation =="substraction":
        
           result =int(number1) -  int(number2)
           syl ="-"
       
        
        else:
        
            return "please select the  correct operation"
    
    
    return render_template('index.html' ,solution = result , fnumber = number1 , snumber = number2 , opera = syl)



if __name__ == '__main__':
    
    app.run(debug=True)


