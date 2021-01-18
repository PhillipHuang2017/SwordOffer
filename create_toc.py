import os, re

articleProg = re.compile(r"^([0-9]{1,3}.*)(.md)$")

def createToc():
    fileList = os.listdir("./")
    fileList = list(filter(lambda x: True if articleProg.fullmatch(x) else False, fileList))
    fileList.sort(key=lambda x: int(x.split(".")[0]))
    writeLines = []
    for filename in fileList:
        name = ".".join(filename.split(".")[:-1])
        writeStr = "[%s](%s)\r"%(name, filename)
        writeLines.append(writeStr)
    
    with open("./TOC.md", "w") as tocFile:
        tocFile.writelines(writeLines)

if __name__ == "__main__":
    createToc()