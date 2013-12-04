import user_input

readByte=open("server.cfg","rb")       #read file
data = readByte.read()
readByte.close()

spl = data.split(";")

user_input.main(("localhost", 12345),(spl[0], int(spl[1])))
