```plaintext
Use Python in CLI to run the game and follow the instructions(the game is in Swedish): 

python main.py

Flowchart for code: 

Start
   ↓
Player Input: "Sten, Sax, or Påse"
   ↓
Computer Input: (Randomly choose Sten, Sax, or Påse)
   ↓
Compare Choices:
   ┌─────────────────────────┐
   │      Is it a tie?        │
   └─────────────────────────┘
       /               \
    Yes                 No
    ↓                   ↓
  "It's a Tie!"        Check Winner:
    ↓                   ┌────────────────────────┐
   Loop back to         │ Player wins?            │
   Player Input         └────────────────────────┘
                          /               \
                       Yes                 No
                       ↓                   ↓
                  "Player Wins!"       "Computer Wins!"
                       ↓                   ↓
                   End Game           End Game

