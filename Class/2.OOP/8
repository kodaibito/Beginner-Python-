from abc import ABC, abstractmethod

# Abstract Class: Ortak özellikleri tanımlar, tek başına kullanılamaz
class Person(ABC):
    def __init__(self, name, age, id_number):
        self.name = name      # isim
        self.age = age        # yaş
        self.id_number = id_number  # kimlik numarası

    @abstractmethod
    def get_info(self):       # herkesin kendine göre dolduracağı metod
        pass

# Abstract Class: Tıbbi hizmetlerin şablonu
class MedicalService(ABC):
    def __init__(self, service_name, duration, cost):
        self.service_name = service_name  # hizmet adı
        self.duration = duration          # süre
        self.cost = cost                  # maliyet

    @abstractmethod
    def perform_service(self):            # her hizmetin kendine göre uygulaması olacak
        pass


# Concrete Class: Doktor
class Doctor(Person):
    def __init__(self, name, age, id_number, specialty, experience, department):
        super().__init__(name, age, id_number)  # Person'dan miras alıyor
        self.specialty = specialty              # uzmanlık alanı
        self.experience = experience            # deneyim yılı
        self.department = department            # bölüm

    def get_info(self):
        return f"Dr. {self.name}, {self.specialty}, {self.experience} years experience"

    def diagnose(self, patient):
        return f"{self.name} diagnoses {patient.condition}"


# Concrete Class: Hemşire
class Nurse(Person):
    def __init__(self, name, age, id_number, level, assigned_doctor, shift):
        super().__init__(name, age, id_number)
        self.level = level              # hemşire seviyesi
        self.assigned_doctor = assigned_doctor  # bağlı olduğu doktor
        self.shift = shift              # vardiya

    def get_info(self):
        return f"Nurse {self.name}, Level {self.level}"

    def assist(self, doctor):
        return f"{self.name} assists Dr. {doctor.name}"


# Concrete Class: Hasta
class Patient(Person):
    def __init__(self, name, age, id_number, condition, room, insurance):
        super().__init__(name, age, id_number)
        self.condition = condition      # hastalık durumu
        self.room = room                # oda numarası
        self.insurance = insurance      # sigorta bilgisi

    def get_info(self):
        return f"Patient {self.name}, Condition: {self.condition}"

    def request_help(self):
        return f"{self.name} requests help"


# Concrete Class: Ameliyat
class Surgery(MedicalService):
    def __init__(self, service_name, duration, cost, type, risk_level, surgeon):
        super().__init__(service_name, duration, cost)
        self.type = type                # ameliyat türü
        self.risk_level = risk_level    # risk seviyesi
        self.surgeon = surgeon          # cerrah

    def perform_service(self):
        return f"Surgery '{self.service_name}' performed by {self.surgeon}"

    def schedule(self):
        return f"Surgery scheduled for {self.duration} hours"


# Concrete Class: Terapi
class Therapy(MedicalService):
    def __init__(self, service_name, duration, cost, method, therapist, frequency):
        super().__init__(service_name, duration, cost)
        self.method = method            # terapi yöntemi
        self.therapist = therapist      # terapist adı
        self.frequency = frequency      # sıklık

    def perform_service(self):
        return f"Therapy '{self.service_name}' with {self.therapist}"

    def reschedule(self):
        return f"Therapy rescheduled to {self.frequency} times/week"


# Multiple Inheritance: Hem hasta hem hizmet → Acil vaka
class EmergencyCase(Patient, MedicalService):
    def __init__(self, name, age, id_number, condition, room, insurance,
                 service_name, duration, cost, severity, ambulance, triage_level):
        Patient.__init__(self, name, age, id_number, condition, room, insurance)
        MedicalService.__init__(self, service_name, duration, cost)
        self.severity = severity        # aciliyet seviyesi
        self.ambulance = ambulance      # ambulans bilgisi
        self.triage_level = triage_level # triaj seviyesi

    def get_info(self):
        return f"Emergency Patient {self.name}, Severity: {self.severity}"

    def perform_service(self):
        return f"Emergency protocol '{self.service_name}' applied with triage level {self.triage_level}"


# Polymorphism: Aynı metod farklı sınıflarda farklı çalışıyor
def show_service(service: MedicalService):
    print(service.perform_service())


# Örnek kullanım
surgery = Surgery("Appendectomy", 2, 5000, "General", "High", "Dr. Smith")
therapy = Therapy("Physiotherapy", 30, 1500, "Manual", "Therapist Jane", 3)

show_service(surgery)   # Surgery sınıfındaki perform_service çalışır
show_service(therapy)   # Therapy sınıfındaki perform_service çalışır