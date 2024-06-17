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

class Manager1(Boss):

    def fun(self):
        print(" Manager1 Reports to : Boss")

class Manager2(Boss):

    def fun(self):
        print(" Manager2 Reports to : Boss")

class TeamLead1(Manager1,Manager2):

    def fun(self):
        print(" TeamLead1 Reports to : Manager1 and Manager2")

class TeamLead2(Manager2 ):

    def fun(self):
        print(" TeamLead2 Reports to : Manager2")

class Developer(TeamLead1,TeamLead2):

    def fun(self):
        print(" Developer Reports to : TeamLead1 and TeamLead2")

print(Developer.__mro__)



