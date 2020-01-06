import sys

#sys.path.insert(0, '/src/Logic/')

from src.Logic.TkinterImplementation import *

#from TkinterImplementation import *

newWindow = TkinterImplementation('test', '500x500')

newWindow.New_Label('test',2,0)

#button1 = newWindow.New_Button('test', print('testo'),2,4)

#button1.pack()

newWindow.MainLoop()
