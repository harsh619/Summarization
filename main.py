from flask import Flask,redirect,url_for,render_template,request
from summa import summarizer

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<summarized_text>')
def success(summarized_text):

    return render_template('result.html',result=summarized_text)



@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        text=request.form['summarize']
        vol=float(request.form['vol'])

        
        # print(text)
        # print("\n\n")
        # print(vol)
        # print("\n\n")
        res=summarizer.summarize(text,ratio=vol/100)
        
        # print("Resolved Doc\n")
        # print(res)
    
    return redirect(url_for('success',summarized_text=res))



if __name__=='__main__':
    app.run(debug=True)