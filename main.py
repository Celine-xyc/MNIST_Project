# 第一课：认识变量
name = "python"
number = 10
print("我正在学习",name)
print("数字是",number)
print("数字加5等于",number+5)
# 第二课：列表和循环
numbers = [1,2,3,4,5]
for number in numbers:
    print("当前数字是",number)
print("全部打印完毕！")
# 第三课 条件判断
number = 7
if number >5:
    print("这个数字大于5")
else:
    print("这个数字小于或等于5")
print("判断结束")
#第四课 学习函数
def say_hello():
    print("你好,欢迎学习python")

say_hello()
say_hello()
say_hello()
def greet(name):
    print("你好，"+name+"!")

greet("小红")
greet("小明")
greet("戴安娜")
def multiply(a,b):
    return a * b

result = multiply(4,3)
print(result+2)
def calculate(a,b=10):
    return a+b

print(calculate(5))
def greet():
    message = "你好"
    print(message)

greet()
name = "小米"
def greet():
    print("你好，",name)

greet()
print(name)
import math
number = 16
result = math.sqrt(number)
print(result)
from calculator import add

print(add(3,5))
#第八课python如何读写文件
with open("hello.text","w") as file:
    file.write("你好,python")
with open("hello.text","r") as file:
    content = file.read()

print(content)
with open("hello.text","a") as file:
    file.write("我在学习文件操作")
with open("hello.text","w") as file:
    file.write("我好累呀")
with open("hello.text","a") as file:
    file.write("\n我还在学习文件操作")
try:
    number = int("123")
    print(number)

except ValueError:
    print("转换失败")

print("程序结束")
try:
    with open("missing.txet","r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("文件不存在")

print("程序结束")
#第十课 列表进阶
numbers = [1,2,3]
numbers.append(4)
print(numbers)
numbers = [1,2,3,4]
numbers.remove(3)
print(numbers)
fruits = ["苹果","香蕉","柿子"]
print(fruits[0])
print(fruits[2])
fruits = ["苹果","香蕉","橘子"]
print(len(fruits))
numbers = [1,2,3,4]
numbers.append(20)
print(len(numbers))
fruits = ["苹果","香蕉","橘子"]
for fruit in fruits:
    print(fruit)
numbers = [1,2,3,4,5,6]

for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        print(f"失败{number}!")
#第十一课 字典（dict)
student = {
    "name":"小明",
    "age":18,
    "score":90
}
print(student["name"])
print(student["age"])
person = {"name":"小红","age":"20"}
person["age"] = 21
print(person["age"])
person = {"name":"小红","age":20}
person["city"] = "东京"
print(person)
student = {"name":"celine","score":100}
student["score"] = 95
student["age"] = 18
del student["name"]
print(student)
print(len(student))
for value in student:
    print(value)
#第十二课 列表和字典结合使用
students = [{"name":"anne","score":90},
            {"name":"tonny","score":"80"},
            {"name":"celine","score":"100"}]
for student in students:
    print(student["name"],student["score"])
