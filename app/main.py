from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import logging

app = Flask(__name__)
app.config['DB_USER'] = os.getenv('DB_USER', 'default_user')
app.config['DB_PASSWORD'] = os.getenv('DB_PASSWORD', 'default_password')
app.config['DB_NAME'] = os.getenv('DB_NAME', 'default_db')
app.config['DB_HOST'] = os.getenv('DB_HOST', 'localhost')
app.config['DB_PORT'] = os.getenv('DB_PORT', '5432')

app.logger.setLevel(logging.INFO)

app.logger.info(f"DB_HOST: {app.config['DB_HOST']}")
app.logger.info(f"DB_USER: {app.config['DB_USER']}")

'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:80/{os.getenv("DB_NAME")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id, 'name': new_item.name}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=80)
'''
