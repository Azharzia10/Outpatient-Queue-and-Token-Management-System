from database import get_db_connection

# Register patient

def register_patient(data):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO patients (first_name, middle_name, last_name, gender, phone)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(
        data["first_name"],
        data["middle_name"],
        data["last_name"],
        data["gender"],
        data["phone"]
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return True

# Get all patients

def get_all_patients():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    cursor.close()
    conn.close()

    return patients