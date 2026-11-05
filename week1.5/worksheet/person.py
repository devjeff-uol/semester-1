# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a Person, given values for name and date of birth
        """
        if not isinstance(name, (str)):
            raise TypeError("Name should be a string")
        
        if not name:
            raise ValueError("Name should not be empty")

        if not isinstance(birth, (date)):
            raise TypeError("Date of birth should be a date object")

        self.name = name
        self.birth = birth
    
    def initials(self):
        """
        Returns the initials of the person's name.
        For example: "Alan John Smith" return "AJS".
        """
        return ''.join([name[0].upper() for name in self.name.split(" ") if name])
    
    def is_birthday(self):
        """
        Returns True if today is the person's birthday
        """
        today = date.today()
        compare = self.birth.replace(today.year)
        return today == compare
