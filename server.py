from flask import Flask, render_template

app = Flask(__name__)


# Level One
@app.route('/play')
def level_one():
    return render_template("index.html", num=3, color="blue")


# Level Two
@app.route('/play/<int:num>')
def level_two(num):
    return render_template("index.html", num=num, color="blue")


#Level 3
@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template("index.html", num=num, color=color)




if __name__=="__main__":
    app.run(debug=True)