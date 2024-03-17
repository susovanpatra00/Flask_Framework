### Integrating HTML with Flask Web Framework with HTTP Verbs (GET & POST)


from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')   
def success(score):   
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"        
    return render_template('result.html',result = res)



@app.route('/fail/<int:score>')    
def fail(score):                
    res = ""
    if score < 50:
        res = "FAIL"
    else:
        res = "PASS"        
    return render_template('result.html',result = res)

## Result Checker
@app.route('/results/<int:marks>')    
def results(marks):
    result = ""                
    if marks<50:
        result =  "fail"
    else:
        result =  "success"

    # return result
    return redirect(url_for(result, score = marks))


## Result Checker HTML Page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + c + datascience)/4
    
    result = ""
    if total_score >=50:
        res = "success"
    else:
        res = "fail"

    return redirect(url_for(res, score = total_score))










if __name__ == '__main__':
    app.run(debug=True)




## 'render_template' - It will help us to render HTML pages. When using render_template we
##                      need to have the folder named 'templates' inside which te html file
##                      must be stored which we want to use.
    
## 'request' - It will help in reading the Posted values.