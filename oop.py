class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender
        

    def introduce(self):
        print(f"hello,my name is{self.name},i am {self.age}years old and i am {self.gender}.")

        person=Person("lucky",19,"female")   

        person.introduce()