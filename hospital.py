# Hospital
# You're going to build a hospital with patients in it! Create a hospital class.
# Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?


# Patient:
# Attributes:

# Id: an id number

# Name

# Allergies

# Bed number: should be none by default
# Hospital
# Attributes:

# Patients: an empty array

# Name: hospital name

# Capacity: an integer indicating the maximum number of patients the hospital can hold.
# Methods:

# Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. 
# Return a message either confirming that admission is complete or saying the hospital is full.


class patient(object):
    
    def __init__(self, id_number, name, allergies, bed_number):
        self.id = id_number
        self.name = name 
        self.allergies = allergies
        self.bed_number = bed_number

    def display(self):
        print " "
        print "Id Number:", self.id
        print "Patient Name:", self.name
        print "Allergies:", self.allergies
        print "Bed Number:", self.bed_number
        print " "
        return self

class hospital(object):

    def __init__(self, hospital_name, max_capacity):
        self.patient = [ ]
        self.hospital_name = hospital_name
        self.max_capacity = max_capacity
        self.capacity = 0
    
    def admit(self, add_patient):    
        if self.capacity > self.max_capacity:
            return self
        self.patient.append(add_patient)
        self.capacity += 1
        return self

    def discharge(self, goodbye):
        self.goodbye = goodbye
        self.patient.remove(goodbye)
        return self

    def display(self):
        for x in self.patient:
            x.display()
        return self



patient1 = patient(01, "Jason", "milk", "001")
patient2 = patient(02, "Jose", "Juan", "002")
patient3 = patient(03, "Juan", "Jose", "003")
# patient1.display()
hospital = hospital("Domo Hospital", 10)
hospital.admit(patient1).admit(patient2).admit(patient3).display().discharge(patient2).display()
    
    




