from flask import Flask, render_template, jsonify
import readApple
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def navindex():
    return render_template('index.html')

@app.route('/apple.html')
def apple():
    return render_template('apple.html')

@app.route('/dowjones.html')
def dowjones():
    return render_template('dowjones.html')

@app.route('/facebook.html')
def facebook():
    return render_template('facebook.html')

@app.route('/google.html')
def google():
    return render_template('google.html')
    
@app.route('/tesla.html')
def tesla():
    return render_template('tesla.html')
    
@app.route('/uber.html')
def uber():
    return render_template('uber.html')
    

# script calls
@app.route('/apple/getApple')
def getApple():
    appleData = readApple.main()

app.run()