class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_info(self):
        print(f"Name = {self.name} age={self.age}")

    @staticmethod
    def is_valid_age(num):
        if (num>0):
            return True
        else:
            return False

print(employee.is_valid_age(-1))

 