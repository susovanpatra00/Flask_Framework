### Building URL dynamically
### Flask Variable Rules and URL Building

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my Web Application"


@app.route('/success/<int:score>')   ## here the score will be passed as a parameter and will 
def success(score):                 ## be in INT format Syntax : /<variable_type:variable_name>
    return "The person has passed the examination and the score is " + str(score)



@app.route('/fail/<int:score>')    
def fail(score):                
    return "<html><body><h1> The person has failed the exam </h1></body></html>"


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



if __name__ == '__main__':
    app.run(debug=True)





## 'redirect' - It is used for redirecting to another webpage which already exists.
## 'url_for' - This is used for giving the url and if any parameters in the redirect. 