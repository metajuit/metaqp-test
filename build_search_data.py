import os
import json

data=[]
def recur(cwd,tag):

	ls_elem=os.listdir(cwd)
	for elem in ls_elem:
		if(os.path.isdir(cwd+"/"+elem)):
			tag.append(elem)
			recur(cwd+"/"+elem,tag)
			tag.pop()
		else:
			if(elem[0]!="."):
				if(elem.find("(")!=-1):
					course=elem[:elem.find("(")]
					sem=elem[ elem.find("(",elem.find("(")+1)+1:elem.find(")",elem.find(")")+1) ]
					if(len(sem)!=5):
						sem=-1
					x={}
					if(tag!=[]):
						tag_len=len(tag)
						url="https://www.jyc.co.in/metaqp/"
						for part in tag:
							# for ch in part:
							# 	if(ch==' '):
							# 		url=url+'%20'
							# 	else:
							# 		url=url+ch
							url=url+part+"/"
						url=url+elem
						try:
							if(sem==-1):
								if(tag[tag_len-1]=="Done"):
									x={"Department":tag[tag_len-2],"Link":url,"Paper":course,"Semester":"","Year":tag[tag_len-3].replace("Done, ","")}
								else:
									x={"Department":tag[tag_len-1],"Link":url,"Paper":course,"Semester":"","Year":tag[tag_len-2]}
							elif(tag[tag_len-1]=="Done"):
								x={"Department":tag[tag_len-2],"Link":url,"Paper":course,"Semester":sem,"Year":tag[tag_len-3].replace("Done, ","")}
							else:
								x={"Department":tag[tag_len-1],"Link":url,"Paper":course,"Semester":sem,"Year":tag[tag_len-2].replace("Done, ","")}
						except:
							print("FILE ERROR : {}".format(elem))
							print("Tag->{}".format(tag))
					data.append(x)
				

				

def main():
	cwd=os.getcwd()
	tag=[]
	recur(cwd,tag)
	t=json.dumps(data)
	f=open("data/data.json",'w')
	f.write(t)
	f.close()
	print(t)

main()






# def recur(cwd):

# 	ls_elem=os.listdir(cwd)
# 	for elem in ls_elem:
# 		if(os.path.isfile(elem)):
# 			print (elem)
# 		else:
# 			recur(cwd+"/"+elem)
			