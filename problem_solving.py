import numpy as np
import numpy.linalg
import re
import probability as P

# Uncomment and implement two of the following.  Refer to the Problem solving brief for specifications.

# def censor(s):
#    #r = 
#    return r

def fertiliser(an, ap, bn, bp, n, p):
   A = np.array([[an, bn],[ap, bp]]) #The matrix of the problem
   y = np.array([n, p]) #The vector of parameters
   if np.linalg.det(A) != 0 : 
      Ainv = np.linalg.inv(A)
      # x is the vector of unknown
      x = Ainv @ y
   else : #The determinant of the matrix is null, the equation has no solution
      print("here")
      return None
   a = x[0]
   b = x[1]
   if (a < 0) | (b<0) : #The solution has at leat one negative term, it is non-physical
      return None
   return a, b

def decide(P, ulist):
   U = np.row_stack(ulist)
   utilities = U @ P
   best = utilities.argmax()
   return best, utilities[best]

def makeBet(headsOdds, tailsOdds, previousOutcome, state):
   likelihood = 
   U1 = np.array([headsOdds, -1]) #choosing heads
   U2 = no.array([-1, tailsOdds]) #choosing tails
   utils = [U1, U2]
   decide = decide(P,utils)
   if decide[1] <= 0 :
      bet = 'no bet'
   else if decide[0] == 0 :
      bet = 'heads'
   else:
      bet = 'tails'
   state = 
   return (bet, state)


# The following will be run if you execute the file like python3 problem_solving.py
# Your solutions should not depend on this code.
# The automated marker will ignore any changes to this code; feel free to modify it
# but keep the if and the indenting as is
if __name__ == '__main__':
   try:
      print(censor('The cat ate a mouse.')) # should give "### cat ate # mouse. <n1234567>"
   except NameError:
      print("Not attempting censoring problem")

   try:
      print(fertiliser(1, 0, 0, 1, 2, 2)) # should give (2.0, 2.0)
   except NameError:
      print("Not attempting fertiliser problem")

   import random
   try:
      random.seed(0)
      totalprofit = 0
      for round in range(10000):
         if random.randint(0,1) == 0:
            headsprob = 0.7
         else:
            headsprob = 0.4

         previousOutcome = None
         state = None
         profit = 0
         odds = dict()
         for _ in range(100):
            odds['heads'] = random.uniform(1, 3)
            odds['tails'] = random.uniform(1, 3)
            
            bet, state = makeBet(odds['heads'], odds['tails'], previousOutcome, state)
            
            previousOutcome = 'heads' if random.random() < headsprob else 'tails'
            if bet == previousOutcome:
               profit += odds[bet] - 1
            elif bet != 'no bet':
               profit -= 1          # stake lost

         print("Probability of heads was", headsprob, "Profit was", profit)
         totalprofit += profit
      print("Average profit per run:", totalprofit / 10000)

   except NameError as e:
      print("Not attempting probability problem")