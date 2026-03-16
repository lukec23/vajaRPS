from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("1naloga.html")




app.run(debug=True)




"https://hackmd.io/@lukac/flaskPre" #tuki so vaje 