import os
from src.compare import Comparison
"""

Input/Output

Author : Danwand NS github.com/DanBrown47

This package deals with the Input/output
of the software. Writes to a file, Read from the file 
Flushes the file

"""

class IO():
    """
    The class of Input/Output
    """

    def __init__(self, path:'str', data:'str') -> None:
        self.path = path
        self.data = data
        
    def isEmpty(self) -> bool:
        """
        Checks if the file is empty [Genisis stage]
        or contains JSON
        """
        print("Hey")
        size = os.path.getsize(self.path)
        if size == 0:
            return True
        else:
            return False



    def writeFile(self) -> None:
        """
        The function interacts with the undelying fs
        Writes to the file
        """
        try:
            file = open(self.path,"w")
            file.write(str(self.data))
            file.close()

        except Exception as e:
            print("Error on writing to file : " + str(e))

        

    def readfile(path) -> str:
        try:
            file = open(path, "r")
            fromFile = file.read()
            return fromFile
        except Exception as e:
            print("Error Reading the file" + str(e))
    def entrypoint(self) -> None:
        """
        Entrypoint serves to sync execution pattern of the IO
        """
        if not IO.isEmpty(self):
            eq = Comparison.compare(self.data, IO.readfile(self.path))
            

        else:
            print("Empty so writing")
            IO.writeFile(self)
