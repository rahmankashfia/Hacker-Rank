class BQueue:
	def __init__(self):
		self.q = []
		self.rear = 0
		self.front = 0


	def enqueue(self, i):
		self.q.append(i)
		self.rear = self.rear + 1

	def dequeue(self):
		if self.rear == self.front:
			print("Queue is empty")
		else:
			self.front = self.front + 1
		return self.q[self.front - 1]

	def printq(self):
		if self.rear == self.front: 
			print("Queue is empty")
		else:
			print(self.q[self.front:self.rear])


q1 = BQueue()
q1.printq()
q1.enqueue(10)
q1.enqueue(100)
q1.printq()
q1.enqueue(1000)
q1.enqueue(10000)
q1.printq()
q1.enqueue(100000)
q1.printq()
q1.dequeue()
q1.printq()
q1.dequeue()
q1.printq()
q1.dequeue()
q1.printq()
q1.dequeue()
q1.printq()
q1.dequeue()
q1.printq()


