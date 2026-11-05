from person import Person
from rect import Rectangle
from datetime import date

person = Person("Jeffrey Chan", 123)
print(person.initials())
print(person.is_birthday())

rect = Rectangle("", 20)
print(rect.is_square(), rect.area(), rect.perimeter())