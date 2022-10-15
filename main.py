# app.py
from flask import Flask, render_template, Response, request  # importing the render_template function

app = Flask(__name__)
# home route
@app.route("/",  methods=['POST', 'GET'])
def hello():
    data = request.data
    print(data)
    if (data == b'hello World!'):
        print('Recieved from client: {}'.format(request.data))
        print(Response('We recieved something…dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'))
        return render_template('index.html')
    else:
        print("awww man")
        return render_template('error.html')


app.run(debug = True) 