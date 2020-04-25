class Attribute:
    def __init__(self,name,value):
        self.name = Attribute.f(name)
        self.value = value

    def get_name(self):
        return self.name
    def get_value(self):
        return self.value