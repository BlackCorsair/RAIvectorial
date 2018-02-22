from pathlib import Path
class Controller:
	directory = ""
	def __init__(self):
		self.directory = "docrepository"
		print("Controller init")

	def main(self):
		print("Start of Controller main method...")
		print("Found the following files:")
		p = Path(self.directory)
		for i in p.glob('*.*'):
			print(i.name)

controller = Controller()
controller.main()