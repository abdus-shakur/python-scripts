def calculate(a,b,case1):
    match case1:
     case 'ADD':
        print("ADD : "+str(a)+":"+str(b))
     case 'SUB':
        print("SUB : "+str(a)+":"+str(b))
calculate(10,20,"ADD")
calculate(10,20,"SUB")