# Comp9 NPC Computers

import random

letters=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,')

class NPC:
  def __init__(self,name,files=[]):
    self.name=name
    self.files={}
    for f in files:
      self.files[f[0]]=f[1]
    for i in range(random.randint(0,10)):
      data=''
      name=''
      for j in range(random.randint(10,100)):
        data+=random.choose(letters)
      for j in range(random.randint(1,10)):
        name+=random.choose(letters)
      self.files[name]=data
