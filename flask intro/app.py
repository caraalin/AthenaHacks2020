from flask import Flask, Blueprint, render_template, url_for, request

page = Blueprint('page', __name__, template_folder='templates')
app = Flask(__name__)
app.register_blueprint(page)

feels = []
assignments = []

@app.route('/', methods=["GET"])
def index():
    return render_template('inputs.html')

@app.route('/inputs', methods=["GET"])
def inputs():
    return render_template('inputs.html')

#@app.route('/calendar', methods=["GET"])
#def calendar():
#    return render_template('calendar.html')

@app.route('/addfeel', methods = ['POST', 'GET'])
def addfeel():
    feel = request.form["feel"]
    feels.append(feel)
    print(feels)
    return render_template('inputs.html', feel=feel)

@app.route('/addassign', methods = ['POST', 'GET'])
def addassign():
    assigns = []
    name = request.form["aname"]
    assigns.append(name)
    workload = request.form["aworkload"]
    assigns.append(workload)
    date = request.form["adate"]
    assigns.append(date)
    assignments.append(assigns)
    print(assignments)
    return render_template('inputs.html', name=name, workload=workload, date=date)

if __name__ == '__main__':
    app.run(debug=True)