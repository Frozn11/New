class GameDev:
  age = 0 
  name = ""
  gameCreating = ""
  gameCreatedit = ['dark souls 1', 'dark souls 2', 'dark souls 3']
  gameCountCreated = 0
  def name_(self):
    print("name:", self.name)

  def age_(self):
      print("age:", self.age)

  def info_(self):
      print("age", self.age,",name:",self.name,",school:",self.gameCreating)

  def finish_Game(self):
      print("Congratulations, the course is finished")
      self.gameCreatedit.append(self.gameCreating)
      self.gameCountCreated += 1

  def GameListCreated(self):
      print("Game count created:", self.gameCountCreated, "\nGame createdit list:", self.gameCreatedit)

  def GameInDev(self):
     print("Game in development", self.gameCreating)

Dev = GameDev()
Dev.name = "МегаМозг"
Dev.gameCreating = "ELDEN RING 2"
Dev.age = 26
Dev.gameCountCreated = 21
# Dev.finish_Game()
Dev.GameInDev()
Dev.age_()
Dev.GameListCreated()
