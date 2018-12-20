steps = input()
index = 1
for step in steps:
    if step == "A":
      if index == 1:
          index = 2
      elif index == 2:
          index = 1
    elif step == "B":
        if index == 2:
            index = 3
        elif index == 3:
            index = 2
    else:
        if index == 1:
            index = 3
        elif index == 3:
            index = 1

print(index)
