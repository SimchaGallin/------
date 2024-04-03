
# שאלה מס 1

x = 0
y = 0
num = 0
while num >= 0:
    num = int(input('plurrdg:'))
    x = num % 10
    y = num // 10 % 10
    if x > 5 and y < 5:
        print(num)



# שאלה מס 2
        
def A(arr):
    for i in range(0,len(arr)//2):
        tamp_i = arr[i]
        arr[i] = arr[-i-1]
        arr[-i-1] = tamp_i
    return arr
print(A([1,2,3,4,5,6]))



# שאלה מס 3

def B(arr):
    con = 0
    num = None
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] != num:
            con += 1
            num = arr[i+1]
    return con

print(B([1,2,2,2,4,5,5,8,8,8]))


# שאלה מס 8

def N(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max_k = 0
    max_v = 0
    print(dic)
    for j in dic:
        if dic[j] > max_v:
            max_v = dic[j]
         


# שאלה מס 10

st={
    123:{"fN":["Asher"], "grades":{"math":88, "english":90, "asm":72}},
    456:{"fN":["Dan"], "grades":{"math":78, "english":89, "C#":72, "asm":95}},
    321:{"fN":["Shimon"], "grades":{"sql":77, "fullStack":99, "python":88, "asm":90}}
   }

def C(st):
    for v in st.values():
        g = list(v['grades'].items())
        print(v['fN'][0])
        for i in range(0,len(g)):
            print(g[i][0],g[i][1])


C(st)

# שאלה מס 11

a =[
    [4,6,1,2,0],
    [5,2,7,3,1],
    [0,5,4,3,2]
]

def show(a):
    for i in range(0,len(a)):
        sum = 0
        for j in range(0,len(a[0])):
            print(a[i][j],end=" ")
            sum += a[i][j]
        print(' ',sum)
        print()

show(a) 
            
            
            
