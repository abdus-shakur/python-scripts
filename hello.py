print("test")
#  String
test = "value"
print (test+test)
# Array
var1 = [1,21,123,15]
print(var1[1])
for x in var1:
    print(x)

import time
start = time.time()

for i in range(10):
   for e in range(i):
       if (e*i)%2 == 0:
           print(e*i)

end = time.time()
print(end - start)