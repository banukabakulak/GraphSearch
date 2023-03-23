from array import array

class Vertex:
    id = -1
    pred = -1
    order = -1
    adj = array('i', [])

    isMarked = False

    #def __init__(self):
     #   pass

    def __init__(self, idIn, adjIn):
        self.id = idIn
        self.adj = adjIn

