# Referred method with bounded and unbounded invocation
class Boundary:

  def __init__(self, country):
    self.country = country
    pass

  def printMsg(self, msg="Freedom"):
    print(self.country, "Recieved", msg)
    pass


bd = Boundary("Bangladesh")
india = Boundary("India")

func = Boundary.printMsg
func(bd, " Freedom in 1971")
func(india, " Freedom in 1875")
