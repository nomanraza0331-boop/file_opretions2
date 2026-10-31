import os
'''
os.chdir("D:\\FileOperations")
with open("employee.txt","r") as fr, open("Salary.txt","w") as fw:
    fileData=fr.readlines()
    for line in fileData:
        l=list(line.split())
        print(l)
        fw.write(f"{l[0]} {l[-1]}\n")
'''
class FileOprerathions:
    def __init__(self,source,dest):
        self.source=source
        self.dest=dest

    def CopyData(self):
        with open (self.source,"r")as fr, open(self.dest,"w")as fw:
            fileData=fr.readlines()
            for line in fileData:
                l=list(line.split())
                fw.write(f"{l[0]} {l[-1]}\n")


F1=FileOprerathions("employee.txt","salary.txt")
F1.CopyData()


        