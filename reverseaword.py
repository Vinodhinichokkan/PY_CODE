str = "Welcome to python progarmming"

words = str.split(" ")
print(words)  #['Welcome', 'to', 'python', 'progarmming']

words = words[-1::-1]
print(words)   #['progarmming', 'python', 'to', 'Welcome']

outputstr = ' '.join(words)
print(outputstr)  #progarmming python to Welcome