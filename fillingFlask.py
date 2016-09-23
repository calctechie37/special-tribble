from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return "Welcome to Software Dev!"

@app.route('/hi')
def hi():
    return "Hello World"

@app.route('/bye')
def bye():
    return "Bye"

@app.route('/occupation')
def occupation():
    from occupations import readFile, getOccupation, getOccupationLink
    occupationDict = readFile()
    return render_template('occupation.html', occupationData=occupationDict, randomOccupation=getOccupation(), occupationLink=getOccupationLink())

if __name__ == '__main__':
    app.run()
