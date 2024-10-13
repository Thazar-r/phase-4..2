from flask import Blueprint, jsonify, request
from models import db, Guest, Episode, Appearance

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': ep.id, 'date': ep.date} for ep in episodes])

@api_blueprint.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{'id': guest.id, 'name': guest.name, 'occupation': guest.occupation} for guest in guests])

@api_blueprint.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.json
    appearance = Appearance(rating=data['rating'], episode_id=data['episode_id'], guest_id=data['guest_id'])
    try:
        appearance.validate()
        db.session.add(appearance)
        db.session.commit()
        return jsonify({
            'id': appearance.id,
            'rating': appearance.rating,
            'guest_id': appearance.guest_id,
            'episode_id': appearance.episode_id
        }), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
