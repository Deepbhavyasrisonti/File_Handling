#data comparitive deletion
with open("eg.txt","r")as f:
    lines=f.readlines()
with open("eg.txt","w")as f:
    for line in lines:
        if line.strip()!="5":
            f.write(line)