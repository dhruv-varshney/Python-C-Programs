class Person:
      department= input("enter the department")
      def set_name(self,new_name):
          self.name = new_name
      def set_location(self,new_location):
          self.location = new_location
person = Person()
a = input("enter a name")
b = input("enter your location")
person.set_name(a)
person.set_location(b)
print('{} live in {} and works in {}'.format(person.name,person.location,person.department))
