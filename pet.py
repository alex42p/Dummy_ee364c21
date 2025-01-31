def main: 
  pet = input("Enter whether you want a dog or a cat (D/C): ")
  if pet.lower() == "d":
    print("bark bark bark\nYour dog has been acquired!")
  elif pet.lower() == "c":
    print("meowwwwwww, purrrrrr\nYour cat has been acquired!")
  else:
    print("That's not an option yet. No pet for you")

  print("GAME OVER!")
          
if __name__ == '__main__':
  main()
