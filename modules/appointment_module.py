from database import get_db_connection

def book_appointment(data):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO appointments (patient_id, doctor_id, appointment_date, status)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(query,(
        data["patient_id"],
        data["doctor_id"],
        data["appointment_date"],
        "scheduled"
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Appointment booked successfully"}