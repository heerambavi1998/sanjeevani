#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn




class Patients(Resource):
    """It contain all the api carryign the activity with aand specific patient"""

    def get(self):
        """Api to retive all the patient from the database"""

        patients = conn.execute("SELECT * FROM patient  ORDER BY pat_date DESC").fetchall()
        return patients



    def post(self):
        """api to add the patient in the database"""

        patientInput = request.get_json(force=True)
        print(patientInput)
        pat_first_name=patientInput['pat_first_name']
        pat_last_name = patientInput['pat_last_name']

        patientInput['pat_id']=conn.execute('''INSERT INTO patient(pat_first_name,pat_last_name)
            VALUES(?,?)''', (pat_first_name, pat_last_name)).lastrowid
        conn.commit()
        return patientInput

class Patient(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self,id):
        """api to retrive details of the patient by it id"""

        patient = conn.execute("SELECT * FROM patient WHERE pat_id=?",(id,)).fetchall()
        return patient

    def delete(self,id):
        """api to delete the patiend by its id"""

        conn.execute("DELETE FROM patient WHERE pat_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the patient by it id"""

        patientInput = request.get_json(force=True)
        print(patientInput)
        pat_first_name = patientInput['pat_first_name']
        pat_last_name = patientInput['pat_last_name']
        l = []
        for i in range(1,7):
            if str(i) in patientInput:
                l.append('1')
            else:
                l.append('0')

        conn.execute("UPDATE patient SET pat_first_name=?,pat_last_name=?,pat_eye=?,pat_gynaec=?,pat_dent=?,pat_skin=?,\
                     pat_ortho=?,pat_ent=? WHERE pat_id=?",
                     (pat_first_name, pat_last_name,l,id))



        appointment['app_id'] = conn.execute('''INSERT INTO appointment(pat_id,doc_id)
                    VALUES(?,?)''', (pat_id, doc_id)).lastrowid
        conn.commit()
        return patientInput