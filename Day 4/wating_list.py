# try:
#     wating_list=["john","marry"]
#     name=input("enter name:")
#
#     number=wating_list.index(name)
#     print(f"{name}'sturn is{number}")
# except ValueError:
#     print("Please enter a valid name")


# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     return(maximum)
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)

# However, 'when running the code,the folL owing error is generated':

# TypeError:'unsupported uperand type(s)for*:'NoneTYPE' and 'float'

# def speed(distance, time):
#     return distance / time
#
#
# print(speed(200, 4))
# 'However, when she calls the function(as you see belOw), she gets an error:

# 'TypeError: speed() missing 1 required positionalargument: 'time'

# 'Try fixing the code so she gets 50 asout put.


# Bug - Fixing Exercise 2 this time ,
# alina traveled 300 miles and it took her 5 hours.However,
# she is not getting thecorrect output from its funtion.try fixing the code:

def speed(distance, time):
    return distance / time


print(speed(5, 300))