from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )
    return conn

@app.route('/points', methods=['GET', 'POST'])
def manage_points():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'GET':
        cursor.execute('SELECT * FROM points')
        points = cursor.fetchall()
        conn.close()
        return jsonify(points)
    
    if request.method == 'POST':
        new_point = request.get_json()
        cursor.execute('INSERT INTO points (adresse, latitude, longitude, status, montant, date) VALUES (%s, %s, %s, %s, %s, %s)',
                       (new_point['adresse'], new_point['latitude'], new_point['longitude'], new_point['status'], new_point['montant'], new_point['date']))
        conn.commit()
        conn.close()
        return '', 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
