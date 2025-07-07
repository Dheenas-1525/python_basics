def students(name, age, mobile, address):
    return name, age, mobile, address

# students = input("Enter your Name : ")
# students = input("enter your Age : ")
# students = input("Enter your mobile number : ")
# students = input("Enter Your Address : ")

name_input = input("Enter Your Name : ")
age_input = input("Enter Your Age : ")
mobile_input = input("Enter Your Mobile NUmber  : ")
address_input = input("Enter Your Address : ")

student_name, student_age, student_mobile, student_address = name_input, age_input, mobile_input, address_input


print("\n🧾 Student Details:")

print("Hello Sir Your Good Name is :-> {}".format(name_input))
print("Your Age is :-> {}".format(age_input))
print("Your Mobile Number is :-> {}".format(mobile_input))
print("Your Adress  is :-> {}".format(address_input))

print("===========================================================")

print("Thankyou for Sharing Your Details With US sir.......")