# 井辻陸,hangman(単語当てゲーム)


# ライブラリのインポート
import random
from words import word_list
import getpass
import re


# ランダムなwordを返す関数random_word()
def random_word():
  word = random.choice(word_list)
  return word


# play_hangman()
def play_hangman(word):
  count = 0 # 間違えた回数
  letters = list(word)
  board = ["_"] * len(word)
  print("\n")
  print("Let's play hangman!")
  print(hangman(count)) # ハングマン（絞首台）を表示
  print("".join(board)) # ボードを表示
  print("\n")
# 外した回数が5回までのときの処理
  while count < 6:
      letter = input("Guess a letter⇒")
      if letter in letters:
        index = letters.index(letter)
        board[index] = letter
      else:
        count += 1
      print(hangman(count)) # ハングマンを表示
      print("".join(board)) # ボードを表示
      print("\n")
      if "_" not in board:
        print("You win!")
        break
# 6回目に外した時の処理
  if count == 6:
    print("You lose. The answer is", word)


# ハングマンの図
def hangman(count):
    stages = [                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """
    ]
    return stages[count]


def main():
  msg = input("Please enter the number of players(1 OR 2)⇒")  # 一人か二人か選んでもらう
# 1人で遊ぶときの処理
  if msg == "1":
    word = random_word()
# 2人で遊ぶときの処理
  if msg == "2":
    while True:
      player1 = "player1: Enter a English word(3 ~ 6 letters)⇒"
      word = getpass.getpass(player1) # player1が入力した文字が見えなくなる
      if not re.match('^[a-z]+$', word):  # 入力がアルファベットかどうかの判定
        print("Enter alphabets !")
      else:
        if len(word) >= 3 and len(word) <= 6:
          break
        else:
          print("Enter a English word(3 ~ 6 letters)⇒")
  play_hangman(word)


main()