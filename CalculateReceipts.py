
def fun(fileName):
    receiptCount=0
    receiptSum=0
    myfile = open(fileName, 'r')
    tmpLine=myfile.readline().strip()
    while tmpLine :
        parameters=tmpLine.split()
        if len(parameters) > 1:
            receiptSum+=int(parameters[0])*int(parameters[1]);
            receiptCount+=int(parameters[1])
        else:
            receiptCount+=1
            receiptSum+=int(tmpLine)
        tmpLine=myfile.readline().strip()
    print receiptCount,receiptSum


if __name__=='__main__':
    fileName="receipt.txt"
    fun(fileName)