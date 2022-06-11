import numpy as np

def isProb(P):
   if P.max() > 1:
      return False
   if P.min() < 0:
      return False
   return P.sum() == 1   

def probEvent(P, E):
   return P.dot(E)

def conditionalProb(P, E, C):
   return P.dot(E * C) / P.dot(C)

def utility(P, u):
   return P.dot(u)

def decide(P, ulist):
   U = np.row_stack(ulist)
   utilities = U @ P
   best = utilities.argmax()
   return best, utilities[best]

if __name__ == '__main__':
   try:
      P = np.array([0.5, 0.4, 0.1])
      Q = np.array([0.5, 0.4, 0.2])
      print('isProb for a good probability dist:', isProb(P))
      print('isProb for a bad prob dist:', isProb(Q))

      E = np.array([0, 1, 0])
      print('prob for event [0, 1, 0]:', probEvent(P, E))
      C = np.array([0, 1, 1])
      print('conditional prob for [0,1,0] given [0, 1, 1]', conditionalProb(P, E, C))

      U = np.array([1,2,3])
      print('Expected utility for  u = [1,2,3]:', utility(P, U))

      U2 = np.array([-1, 2, 2])
      U3 = np.array([1, -1, 5])
      utils = [ U, U2, U3 ]
      print('Choosing based on max expected utility', decide(P, utils))

   except NameError as e:
      print(e)      
      print("Not attempting linear algebra problem")
