### Jinja2 Template Engine

'''
{%...%}     conditions, for loops
{{   }}     expression to print output
{#...#}     Internal Comments
'''


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
    
    exp = {'score':score,'res':res}
    # return render_template('result_4.html',result = score)
    return render_template('result_4.html',result = exp)



@app.route('/fail/<int:score>')    
def fail(score):                     
    # return render_template('result_4.html',result = score)
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    
    exp = {'score':score,'res':res}
    # return render_template('result_4.html',result = score)
    return render_template('result_4.html',result = exp)

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
