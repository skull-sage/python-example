def sortExample():
  """
    built in sorted() function take iterable as arg 
    and create a new sorted list. while list.sort() 
    modifies the list in place
  """
  smList = [5, 1, 2, 3, 4, 6]
  o1List = sorted(smList)
  print("in place sorted? ", 'yes' if o1List is smList else 'no')
  smList.sort()
  pass


def pushPopExample():
  sampleList = [10, 20, 30]
  sampleList.append(95)
  print("as stack: after push ", sampleList)

  poppedItem = sampleList.pop()
  print("as stack: pop", poppedItem, "from", sampleList)

  sampleList.insert(1, 50)
  print("as queue: after insert ", sampleList)

  pass


matrix = [
    ['a1', 'b1', 'c1', 'd1'],
    ['a2', 'b2', 'c2', 'd2'],
    ['a3', 'b3', 'c3', 'd3'],
]


def transposeByLoop():
  tMatrix = []
  for colIdx in range(len(matrix[0])):
    tRow = []
    for row in matrix:
      tRow.append(row[colIdx])
    #endfor
    tMatrix.append(tRow)
  #endfor


def transposeByComprehension():
  #Turning loop into comprehention
  tMatrix = [[row[idx] for row in matrix] for idx in range(len(matrix[0]))]
  print("Transposed Matrix: ", tMatrix)


# transposeByComprehension()
def delExample():
  global matrix

  print(matrix)
  del matrix[1][2]
  print(matrix)

  del matrix[1]
  print(matrix)
  pass


def copy2DList():
  """ 
    copy() generally does a shadow copy
    comprehension technique with [list()] does a deep copy
  """
  listCopy = matrix.copy()

  listCopy = [list(row) for row in matrix]
  listCopy[0].append('HOLA!')
  print("original", matrix[0])
  print("copy", listCopy[0])
  pass


#copy2DList()

pushPopExample()