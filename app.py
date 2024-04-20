from flask import Flask,render_template,request
import pickle

app=Flask(__name__)  #create falsk application name app

#create home page
@app.route('/')
def hello():
    # return 'hello!'
    return render_template('index.html')

# @app.route('/prediction')
@app.route('/prediction',methods=['GET','POST']) #adding POST & GET method in the prediction page (by def. GET method only)
def predict():
    # return 'this is the result page'
    if request.method=='POST':
        height=request.form['height']  #extract height value from the form in req to variable height
        print(height)     #print the value in terminal
        model=pickle.load(open('model.pkl','rb'))   #laod the model pickle
        weight=model.predict([[float(height)]]) #covert the height value from string to float
        print(weight[0])  #print the value only
        
    return render_template('prediction.html',weight=weight[0]) #paasing the weight value into weight variable

if __name__=='__main__':
    app.run()