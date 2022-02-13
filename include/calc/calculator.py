import queue

class Expression:
    def __init__(self, infixExpr):
        self.__infixExpr = infixExpr  # Infix expression input by user.
        self.__postfixExpr = ""       # Postfix conversion of '__infixExpr'.
        self.__tmpNumString = ""      # Temporary number stored in string form
        self.isIntegerOnly = True   # Whether operands or the operator need only integers.

    def __StoreNumber(self, pos: int, exprType: str) -> int:
        i = pos
        if exprType == "in":
            while (i < len(self.__infixExpr)) and (self.__infixExpr[i].isdigit()) or (self.__infixExpr[i] == '.'):
                if self.__infixExpr[i] == '.':
                    self.isIntegerOnly = False
                self.__tmpNumString += self.__infixExpr[i]
                i += 1
        elif exprType == "post":
            while (i < len(self.__postfixExpr)) and (self.__postfixExpr[i].isdigit()) or (self.__postfixExpr[i] == '.'):
                self.__tmpNumString += self.__postfixExpr[i]
                i += 1
        return i

    def __ClearNumber(self):
        self.__tmpNumString = ""

    def __IsOperator(self, inputString: str) -> bool:
        if inputString == '^' or inputString == '/' or inputString == "ln" or inputString == "ln":
            self.isIntegerOnly = False
            return True
        # Update self.isIntegerOnly to false when using additional mathematical functions.

        if inputString == '+' or inputString == '-' or inputString == '*':
            return True
        else:
            return False

    def __IsLeftAssociative(self, operator: str) -> bool:
        if operator == '-' or operator == '/' or operator == '+' or operator == '*':
            return True
        return False

    def __Tokenizer(self, inputExpr: str, exprType: str) -> list:
        tokens = []
        jumpIdx = 0
        for i in range(0, len(inputExpr)):
            if (i < jumpIdx) and (i != 0):
                # Jump characters until jumpIdx.
                continue
            if self.__IsOperator(inputExpr[i]):
                tokens.append((inputExpr[i], 'o'))
            elif inputExpr[i] == '(':
                tokens.append((inputExpr[i], 'l'))
            elif inputExpr[i] == ')':
                tokens.append((inputExpr[i], 'r'))
            elif inputExpr[i].isdigit():
                jumpIdx = self.__StoreNumber(i, exprType)
                tokens.append((self.__tmpNumString, 'n'))
                self.__ClearNumber()
        return tokens

    def Tokenizer(self) -> list:
        return self.__Tokenizer(self.__postfixExpr, "post")

    def __GetPrecedence(self, operator1: str, operator2: str) -> int:
        precedenceList = ['^',1,'*',2,'/',2,'+',3,'-',3] # Precedence list, lowest number means highest precedence.
        precedencePair = [0,0]  # Precedence of given operators, first value for "operator1', second value for 'operator2'.
        for i in range(0, 10, 2):
            if operator1 == precedenceList[i]:
                precedencePair[0] = precedenceList[i + 1]
            elif operator2 == precedenceList[i]:
                precedencePair[1] = precedenceList[i + 1]
        if precedencePair[0] < precedencePair[1]:
            return 1
        elif precedencePair[1] < precedencePair[0]:
            return -1
        else:
            return 0

    def __Next(inputQueue: Union[queue.Queue, queue.LifoQueue]) -> str:
        nextItem = inputQueue.get()
        inputQueue.put(nextItem)
        return nextItem


