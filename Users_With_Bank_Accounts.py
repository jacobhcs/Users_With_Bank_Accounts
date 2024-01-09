class User:
  def __init__(self, f_name, l_name, email, age):
    self.first_name = f_name
    self.last_name = l_name
    self.email = email
    self.age = age
    self.account = BankAccount(200)
    is_rewards_memeber = False
    gold_card_points = 0
  def display_info(self):
    print(self.first_name, self.last_name, self.email)
    return self
  def enroll(self):
    self.is_rewards_memeber = True
    self.gold_card_points = 200
    return self
  def spend_points(self, amount):
    self.gold_card_points -= amount
    return self
  def make_deposit(self,amount=0):
     self.account.deposit(amount)
     return self
  def make_withdrawal(self,amount=0):
     self.account.withdraw(amount)
     return self
  def display_user_balance(self, account_type="checking"):
     self.account.display_account_info()
     return self
  
class BankAccount:
    all_accounts = []
    bank_balance = 0
    def __init__(self, int_rate=0.02, balance=0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Account Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self

user_profile = User("Jacob", "Harris", "jacobh@aol.com", 24).enroll().display_info().spend_points(50).make_deposit(1000).make_withdrawal(50).display_user_balance()

user_profile2 = User("John", "Doe", "johnd@aol.com", 34).enroll().display_info().spend_points(50).make_deposit().make_withdrawal(50).display_user_balance()