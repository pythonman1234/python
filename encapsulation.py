class Person:
    def __init__(self, name, age, _address, __phone):
        self.name = name
        self.age = age
        self._address = _address  # protected
        self.__phone = __phone  # private

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Address:{self._address}")
        print(f"Phone:{self.__phone}")


Person = Person("Pythonman", 24, "123-KingCity", "999630301")

print(f"Name:{Person.name}")
print(f"Age:{Person.age}")

print(f"Address:{Person._address}")
print(f"Phone:{Person.__phone}")

Person.display_info()
