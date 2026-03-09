from flask import Blueprint, request, jsonify
from modules.patient_module import register_patient, get_all_patients

patient_bp = Blueprint("patients", __name__)


# Register patient
@patient_bp.route("/patients", methods=["POST"])
def register_patient_route():

    data = request.json

    register_patient(data)

    return jsonify({"message":"Patient registered successfully"})


# Get all patients
@patient_bp.route("/patients", methods=["GET"])
def get_patients():

    patients = get_all_patients()

    return jsonify(patients)