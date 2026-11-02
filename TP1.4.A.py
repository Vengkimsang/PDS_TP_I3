print(" Part A. Copy the table into your notebook. Predict the result of each expression first, then check it in Python.")

a = int("7") + 3.5
b = str(10) * 3
c = bool(""), bool(" ")
d = int(3.99)
e = float("1e3")
f = int(True) + float("2.5")
g = round(2.5), round(3.5)
h = type(10 / 2)
print("Expression" + " "*15 +  "Your prediction" + " "*15 + "Python's answer")
print("int(\"7\") + 3.5 " + " "*10 + "10.5" + " "*25 ,a )
print("str(10) * 3" + " "*14 + "error" + " "*24 ,b )
print("bool(""), bool(" ")" + " "*12 + "\" \"" + " "*24 ,c )
print("int(3.99)" + " "*18 + "3" + " "*26 ,d )
print("float(\"1e3\")" + " "*15 + "1e3" + " "*24,e) 
print("int(True) + float(\"2.5\")" + " "*3 + "2.5" + " "*24,f)
print("round(2.5), round(3.5)"  + " "*5 + "3,4" + " "*24,g)
print("type(10 / 2)" + " "*14 + "int" + " "*24,h)
