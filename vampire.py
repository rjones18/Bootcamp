class Vampire:
  coven = []
  
  def __init__(self, name, age, in_coffin=True, drank_blood_today=True):
    self.name = name
    self.age = age
    self.in_coffin = in_coffin
    self.drank_blood_today = drank_blood_today
    __class__.coven.append(self)

  def drink_blood(self):
    self.drank_blood_today = True
  
  def sunset(self):
      for vamp in self.coven:
        vamp.drank_blood_today = False
        vamp.in_coffin = False
      

          

  def go_home(self):
    self.in_coffin = True


  @classmethod 
  def sunrise(cls):
    remaining_vampires = [] 
    for vamp in cls.coven:
      if vamp.in_coffin and vamp.drank_blood_today:
        remaining_vampires.append(vamp)
    cls.coven = remaining_vampires
        


  
def main():
  riley = Vampire('Riley', 25)
  alice = Vampire('Alice', 24)
  jasper = Vampire('Jasper', 23)
  renesmee = Vampire('Renesmee', 25)
  marcus = Vampire('Marcus', 28)
  zafrina = Vampire('Zafrina', 49)
  demetri = Vampire('Demetri', 28)

  print('Coven at the beginning:')
  for vampire in Vampire.coven:
    print(vampire.name)

  Vampire.sunset(vampire)
  riley.drink_blood()
  riley.go_home()
  jasper.drink_blood()
  renesmee.drink_blood()
  renesmee.go_home()
  marcus.go_home()
  Vampire.sunrise() # Should remove all vampires except 'Riley' and 'Renesmee'

  print('Coven at the end:')
  for vampire in Vampire.coven:
    print(vampire.name) #--> 'Riley', 'Renesmee'

main()
