temp = open("arquivo.txt", "w")
temp.write(input("Digite algum texto: "))
temp.close()

temp2 = open("arquivo.txt","r")

print(temp2.readlines())

temp2.close()
