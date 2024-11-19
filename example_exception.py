import sys


def checkEnergy(energy):
  if energy < 70:
    raise Exception("Not enough to fuel a system")


def assertEnergy():
  pass


try:
  checkEnergy(50)
except Exception as excp:
  print("Error Recieved:", excp)
else:
  print("Energy is enough to fly")
finally:
  print("Why do we need elese at all ?")
