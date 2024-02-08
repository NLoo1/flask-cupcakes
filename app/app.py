from flask import jsonify, request, render_template
from .__init__ import create_app
from .models import Cupcake, db

app = create_app()
db.app = app

@app.route("/api/cupcakes")
def get_cupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    json_cupcakes = jsonify(cupcakes=cupcakes)
    return json_cupcakes

@app.route('/api/cupcakes/<cupcake_id>')
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/', methods=['POST'])
def add_cupcake():
    new_cupcake =Cupcake(
        flavor=request.json['flavor'],
        size=request.json['size'],
        rating=request.json['rating'],
        image=request.json['image'],
    )
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)
    

if __name__ == '__main__':
    app.run(debug=True)
