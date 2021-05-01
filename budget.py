class Category:


    def __init__(self, name):
         self.name = name
         self.ledger = list()
         
         
    def __str__(self):
      title = f"{self.name:*^30}\n"
      items = ""
      total = 0
      for item in self.ledger:
          items += f"{item ['description'][0:30]:30}"+ f"{item ['amount']:>7.2f}" '\n'
          total += item ['amount']
      output = title + items + "Total:" + str(total)
      return output


    def deposit(self, amount, description ):


          """
          A deposit method that accepts an amount and decription. If no
          decription is given, it should default to an empty string. The
          method should append an object to the ledger list in the form of
          ("amount": amount, "description": description)
          """ 
          self.ledger.append({"amount": amount, "description": description})
        

    def withdraw(self, amount, description):
        """
        A withdraw method. 
        """
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False


    def get_balance(self):
        """
        Getting total balance.
        """
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]
            return total_cash


    def transfer(self, amount, Category):
        """
        Transfer method from one category to another.
        """
        if(self.check_funds(amount)):
            self.withdraw(amount, "Transfer to" + Category.name)
            Category.deposit(amount, "Transfer from" + self.name)
            return True
        return False


    def check_funds(self, amount):
        """
        This checks if there is sufficient to be deposited or withdrawn from one category or another. 
        """
        if(self.get_balance () >= amount):
            return True
        return False