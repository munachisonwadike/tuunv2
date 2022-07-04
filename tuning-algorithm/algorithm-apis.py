'''
TuningAlgorithm is the high-level abstract class that 
other algortihms such as RandomSearch and BO variants inherit from

Note that the use of the ABC class in Python comes with a number of features, 
e.g (a) preventing the user from instantating the high-level
TuningAlgorithm class (which serves here as a ghost class). 
(b) forcing the implementation of any method declared by the high-level class, 
in all it's subclasses

@abstractmethod decorator must be used at least once for the TuningAlgorithm
to count as an abstract class, and have all such features see explanation here: https://youtu.be/TeDlx2Klij0
'''

from abc import ABC, abstractmethod

class TuningAlgorithm(ABC):
	@abstractmethod
	def suggest(self):
		""" suggests the next best 
		point to query. e.g for random search
		we just pick a point in our range; whereas
		for BO, we maximise acquisition function
		"""
		pass

	@abstractmethod
  	def wss(self):
  		"""sends set of hyperparameters 
		to workflow submission system
  		i.e our pipeline which runs 
  		via Argo workflows SDK"""
  		pass

  	@abstractmethod
	def update(self):
		""" updates the 'thing' that helps us
		pick new query points: e.g for gridsearch we 
		the next point in a list; whereas for 
		BO we can update parameters of a Gaussian Proc.
		"""
		pass

	@abstractmethod
	def loop(self):
		""" main iterative-convergent loop using 
		all the fxn's defined above
		see pseudo-code in below:
		for i in range(query_budget or num_iters):
		 1. select a point
		 2. evaluate point by passing to WSS
		  - return the cost/fxn value from wss  
		 3. update acquisition function
		  - in case of random search => pass
		  - in case of BO => update prob dists 
		   & and use to update acq. fxn
		"""
		pass
		 

class RandomSearch(TuningAlgorithm):
	def suggest(self):
		"""picks a value from 
		predifined ranges along each axis"""
		pass

	def wss(self):
		pass

	def update(self):
		pass

	def loop(self):
		print("RandomSearch is now running")



class GridSearch(TuningAlgorithm)
	def __init__(self, ranges):
		"""create list of values
		based on provided ranges"""

		# TO-DO
		self.list = None

		pass

	def suggest(self):
		"""picks a value from 
		predifined list """
		return next(self.list)

	def wss(self):
		pass

	def update(self):
		pass

	def loop(self):
		print("GridSearch is now running")



class VanillaBO(TuningAlgorithm)
	def suggest(self):
		"""picks next val by maximing
		acquisition function"""
		pass

	def wss(self):
		pass

	def update(self):
		"""Updates simple Gaussian Process
		parameters to have an improved
		acquisition function for next cycle""" 
		pass

	def loop(self):
		print("VanillaBO is now running")

		








if __name__ == '__main__':
	r = RandomSearch()
	r.run_algorithm_loop()

	t = TuningAlgorithm()

