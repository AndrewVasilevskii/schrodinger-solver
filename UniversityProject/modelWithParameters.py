import json
class ModelWithParameters:

    def __init__(self):
        self.R = None
        self.d = None
        self.a = None
        self.b = None
        self.E1 = None
        self.E2 = None
        self.E3 = None
        self.tox = None
        self.z0 = None
        self.z1 = None
        self.z2 = None
        self.F0 = None
        self.F1 = None
        self.F2 = None
        self.FJ = None

    @property
    def modelParameters(self):
        return {key: value for key, value in self.__dict__.items() if value != None}

    def __str__(self):
        return json.dumps({key: value for key, value in self.__dict__.items() if value != None})

    def SetValueFor(self, name, value):
        self.__setattr__(name, value)



# mod = ModelWithParameters()

# print(mod.__setattr__("b", 5))
# print(mod.modelParameters)
