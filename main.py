import random
class Player: 
  def __init__(self):
    self.valid_options = ["sten", "sax", "påse"]
    self.choice = None

    while self.choice not in self.valid_options:
      self.choice= input("Välj sten, sax eller påse: ")
      if self.choice not in self.valid_options:
        print(f"Försök igen: ")

    print(f"Du valde: {self.choice}")

class Computer:
  def __init__(self):
    self.valid_options = ["sten", "sax", "påse"]
    self.choice = random.choice(self.valid_options)

    print(f"Datorn valde: {self.choice}")


def game(player_choice, computer_choice):
  if player_choice == computer_choice:
        return "LIKA!"
  elif (
      (player_choice == "sten" and computer_choice == "sax") or
      (player_choice == "sax" and computer_choice == "påse") or
      (player_choice == "påse" and computer_choice == "sten")
    ):
      return "DU VANN!"
  else:
      return "DATORN VANN"

if __name__ == "__main__":
  while True:
    player = Player()
    computer = Computer()

    result = game(player.choice, computer.choice)
    print(result)

    if result == "LIKA!":
      player.choice = None
    else:
      break