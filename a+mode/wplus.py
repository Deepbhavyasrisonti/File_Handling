with open("file1.txt","w+")as f:
    f.write("Hello Students!!!!")
    f.seek(0)
    data=f.read()
    print("previous:",data)
    new_data=data.replace("Students!!!!","future IT employees")
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("file1.txt","r")as f:
    print("latest:",f.read())