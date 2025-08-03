class BaseChai:
    def __init__(self,type_):
        self.type=type_
    def prepare(self):
        print( f"Preparing {self.type} chai ...."  )

class MassalaChai(BaseChai):
    def addSpices(self):
        print("adding spices")

class ChaiShop:
    chai_cls=BaseChai
    def __init__(self):
        self.chai=self.chai_cls("Regular")
