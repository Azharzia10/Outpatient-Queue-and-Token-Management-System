from flask import Blueprint, request, jsonify
from modules.doctor_module import add_doctor, get_doctors

doctor_bp = Blueprint("doctors", __name__)

@doctor_bp.route("/doctors", methods=["POST"])
def create_doctor():

    data = request.json
    result = add_doctor(data)

    return jsonify(result)


@doctor_bp.route("/doctors", methods=["GET"])
def fetch_doctors():

    doctors = get_doctors()

    return jsonify(doctors)