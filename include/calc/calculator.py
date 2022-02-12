class Expression:
    def __init__(self, infixExpr):
        self.infixExpr = infixExpr  # Infix expression input by user.
        self.postfixExpr = ""       # Postfix conversion of 'infixExpr'.
        self.tmpNumString = ""      # Temporary number stored in string form
        self.isIntegerOnly = True   # Whether operands or the operator need only integers.

    def StoreNumber(self, pos, exprType):
        i = pos
        if exprType == "in":
            while (i < len(self.infixExpr)) and (self.infixExpr[i].isdigit()) or (self.infixExpr[i] == '.'):
                if self.infixExpr[i] == '.':
                    self.isIntegerOnly = False
                self.tmpNumString += self.infixExpr[i]
                i += 1
        elif exprType == "post":
            while (i < len(self.postfixExpr)) and (self.postfixExpr[i].isdigit()) or (self.postfixExpr[i] == '.'):
                self.tmpNumString += self.postfixExpr[i]
                i += 1
        return i
