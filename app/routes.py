
from flask import Blueprint, flash, redirect, render_template, request, jsonify

from app.forms import AddCupcakeForm
from .models import Cupcake, db

rts = Blueprint('rts', __name__)

@rts.route("/", methods=['POST', 'GET'])
def home():

    form = AddCupcakeForm()
    if form.validate_on_submit():
        flavor = form.flavor.data
        size = form.size.data
        rating = form.rating.data
        image = form.image.data
        new_cupcake = Cupcake(flavor=flavor,size=size,rating=rating,image=image)
        db.session.add(new_cupcake)
        db.session.commit()
        flash('Cupcake added!')
        return redirect('/')
    else:
        return render_template('home.html', form=form)

@rts.route("/api/cupcakes")
def get_cupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    json_cupcakes = jsonify(cupcakes=cupcakes)
    return json_cupcakes

@rts.route('/api/cupcakes/<cupcake_id>')
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@rts.route('/api/cupcakes', methods=['POST'])
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

@rts.route('/api/cupcakes/<cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)  
    print(request.json)
    print(type(request.json))
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    return jsonify(message=f"updated Cupcake {cupcake_id}")

@rts.route('/api/cupcakes/<cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message=f"deleted Cupcake {cupcake_id}")