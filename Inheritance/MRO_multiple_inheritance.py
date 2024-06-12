'''
class Boss:

    def report(self):
        print("Boss : Report")

class Manager1(Boss):

    def report(self):
        print("Manager 1 : Report")

class Manager2(Boss):

    def report(self):
        print("Manager 2 : Report")

class Manager3(Boss):

    def report(self):
        print("Manager 3 : Report")

class TeamLead1(Manager1,Manager3):

    def report(self):
        print("TeamLead 1 : Report")

class TeamLead2(Manager2,Manager3):

    def report(self):
        print("TeamLead 2 : Report")

class Developer(TeamLead1,TeamLead2):

    def report(self):
        print("Developer : Report")

print(Developer.__mro__)

print(Developer.mro())
'''
class Boss:

    def fun(self):
        print("Mich aahe BOSS")

class Manager(Boss):

    def fun(self):
        print("In Fun : Manager")

class TeamLead(Boss,Manager):

    def fun(self):
        print("In Fun : Boss & Manager")

class Developer(TeamLead):

    def fun(self):
        print("In Fun : Developer")

print(Developer.__mro__)



