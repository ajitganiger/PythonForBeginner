__author__ = 'aganiger'


def displayContent(filename):
    file = open(filename, "r")
    print(file.read())
    file.close()

def appendFileContent(filename,data):
    file = open(filename, "a")
    file.write(data)
    file.close()
    displayContent(filename)

def main():
    displayContent("D:/Data/Office/Automation/Training/com.learning/basic/ConvertingList.py")
    appendFileContent("D:/Data/Office/Automation/Training/com.learning/basic/ConvertingList.py","\n# this is new text added by progress")


main()


