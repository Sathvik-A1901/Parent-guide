from flask import Flask,render_template,request,jsonify
import LangChain
import config


app=Flask(__name__)



@app.route("/",methods=['POST','GET'])
def home():

    if request.method=='POST':
        query=request.form['prompt']

        res={}
        res['answer']=LangChain.convo(query)

        return jsonify(res),200
    
    return render_template('index.html')
    



if __name__=='__main__':
    app.run(debug=True)
