#Solve Rectangula according to the user input.

def createIntPositions(board):
    #return a list of all the position on board with number
    (rows,cols) = (len(board),len(board[0]))
    result = []
    for row in range(rows):
        for col in range(cols):
            if board[row][col]!=0:
                result.append((row,col,board[row][col]))
    return result

def getPossibleDimensions(area):
    #return a list of all the possible dimensions for given area
    result = []
    for row in range(1,area+1):
        if area%row==0:
            col = int(area/row)
            result.append((row,col))
    return result

def getPossibleStartPositions(board,intPosition,dimension):
    #return a list of all start position with given number and dimension
    result = []
    (rows,cols) = (len(board),len(board[0]))
    (recRow,recCol) = dimension
    (intRow,intCol) = (intPosition[0],intPosition[1])
    for row in range(intRow-recRow+1,intRow+1):
        for col in range(intCol-recCol+1,intCol+1):
            if 0<=row<rows and 0<=col<cols:
                result.append((row,col))
    return result

def isLegalMove(board,startPosition,dimension):
    #test if a move from a position with dimension is valid or not
    (rows,cols) = (len(board),len(board[0]))
    (recRow,recCol)=dimension
    (startRow,startCol) = startPosition
    for row in range(startRow,startRow+recRow):
        for col in range(startCol,startCol+recCol):
            if (row<0) or (row>=rows) or (col<0) or (col>=cols):
                return False
            elif board[row][col]!=0:return False
    return True

def makeMoveOnBoard(board,startPosition,dimension,depth):
    #make the move on board from start position with required dimension
    (rows,cols) = (len(board),len(board[0]))
    (recRow,recCol) = dimension
    (startRow,startCol) = startPosition
    for row in range (startRow,startRow+recRow):
        for col in range(startCol,startCol+recCol):
            board[row][col] = depth

def resetBoard(board,startPosition,dimension):
    #reset the board from start position follow the dimension
    (rows,cols) = (len(board),len(board[0]))
    (recRow,recCol) = dimension
    (startRow,startCol) = startPosition
    for row in range (startRow,startRow+recRow):
        for col in range(startCol,startCol+recCol):
            board[row][col] = 0

def solveRectangula(board):
    #use backtracking to solve the Rectangular problem
    (rows,cols) = (len(board),len(board[0]))
    solution = [[0]*cols for i in range(rows)]  
    solutionSet = [];intPositions = createIntPositions(board) #get all number
    def createSolution(depth=0):
        if depth==len(intPositions):return solutionSet
        currInt = intPositions[depth]  
        allDimensions = getPossibleDimensions(currInt[2]) 
        #all possible dimensions for the area
        for dim in allDimensions:
            allStartPosition = getPossibleStartPositions(solution,currInt,dim)
            #all possible left-top position for a given number area
            for sp in allStartPosition:
                if isLegalMove(solution,sp,dim):
                    makeMoveOnBoard(solution,sp,dim,depth+1)
                    solutionSet.append((sp[0],sp[1],dim[1],dim[0]))
                    result = createSolution(depth+1)
                    if result!=None:return result #return it if not None
                    
                    #reset board and try other solution
                    resetBoard(solution,sp,dim)
                    solutionSet.pop()  
        return None
    return createSolution(0)


from hw10_rectangula_tester import testSolveRectangula
from hw10_rectangula_tester import playRectangula       
testSolveRectangula(solveRectangula)
playRectangula(solveRectangula)

    

