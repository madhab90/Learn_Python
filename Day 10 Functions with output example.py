firstName = input("Enter your First Name. ")
LastName = input("Enter your Last Name.")

def format_name(fName, lName):
  return fName.title() + " "+ lName.title()



format_fullName = format_name(firstName, LastName)

print(f"Your name is {format_fullName}")
