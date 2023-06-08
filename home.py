from flask import Flask, render_template, request, Markup
import os
app=Flask(__name__)
######################dashboard############################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    title='Exam Authoring Tool-Dashboard'
    if(request.method=='POST'):
        subject=str(request.form['subject'])
        print(subject)
        file_name='C:\Users\Subhanshu\OneDrive\exam authoring\question'+subject+'.txt'
        isexit=os.path.exists(file_name)
        if(isexit==True):
            return render_template('index.html',subject=True)
        else:
            return render_template('index.html',subject=True)

   
if __name__ == "__main__":
    app.run(port=3000)

