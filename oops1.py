#class definition 

class Employee:
    def __init__(self):
        self.id=1
        self.name = "Bipin Ghimire"
        self.salary = "12345"

    def tours(self, place):
        print(f"He can go to {place} ")

# creating an object

sam = Employee()

# print(sam.id)
# print(sam.salary)

sam.tours("Pokhara")

print(type(sam))