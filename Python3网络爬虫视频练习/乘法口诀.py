# -*-coding:utf-8-*-
__author__ = "Ink.white"

for i in range(1,10):
    for a in range(1,i+1):
        print(str(i) + "*" + str(a) + "=" + str(i*a),end=" ")
    print("")

print("-------------------------------------------------------------")
for k in range(9,0,-1):
    for v in range(1,k+1):
        print(str(k) + "*" + str(v) + "=" + str(k*v),end=" ")
    print("")