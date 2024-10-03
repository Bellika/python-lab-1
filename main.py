import random
class Player: 
  def __init__(self):
    self.valid_options = ["sten", "sax", "påse"]
    self.option = None

    while self.option not in self.valid_options:
      self.option = input("Välj sten, sax eller påse: ")
      if self.option not in self.valid_options:
        print(f"Försök igen: ")

    print(f"Du valde: {self.option}")

class Computer:
  def __init__(self):
    self.valid_options = ["sten", "sax", "påse"]
    self.option = random.choice(self.valid_options)

    print(f"{self.option}")

if __name__ == "__main__":
  player = Player()
  computer = Computer()