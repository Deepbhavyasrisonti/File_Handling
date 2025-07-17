with open("file1.txt","w")as f:
    f.write("welcome to coding class")
with open("file1.txt","r+")as f:
    data=f.read()
    print("previous:",data)
    new_data=data.replace("coding","file_handling")
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("file1.txt","r")as f:
    print("latest:",f.read())