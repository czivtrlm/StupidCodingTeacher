#############################
# Collaborators: (enter people or resources who/that helped you)
# If none, write none
# Leo Yang
#
#############################
import io
import random
import sys

inputs_1 = ["cxk", "niganma~~ haiyo", "From Athenian school", "Haiya why so good", "training 2 and half year"]
answer_1 = [3, 12, 18, 14, 20]
stdout = sys.stdout
question = random.randint(1, 2)
match question:
    case 1:
        print("please make a code that can identify how many letters are there in a string (exclude spaces):")
    case 2:
        print("make a code that can print from 1 to 100:")

r = "def answer():\n"
while True:
    s = input()  # get the writen code
    if s.strip() == "end":
        break
    r += "\t" + s + "\n"

original_input = input
input_index = random.randint(0, 4)


# print(inputs_1[input_index + 1])
# print(r)


def input(*args, **kwargs):
    match question:
        case 1:
            return inputs_1[input_index]  # cover the definition of input to get the value in the writen code


try:
    sys.stdout = result = io.StringIO()
    exec(r)
    exec("answer()")  # run the program to identify if it's correct


    def input(*args):
        return original_input(args)  # turn the input back to normal


    sys.stdout = stdout
    r = result.getvalue().strip()
    # print(r)
    match question:
        case 1:
            if int(r) != answer_1[input_index]:
                raise Exception("/////////////////////haiya why so weak/////////////////////")
            print("Nice job!")
        case 2:
            rs = r.split("\n")
            for i in range(1, 101):
                if rs[i - 1] != str(i):
                    raise Exception("/////////////////////haiya why so weak/////////////////////")
            print("Nice job!")
except Exception as e:
    sys.stdout = stdout
    print(e, "\nError!!")

#############################
# Answer of the code:
#
# for i in range(1,101):
#     print(i)
#
# e = input()
# b = 0
# for i in e:
#     if i != " ":
#         b +=1
# print(int(b))
############################
