from flask import Blueprint, request, jsonify
from .image_processing import preprocess_image, recognize_text
from .database import get_db_connection
from datetime import datetime

bp = Blueprint("routes", __name__)

@bp.route('/upload', methods=['POST'])
def upload_and_process():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image'].read()
    try:
        processed_image = preprocess_image(image)
        consumption = recognize_text(processed_image)

        if not consumption:
            return jsonify({"error": "Failed to recognize consumption"}), 400

        timestamp = datetime.now()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO meter_readings (timestamp, day_readings)
            VALUES (%s, %s)
        """, (timestamp, consumption))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"status": "success", "consumption": consumption}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
