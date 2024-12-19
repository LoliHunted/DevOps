from flask import Flask, request, jsonify
import psycopg2
import time
import logging

app = Flask(__name__)

DB_HOST = 'db'
DB_NAME = 'db'
DB_USER = 'user'
DB_PASSWORD = 'password'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.OperationalError as e:
        logger.error(f"Ошибка подключения к базе данных: {e}")
        raise

@app.route('/items', methods=['GET'])
def get_items():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM item;')
        items = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{'id': item[0], 'name': item[1]} for item in items])
    except Exception as e:
        logger.error(f"Ошибка при получении элементов: {e}")
        return jsonify({'error': 'Ошибка при получении элементов'}), 500

@app.route('/items', methods=['POST'])
def create_item():
    try:
        data = request.json
        name = data['name']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO item (name) VALUES (%s) RETURNING id, name;', (name,))
        new_item = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'id': new_item[0], 'name': new_item[1]}), 201
    except Exception as e:
        logger.error(f"Ошибка при создании элемента: {e}")
        return jsonify({'error': 'Ошибка при создании элемента'}), 500

if __name__ == '__main__':
    time.sleep(12)
    app.run(host='0.0.0.0', port=8080)
