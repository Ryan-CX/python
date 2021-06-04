def caseTransfer(text,text2):
    count = 0
    for i in range(len(text)):
        if text[i]!=text2[i]:
            count+=1
    print(count)
    
    

caseTransfer('river','rover')