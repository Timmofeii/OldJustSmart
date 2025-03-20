import person
from employee import Employee

pers1 = person.Person("Jojo")
empl = Employee("Worker")
print("{}, {}".format(pers1.get_name(),pers1.isEmployee()))
print( "{}, {}".format(empl.isEmployee(), empl.get_name()))
