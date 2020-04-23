from projectq.ops import H, Measure
from projectq import MainEngine


def create_random_number(quantum_engine):
	qubit = quantum_engine.allocate_qubit()
	H | qubit
	Measure | qubit
	randomNumber = int(qubit)
	return randomNumber
	

quantum_engine = MainEngine()

rNumber = None

rNumber = create_random_number(quantum_engine)

quantum_engine.flush()
print("The random number is: ", rNumber)
