from turtle import clear
import getIpynb


inputfileObject = open('input.txt','r')
ls=inputfileObject.readlines()

snippetList=[]
#print(ls)

def addCell(checkIfQuery,lineSnippet):
    
    global snippetList
    #lineSnippet=lineSnippet.replace("\'",'\\"')
    if checkIfQuery==True:
        lineSnippet=lineSnippet.replace("\'",'\"')
        snippetList.append(getIpynb.Cell("code",lineSnippet))
    else:
        snippetList.append(getIpynb.Cell("markdown",lineSnippet))

checkIfQuery=False
lineSnippet=""
for x in ls:
    x=x.strip(" ").strip("\n")
    if(checkIfQuery):
        #append line snippet
        if(x.startswith('`')==False or x==""):
            addCell(checkIfQuery,lineSnippet.strip())
            lineSnippet=""
            checkIfQuery=False
        else:
           lineSnippet=lineSnippet+"\n"+x.strip('`') 
    else:
        if(x.startswith('cluster(') or x.startswith('let ') or x.startswith('`')):
            addCell(checkIfQuery,lineSnippet)
            lineSnippet=x.strip('`')
            checkIfQuery=True
        else:
            lineSnippet=lineSnippet+"\n"+x.strip('`')

addCell(checkIfQuery,lineSnippet)

file1 = open("JupyterFile.ipynb", "w") 
file1.write(str(getIpynb.getIpynb(snippetList)))
