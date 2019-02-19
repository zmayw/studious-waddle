#coding=utf-8

class Calculator:

    operator_level = {"+":1, "-":1, "*":2, "/":2}
    splitstr = ["+","-","*","/","(",")"]
    numbers = (0,1,2,3,4,5,6,7,8,9)
    inputExpr = []
    newExpr = []
    result = 0

    def __init__(self,inputStr):
        self.inputExpr = self.mySplit(inputStr, self.splitstr)
        print "inputStr: ", inputStr
        print "inputExpr: ", self.inputExpr


    def mySplit(self, s, ds):
        res = [s]
        for d in ds:
            t = []
            for s in res:
                sub_res = s.split(d)
                n = len(sub_res)
                newsub = []
                for i in range(n):
                    newsub.append(sub_res[i])
                    if i<n-1:
                        newsub.append(d)
                t.extend(newsub)
            res = t
        return [x for x in res if x]


    def changeMidExprToAfterExpr(self, inputExpr, newExpr):
        list = []
        for i in inputExpr:
            if(i == "("):
                list.append(i)
            elif ( i in self.operator_level.keys()):
                while (len(list)>0 and list[-1] != "(" and self.operator_level[list[-1]] >= self.operator_level[i]):
                    operator = list.pop()
                    newExpr.append(operator)
                list.append(i)
            elif i==")":
                while(len(list)>0 and list[-1]!="("):
                    operator = list.pop()
                    newExpr.append(operator)
                if len(list) > 0 and list[-1] == "(":
                    list.pop()
            else:
                newExpr.append(i)
        while len(list) > 0:
            newExpr.append(list.pop())


    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y,):
        if y==0:
            raise "除数不能为0"
        return x/y

    operator = {"+": add, "-": subtract, "*": multiply, "/": divide}

    def calculator(self, newExpr):
        if newExpr == []:
            return
        list = []
        for element in newExpr:
            if element in self.operator.keys():
                y = float(list.pop())
                x = float(list.pop())
                res = self.operator.get(element)(self, x, y)
                list.append(res)
            else:
                list.append(element)
        self.result = list.pop()

    def run(self):
        self.changeMidExprToAfterExpr(self.inputExpr,self.newExpr)
        print "newExpr: ",self.newExpr
        self.calculator(self.newExpr)
        print "Result: ",self.result


cal = Calculator("10-2+(2+2)*5/0")
cal.run()
