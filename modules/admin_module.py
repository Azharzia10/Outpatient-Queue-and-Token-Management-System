from database import get_db_connection


def admin_login(username, password):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM admin WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    admin = cursor.fetchone()

    cursor.close()
    conn.close()

    return admin


def add_doctor(data):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO doctors
    (first_name, middle_name, last_name, specialization, phone)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(
        data.get("first_name"),
        data.get("middle_name"),
        data.get("last_name"),
        data.get("specialization"),
        data.get("phone")
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Doctor added successfully"}


def get_doctors():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM doctors")

    doctors = cursor.fetchall()

    cursor.close()
    conn.close()

    return doctors


def delete_doctor(doctor_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM doctors WHERE doctor_id=%s"

    cursor.execute(query,(doctor_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Doctor deleted successfully"}


def get_patients():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    cursor.close()
    conn.close()

    return patients


def get_appointments():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM appointments")

    appointments = cursor.fetchall()

    cursor.close()
    conn.close()

    return appointments