class Person(object):
    t="I squirreled it away before it could catch on fire."

    def __init__(self, name):
        self.name = name

    def say(self, stuff):
        Person.t=stuff
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        return self.say(Person.t)


class Account(object):
    """A bank account that allows deposits and withdrawals."""

    interest = 0.02
    


    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions=[]

    def deposit(self, amount):
        self.transactions.append(('deposit',amount))
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.transactions.append(('withdraw',amount))
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
    



class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""

    withdraw_fee = 1
    interest = 0.01
    

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    def deposit_check(self, check):
        if check.payable_to==self.holder:
            if check.deposited == False:
                check.deposited = True
                return self.deposit(check.check_balance)
                
            else:
                print('The police have been notified.')
        else:
            print('The police have been notified.')
        

class Check(object):
    def __init__(self, payto, checkbalance):
        self.check_balance = checkbalance
        self.payable_to = payto
        self.deposited = False

            
