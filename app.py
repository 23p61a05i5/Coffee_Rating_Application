from flask import Flask,render_template,redirect,url_for
from database import connect,init_db
app=Flask(__name__)
@app.get("/")
def index():
    with connect() as c: coffees=c.execute("SELECT * FROM coffees ORDER BY votes DESC,name").fetchall()
    return render_template("index.html",coffees=coffees)
@app.post("/vote/<int:coffee_id>")
def vote(coffee_id):
    with connect() as c: c.execute("UPDATE coffees SET votes=votes+1 WHERE id=?",(coffee_id,))
    return redirect(url_for("index"))
if __name__=="__main__": init_db(); app.run(debug=True)
