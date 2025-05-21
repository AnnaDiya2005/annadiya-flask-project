from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
   fruits=["apple","orange","mango"]
   return render_template("index.html",items=fruits)
    
@app.route('/users')
def users():
    users=["anna","hanna","neha"]
    return render_template("users.html",users=users)
if __name__ =='__main__':
  app.run(debug = True)