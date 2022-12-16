from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
DB_NAME="database.db"

# itemname
# brandname
# price
# itemtype
# Quantityadded

class Item(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    itemname=db.Column(db.String(100))
    brandname=db.Column(db.String(100))
    price=db.Column(db.Integer)
    itemtype=db.Column(db.String(100))
    quantityAdded=db.Column(db.Integer)

app=Flask(__name__)
app.config['SECRET_KEY'] = "example123"
app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/additem',methods=['GET','POST'])
def additem():
    if request.method == "POST":
        itemname = request.form.get('ItemName')
        brandname = request.form.get('BrandName')
        price = request.form.get('Price')
        itemtype = request.form.get('ItemType')
        quantityAdded = request.form.get('Quantityadded')
        new_item= Item(itemname=itemname, brandname=brandname, price=price, itemtype=itemtype, quantityAdded=quantityAdded)
        db.session.add(new_item)
        db.session.commit()
        return redirect('/viewitems')
    return render_template("additem.html")

@app.route('/viewitems',methods=['GET'])
def view():
    items = Item.query.all()
    return render_template("viewitems.html", items=items)

@app.route('/', methods=["GET"])
def slash():
    return redirect('/viewitems')

if __name__=="__main__":
    app.run(debug=True)