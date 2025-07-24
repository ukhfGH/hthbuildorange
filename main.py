print("first pyton file yippeee!!1!")

def yippee (yippee_amount):
    return "yippee " * yippee_amount


while True:
    try:
      yippee_num = int(input("put how many yippeees here: "))
      print(yippee(yippee_num))
      break
    except ValueError:
       pass
