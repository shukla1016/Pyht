class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
    def deposit(self, a, des=''):
        self.ledger.append({'amount':a, 'description':des})
    def withdraw(self, a, des=''):
        if self.check_funds(a) == True:
            self.ledger.append({'amount':a*-1, 'description':des})
            return True
        else:
            return False
    def transfer(self, a, catg):
        if self.check_funds(a) == True:
            wdes = "Transfer to " + catg.category
            self.ledger.append({'amount':a*-1, 'description':wdes})
            ddes = "Transfer from " + self.category
            category.deposit(amount, ddes)
            return True
        else:
            return False  
    def get_balance(self):
        res = ''
        titl = self.category.center(30, '*')
        res += titl + '\n'
        total = 0
        for i in self.ledger:
            des = i['description'][:23]
            res += des
            a = i['amount']
            total += i['amount']
            a = format(a, '.2f')
            offset = 30 - len(des)
            offsetStr = '{:>' + str(offset) + '}'
            a = offsetStr.format(a)
            res += a + '\n'
            res += 'Total: ' + format(total)
            return res

        def check_funds(self, a):
            bal= 0
            for i in self.ledger:
                for j in i:
                    bal+= i['amount'] 
                if a < bal:
                    return True
                else:
                    return False
def create_spend_chart(catgs):
    res = "Percentage spent by category\n"
    totals = getTotals(catgs)
    for i in (0,100,10):
        spaces = " "
        for total in totals:
            if total * 100 >= i:
                spaces += "o  "
            else:
                spaces += "   "
        res+= str(i).rjust(3) + "|" + spaces + ("\n")
    dash = "-" + "---"*len(catgs)
    names = []
    x_axis = ""
    for catg in catgs:
        names.append(catg.name)
    maxi = max(names, key=len)
    for i in range(len(maxi)):
        nameStr = '     '
        for j in names:
            if i >= len(j):
                nameStr += "   "
            else:
                nameStr += j[i] + "  "
        nameStr += '\n'
        x_axis += nameStr
    res+= dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return res