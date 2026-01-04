import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

# Before each request, store the application's path in g
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

# Index route
@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>Python Operations with Flask Routing and Views</h1>
        <h2>The host for this page is {host}</h2>
        <h3>The name of this application is {appname}</h3>
        <h4>The path of this application on the user's device is {g.path}</h4>
    '''
    status_code = 200
    headers = {}
    return make_response(response_body, status_code, headers)

# Print string route
@app.route("/print/<string:param>")
def print_string(param):
    print(param)  # prints to console
    return make_response(param, 200)  # return exactly what test expects

# Count numbers route
@app.route("/count/<int:number>")
def count(number):
    output = ""
    for i in range(number):  # start from 0
        output += f"{i}\n"
    return make_response(output, 200)

# Math operations route
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            return make_response("Cannot divide by zero", 400)
        result = num1 / num2  # always float
        return make_response(str(result), 200)
    elif operation == "%":
        result = num1 % num2
    else:
        return make_response("Invalid operation", 400)

    # Return integer as string if no decimal part
    if result == int(result):
        return make_response(str(int(result)), 200)
    return make_response(str(result), 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
