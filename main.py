class Hotel:
    count = 0

    def __init__(self, name='', visitor_of_year=0, number_of_rooms=0):
        self.name = name
        self.visitor = visitor_of_year
        self.number = number_of_rooms
        Hotel.count = Hotel.count+1

    def __str__(self):
        return f"name:{self.name} visitor:{self.visitor} number:{self.number}"

    def __del__(self):
        print("викликаэмо деструктор")

    @staticmethod
    def staticmethod():
        return Hotel.count


Lisha_1 = Hotel("Lisha_1", 10, 10)
Lisha_2 = Hotel("Lisha_2", 6, 7)
Lisha_3 = Hotel("Lisha_3", 15, 15)
Lisha_4 = Hotel("Lisha_4", 11, 12)

print(Lisha_1, Lisha_2, Lisha_3, Lisha_4)

print(f"Count={Hotel.getcount}")

