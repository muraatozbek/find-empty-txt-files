
import os
# in this example pos_21.txt is empty this program will remove pos_21.txt file

path="/path/of/file/text/" # give the path of txt file direction
for file in os.listdir(path):
    
    with open(os.path.join(path,file), "r") as f: #opens the direction and reads
        lines = f.readlines()
        
        # 
        if len(lines) == 0: #if the length of lines is 0 it removes the txt file and print what it removed
            print(file)
            os.remove(os.path.join(path,file))
                    

                    