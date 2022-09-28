fun = 4

notFun = 4.4

sum = fun + notFun
print(type(sum), sum)


import random 
rand_num = random.randint(2,1000000)
print(rand_num)

practice = float(4)

print (practice)

# rfhwifh;owriefheoirfh

name = "Zen"
print("My name is " + name)

name = "Zen"
print("My name is", name)


print("Hello " + str(42))		# output: Hello 42

f_name = "Jack"
l_name = "Tangel"
age = 24
love = "climbing"

x = "Hi all, my name is {} {}. I am {}, and I love {}".format(f_name, l_name, age, love)
# x = (f"Hi all, my name is {f_name} {l_name}. I am {age}, and I love {love}.")
print(x.upper())
print(x.count("I"))

# Wed Sept 28

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

print (ninjas + my_list)

print (ninjas * 2)

# print (ninjas * my_list) error!


#Challenge: Taking the example list below, read each line of the code snippet and see if you can see the pattern in the syntax. What does the number before the colon do, what about the one after? How are they different? What if there is no number? Feel free to write down your thoughts!

words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']


# MY ANSWER: the number before the colon tells the console to slice the list starting at that specfifc index. if there is no number, it starts at the beginning. The number at the right of the colon tells the console which index to stop at. If there is no number, it means the computer should go THROUGH the end of the list. Since line 57 tells the computer  to end at index 4, it will not print index four. It will stop.


# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']


trial = ['this', 'is', 'a', 'trial']
trial2 = [9,4,8,3,7,2,6,5,1]

print(len(trial))
print(max(trial)) #output is trial because it has the most letters
print(min(trial)) #output is a bc it has the least
print(sorted(trial)) #sorts by number of letters min-max
print(sorted(trial2)) #sorts by value

trial.append("or is it")
print(trial)
trial.pop(0)
print(trial)
print(trial.index("is"))
trial.reverse()
print(trial)
trial.sort()
print(trial)



x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")

# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")

# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")

# nothing happens, because the statement is false   



isJackCoding = False
isJackClimbing = True

if isJackCoding == True:
    print('Nice job Jack')
elif isJackCoding == False: 
    isJackClimbing == True
    print('I guess fun is important')
else:
    print('Jack should probably be coding')





for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

#just a line break in console

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

# Challenge: Write a for loop to print all integers from 1 to 20, including 20.


for i in range(1,21):
    print(i)





countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
for integer in range(0, len(countries)):
    print("Index:", integer)
    # Challenge 2: print the index here
    print("Country:", countries[integer])
    # Challenge 3: print the country here

# Looping over values only...
for country in countries:
    print("Country: ", country)
    # Challenge 4: print the country here



# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name(fname, lname):
    return fname + " " + lname 

name1 = full_name("Eddie", "Aikau")
print(name1) # should print Eddie Aikau

# Challenge 2: 
#   Call the function again using your own name and print the results!

name2 = full_name ("Jack", "Tangel")
print(name2)