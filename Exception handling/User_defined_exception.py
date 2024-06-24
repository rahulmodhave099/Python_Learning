class VotingError(BaseException):

    def __init__(self,msg):
        self.msg = msg
        #     OR
        super().__init__(msg)

def voting(name,age):

    if age<18:
        raise VotingError("Not Eligible for voting")
    else:
        print("Thanks for voting")

print("Start Code")

name = input("Enter your name : ")

try:
    age = int(input("Enter your age : "))

except ValueError:
    print("Proper integer value de ")
    age = int(input("Enter your age : "))

try:
    voting(name,age)

except VotingError as err:
    print(err.msg)
    #    OR
    print(err)

finally:
    print("End Code")