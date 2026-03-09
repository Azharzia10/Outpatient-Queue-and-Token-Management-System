from database import get_db_connection

def add_doctor(data):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO doctors (first_name, middle_name, last_name, specialization)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(query,(
        data["first_name"],
        data["middle_name"],
        data["last_name"],
        data["specialization"]
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