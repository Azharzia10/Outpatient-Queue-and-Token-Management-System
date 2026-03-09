from flask import Blueprint, request, jsonify

from modules.admin_module import (
    admin_login,
    add_doctor,
    get_doctors,
    delete_doctor,
    get_patients,
    get_appointments
)

admin_bp = Blueprint("admin_bp", __name__)


# ADMIN LOGIN
@admin_bp.route("/admin/login", methods=["POST"])
def login():

    data = request.json

    admin = admin_login(
        data.get("username"),
        data.get("password")
    )

    if admin:
        return jsonify({
            "message": "Login successful",
            "admin": admin
        })

    return jsonify({
        "message": "Invalid username or password"
    }), 401


# ADD DOCTOR
@admin_bp.route("/admin/add_doctor", methods=["POST"])
def create_doctor():

    data = request.json

    result = add_doctor(data)

    return jsonify(result)


# VIEW DOCTORS
@admin_bp.route("/admin/doctors", methods=["GET"])
def view_doctors():

    doctors = get_doctors()

    return jsonify({
        "doctors": doctors
    })


# DELETE DOCTOR
@admin_bp.route("/admin/delete_doctor/<int:doctor_id>", methods=["DELETE"])
def remove_doctor(doctor_id):

    result = delete_doctor(doctor_id)

    return jsonify(result)


# VIEW PATIENTS
@admin_bp.route("/admin/patients", methods=["GET"])
def view_all_patients():

    patients = get_patients()

    return jsonify({
        "patients": patients
    })


# VIEW APPOINTMENTS
@admin_bp.route("/admin/appointments", methods=["GET"])
def view_all_appointments():

    appointments = get_appointments()

    return jsonify({
        "appointments": appointments
    })