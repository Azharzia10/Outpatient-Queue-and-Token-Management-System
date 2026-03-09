from flask import Blueprint, request, jsonify
from modules.appointment_module import book_appointment

appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route("/appointments", methods=["POST"])
def create_appointment():

    data = request.json

    result = book_appointment(data)

    return jsonify(result)