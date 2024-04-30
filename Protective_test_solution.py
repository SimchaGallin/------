
 1 שאלה מס 

כתוב קטע תוכנית שתקלוט מהמשתמש מספרים שלמים,עד שיקלט ערך שלילי
על התוכנית להציג את כל המספרים שסיפרת האחדות שלהם גדולה מ-5 וסיפרת העשרות שלהם קטנה מ-5

# פיתרון

x = 0
y = 0
num = 0
while num >= 0:
    num = int(input('Please enter a number:'))
    x = num % 10
    y = num // 10 % 10
    if x > 5 and y < 5:
        print(num)




2  שאלה מס 

כתוב פעולה המקבלת רשימה של מספרים שלמים, והופכת את כל האיברים בצורת מראה 
לדוגמא עבור רשימה[2,5,6,7,8,1]
נקבל[1,8,7,6,5,2]

# פיתרון

def A(arr):
    for i in range(0,len(arr)//2):
        tamp_i = arr[i]
        arr[i] = arr[-i-1]
        arr[-i-1] = tamp_i
    return arr
print(A([1,2,3,4,5,6]))



שאלה מס 3
כתוב פעולה המקבלת רשימה של מספרים ממוינים מהקטן לגדול
על הפעולה להחזיר את מספר הערכים שמופיעים יותר מפעם
לדוגמא עבור הרשימה[3,5,5,7,9,11,33,44,44,44,55,66,66]
הפעולה תחזיר 3

# פיתרון

def B(arr):
    con = 0
    num = None
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] != num:
            con += 1
            num = arr[i+1]
    return con

print(B([1,2,2,2,4,5,5,8,8,8]))

 שאלה מס 5
כתוב את הפלט של התוכנית הבאה

names = ['gad','david','yaakov','avraham']
le = []
for name in names:
    le.append(len(name))
print(le)

num = 31
bn = ' '
while num > 0:
    digit = num % 2
    num = num // 2
    bn = str(digit) + bn
print(bn)

# פיתרון

print(el)

# :פלט

[3,5,6,7]

print(bn)

#  :פלט

"11111"



שאלה מס 8

נתונה מחלקה Test
הכוללת שתי תכונות שם המקצוע והציון 

class Test:
    def __init__(self,subject,grade)
        self.subject = subject
        self.grade = grade

כתוב פעולה המקבלת רשימה של הפניות ומציגה את הציון הכי נפוץ
הנח שכל הציונים הם ערכים שלמים בן 0 ל-100

# פיתרון

def N(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i.grade] += 1
        else:
            dic[i.grade] = 1
    max_k = 0
    max_v = 0
    print(dic)
    for j in dic:
        if dic[j] > max_v:
            max_v = dic[j]

'------------------------------------------------------------'
# פתרון לשאלה מס׳ 8 תחת מגבלות זמני הריצה שניתנו

# Define a class named Test
class Test:
    # The constructor method for the class, which initializes the instance with a subject and a grade
    def __init__(self, subject, grade):
        self.subject = subject  # Assign the subject argument to the instance's subject attribute
        self.grade = grade  # Assign the grade argument to the instance's grade attribute

# Create instances of the Test class, each representing a different test with a subject and a grade
t1 = Test('math', 90)
t2 = Test('history', 80)
t3 = Test('english', 95)
t4 = Test('biology', 75)
t5 = Test('chemistry', 80)

# Store the instances in a list
arr = [t1, t2, t3, t4, t5]

# Define a function named most that takes a list of Test instances as an argument
def mostCommon(arr):
    dct = {}  # Initialize an empty dictionary to store the grades and their frequencies

    # For each test in the list, add the grade to the dictionary with a count of 0
    for i in arr:
        dct[i.grade] = 0

    # For each test in the list, increment the count of the grade in the dictionary
    for j in arr:
        dct[j.grade] += 1

    most = 0  # Initialize a variable to store the highest frequency
    grade = 0  # Initialize a variable to store the grade with the highest frequency

    # For each grade in the dictionary, if its frequency is higher than the current highest frequency,
    # update the highest frequency and the grade with the highest frequency
    for key in dct:
        if dct[key] > most:
            most = dct[key]
            grade = key

    # Print the grade with the highest frequency
    print(grade)

# Call the most function with the list of Test instances as an argument
mostCommon(arr)


# שאלה מס 9

print(ntext)

#  :פלט

"rujfpvlmhw"



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



