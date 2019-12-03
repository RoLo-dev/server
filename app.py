from flask import Flask, render_template, redirect, request, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/play')
def home():
    return render_template("level_1.html")

@app.route('/play/<num>')
def blue_box(num):
    return render_template('level_2.html', num_times=int(num))

@app.route('/play/<num>/<color>')
def random_box(num, color):
    random_color = color
    return render_template('level_3.html', num_times=int(num), random_color = random_color)

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/play/<number_of_boxes>/<color_change>")
# def box_color(number_of_boxes,color_change):
#     repeat = (int(number_of_boxes))
#     colorChange = color_change
#     return render_template('playground3.html', repeat = repeat, colorChange = colorChange )