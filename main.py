class Hotel():
    static = 0

    def __init__(self, name='', visitor_of_year=0, number_of_rooms=0):
        self.name = name
        self.visitor = visitor_of_year
        self.number = number_of_rooms

    def __str__(self):
        return f"name:{self.name} visitor:{self.visitor} number:{self.number}"

    def __del__(self):
        print("викликаэмо деструктор")

    @staticmethod
    def staticmethod(static):
        return f"static={static}"


Lisha_1=Hotel("Lisha_1",10,10)
print(Lisha_1.__str__())

Lisha_2=Hotel("Lisha_2",16,17)
print(Lisha_2.__str__())

Lisha_3=Hotel("Lisha_3",15,15)
print(Lisha_3.__str__())

Lisha_4=Hotel("Lisha_4",11,12)
print(Lisha_4.__str__())

