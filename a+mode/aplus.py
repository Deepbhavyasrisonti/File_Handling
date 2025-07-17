with open ("log.txt","a+")as f:
    f.write("\n Latest line ..............")
    f.seek(0)
    data=f.read()
    print("current data:\n",data)