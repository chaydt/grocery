#grocery list
#change 
#change  2

from time import sleep

list = []
msg = "Welcome to the grocery list, what is your name? "
finished = False
named = False
userName = ""


def namer(msg):
  global userName
  userName = input(msg)


namer(msg)

while not named:

  def valid_name(userName):
    leng = len(userName)
    valid_leng = bool(leng >= 2 and leng <= 15)
    nums = False
  
    for i in userName: 
      if i.isdigit():
        nums += 1
      else:
        nums = nums

    return bool(valid_leng and nums == 0)

  if valid_name(userName):
    userName = userName.capitalize()
    print(
    f"\nWelcome, {userName}, this program will help store, "
    "print and edit your grocery list.\n"
    )
    named = True
  else:
    print("Make sure to enter a valid name!")
    namer("Name: ")


#add items to the list
def add_item():
  global list
  item = input("\nWhat items do you want to add? \n:")
  item = item.strip()
  items = item.split(", ")

  for i in items:
    list.append(i)

  print(f"added {item} to list \n")


def remove_item():
  item = input("\nWhat items do you want to remove? \n:")
  item = item.strip()
  items = item.split(", ")

  for i in items:
    try:
      list.remove(i)
    except ValueError:
      print(f"{i} not in list")
      
    print("removed valid items from list")


def view_all(speed):
  n = 1
  for i in list:
    print(f"{n}, {i}")
    sleep(speed)
    n += 1


def end():
  global finished
  loc = 'list.txt'
  n = 1
  with open(loc, "w") as file:
    print(
    f"Thank you for using this shopping list script, {userName}! "
    "Saving your items..."
    )
    sleep(1)
    #view_all(0.02)
    for i in list:
      file.writelines(f"{n}, {i} \n")
      n += 1
    print(f"Saved list to file {loc} ")
    finished = True


while not finished:
  operation = input(
      "Would you like to a) add to list b) remove an item "
      "c) print the list d) finalise and save the list? \n:"
  )

  if "a" in operation:
    add_item()
  elif "b" in operation:
    remove_item()
  elif "c" in operation:
    view_all(0.1)
  elif "d" in operation:
    end()
  else:
    print(f"'{operation}' not valid! \n")
