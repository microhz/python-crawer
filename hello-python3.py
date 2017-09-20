#!/usr/local/bin/python3
# print ("hello")

# b = 0
# l = [1,2,3,4]
# if (b in l) :
#     b = True
# else :
#     b = False
# if b : 
#     print ("this is true code..")
# else : 
#     print ("this is false code..")

# # this is 注释
# print ("this is print")

# s = "a " + \
#     "b " + \
#     "c "
# print (s)

# s = "abcdefg"
# print (s[2:])
# print (s[3:5])

# ## r可以拒绝转义
# s2 = r"this is lint \n"
# print (s2)

# s3  = "this is \n s"
# print (s3)

# s4 = u"this is unicode.."
# print (s4)

# # input("put enter and exit..")

# s5 = "a"
# print (s5);print (s4) ##一行写多个代码

# # import sys
# # for i in sys.argv :
# #     print (i)
# # print (sys.path)

# from sys import argv, path
# print (path)

# ## 数组
# list = [1,2,3]
# print (list * 2)

# ## 哈西表 
# d = {1:"a",2 : "b"}
# for i in d.keys() :
#     print ("key " + str(i))
#     print ("val " + d[i])

# ## 元组, 与列表类似,但是不能修改
# s = ("a","c", "d", 2, 4)
# if ("a" in s) :
#     print ("a is in")
# else :
#     print ("a not in")

# ## Set
# s = {"a","c","d",2, 4}
# s2 = {"a", "f", "g"}
# print (s & s2)
# print (s | s2)
# print (s - s2)
# print (s ^ s2)


# # class Solution:
# #     # array 二维列表
# #     def Find(self, target, array):
# #         # write code here
# #         for row in array : 
# #             for j in row : 
# #                 if (j == target) :
# #                     return True
# #         return False

# # # -*- coding:utf-8 -*-
# # class Solution:
# #     # s 源字符串
# #     def replaceSpace(self, s):
# #         # write code here
# #         return s.replace(" ", "%20")

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         # write code here
#         list = []
#         p = listNode
#         while (p != None) :
#             list.append(p.val)
#             p = p.next
#         for i in range(len(list)) :
#             j = len(list) - i - 1
#             if (i <= j) :
#                 t = list[i]
#                 list[i] = list[j]
#                 list[j] = t
#         return list


# n = ListNode(1)
# n.next = ListNode(2)
# n.next.next = ListNode(3)
# s = Solution()
# l2 = s.printListFromTailToHead(n)
# print (l2)
# print (n.val, n.next.val, n.next.next.val)


# sum = 0
# for i in range(0,101) :
#     sum += i
# print ("1 + 2 + .. + 100 is ",sum)


# import time
# print (time.time())

# localtime = time.localtime(time.time())
# year,day = localtime.tm_year,localtime.tm_mday
# print ("this is local time " + str(year) + str(day))



# def printStr (str) :
#     print ("this string is ", str)

# printStr("micro")

# list = [1,2,3]
# def appendList (list) :
#     list.append([4,5,6])
# print (list)
# appendList (list)
# print (list)

# 不定长参数
# def p (* list) :
#     for i in list :
#         print (i)

# p ([1,2,3])


## 函数编程
# def fun2(list, p) : 
#     max,min = list[0],list[0]
#     for i in list :
#         if (max < i) :
#             max = i
#         elif (min > i) :
#             min = i
#     p(max, min)
# fun2([5,2,4,5,6,7],lambda max,min:print("max is " + str(max) + ",min is " + str(min)))


## 全局与局部变量
# total = 0
# def s2() :
#     # 函数内部的变量名如果第一次出现，且出现在=前面，即被视为定义一个局部变量
#     # 函数内部的变量名如果第一次出现，且出现在=后面，且该变量在全局域中已定义，则这里将引用全局变量
#     # x = total
#     # total = 20
#     # print(x)
#     global total #global可以给全局变量赋值
#     total = 100
#     print (total)
# s2()
# print(total)

# def s(p1,p2="g") :
#     print("p1 ",p1)
#     print("p2 ",p2)

# s(p1="k",p2="b")

# print("hello world!")


# def s(p="a", p2="b") : 
#     print(p,p2)
# s("1","2")


# s = "hello world"
# print(s.title())

# for c in s :
#     print(c)

# s = "NI HAO"
# print(s.lower())
# s = "abcdef"
# print(s[:3])

# list = [1,2,3,4,5]
# for s in list : 
#     print(s)
# print(list)

# print(list[2:])

# print("遍历截取后的列表")
# for i in list[2:] :
#     print(i)


# def sumList(list) :
#     sum = 0
#     for i in list :
#         sum = sum + i
#     return sum

# l = [1,2,3]
# s = sumList(l)

# print(s)

# import urllib.request

# def http(url) :
#     return urllib.request.urlopen(url)

# print(http("http://www.baidu.com").read().decode("utf_8"))

# for i in range(1,5) :
#     for j in range(1,5) :
#         for k in range(1,5) :
#             if (i != j and j != k and i != k) :
#                 print(i, j, k)


# def getOut(income) :
#     sum = 0
#     if (income > 1000000) :
#         sum += (income - 100000) * 0.01
#         income -= 400000
#     if (income <= 600000) :
#         sum += (income - 400000) * 0.015
#         income -= 2000
#     if (income <= 400000) :
#         sum += (income - 200000) * 0.05
#         income -= 200000
#     if (income <= 200000) :
#         sum += (income - 100000) * 0.075
#         income -= 100000
#     if (income <= 100000) :
#         sum += (income - 100000) * 0.1
#     return sum

# income = 170000 # 这是金额

# sum = 0
# if (income > 100000) :
#     sum += 100000 * 0.1
#     if (income > 200000) :
#         sum += (200000 - 100000) * 0.075
#         if (income > 400000) :
#             sum += (400000 - 200000) * 0.05
#             if (income > 600000) :
#                 sum += (600000 - 400000) * 0.015
#                 if (income > 1000000) :
#                     sum += (income - 1000000) * 0.1
#             else :
#                 sum += (income - 400000) * 0.015
#         else :
#             sum += (income - 400000) * 0.05
#     else :
#         sum += (income - 100000) * 0.075
# else :
#     sum += income * 0.1
# print(sum)



# x + y = 7, x - y = 1
# 2x + y = 4  x + 2y = 5
# import numpy as np
#     a = np.mat('2,1;1,2')
#     b = np.mat('4,5').T
#     r = np.linalg.solve(a.b)
#     print(r)
# for x in range(0, 4) :
#     for y in range(0, 5) :
#         if (2 * x + y == 4 and x + 2 * y == 5) :
#             print(x, y)
# for x in range(0, 8) :
#     for y in range(0, 8) :
#         if (x - y == 1 and x + y == 7) :
#             print("x = " + str(x), "y = " + str(y), " 满足条件")
#设有整数i，i+100是一个完全平方数，再加168又是一个完全平方数，求出该整数的值。
# def isASqure(number) :
#     j = 0
#     while (j ** 2 < number) :
#         j = j + 1
#         if (j ** 2 == number) :
#             print(str(number) + " sq " + str(j))
#             return True
#     return False

# def getNum() :
#     i = 0
#     while (True) :
#         n1 = i + 100
#         n2 = n1 + 168
#         if (isASqure(n1) and isASqure(n2)) :
#             return i
#         i = i + 1

# r = getNum()
# print(r)

# import time
# d = time.localtime(time.time())
# print(d.tm_yday)


# for i in range(0,10) :
#     for j in range(0,i + 1) :
#         print(str(i) + " x " + str(j) + " = " + str(i * j) + ",", end="")
#     print("\n")



# def f_number(n):
#     f_1 = 0
#     f_2 = 1
#     f_3 = 0
#     for i in range(0,n + 1):
#         if i == 0:
#             f_3 = 0
#         elif i == 1:
#             f_3 = 1
#         else:
#             f_3 = f_1 + f_2
#             f_1 = f_2
#             f_2 = f_3
#     return f_3

# a = f_number(2)
# print(a)

# 0,1,1,2,3,5....
# def get_fibonacii(n) :
#     if (n == 0) :
#         return 0
#     elif (n == 1) :
#         return 1
#     else :
#         f1,f2,f3 = 0,1,1
#         for i in range(2, n) :
#             temp = f2
#             f2 = f3
#             f3 = f3 + temp
#         return f3
# print(get_fibonacii(4))

# l = [1,2,3,4]

# l2 = [[1,2,3,4],[2,3,4],[3,4,5]]
# for i in l2 :
#     for j in i :
#         print(j)

# def replaceSpace(s):
#     l_1 = s.split()
#     l_2 = l_1[0]
#     l_3 = "%20"
#     for i in l_1[1:]:
#         l_2 = l_2 + l_3 + i
#     return l_2

# print(replaceSpace(" i love you..."))


# def replaceSpace(s):
#     new_s = ""
#     for i in range(0, len(s)):
#         if s[i] == " ":
#             new_s += "20%"
#         else:
#             new_s += s[i]
#     return new_s
# print(replaceSpace(" i love you..."))

# def Power(base, exponent):
#     if exponent < 0:
#         n = 1 / base
#         e = - exponent
#     else:
#         n = base
#         e = exponent
#     if e == 0:
#         return 1
#     elif e == 1:
#         return n
#     else:
#         s = n
#         for i in range(2,e+1):
#             n *= s
#         return n

# def Power(base, exponent) :
#     if (exponent == 0) :
#         return 1
#     n = get_fabs(exponent)
#     temp = base
#     for i in range(0, n - 1) :
#         base *= temp
#     if (exponent < 0) :
#         return 1 / base
#     return base

# def get_fabs(n) :
#     if (n < 0):
#         return -n
#     return n

# def GetLeastNumbers_Solution(tinput, k):
#     if (len(tinput) < k) :
#         return []
#     k_min_list = []
#     list = tinput
#     for i in range(0, k) :
#         min = get_min(list)
#         k_min_list.append(min)
#         list = remove_min_from_list(list, min)
#     return k_min_list
# def remove_min_from_list(list, min) :
#     l = []
#     for i in list :
#         if (i != min) :
#             l.append(i)
#     return l
# def get_min(list) :
#     min = list[0]
#     for i in list :
#         if (i < min) :
#             min = i
#     return min

# list = [6,3,4,6,7,2,2,4,1]
# print(GetLeastNumbers_Solution(list, 3))

# def gcb(m , n):
#     if n == 0:
#         m, n = n, m
#     while m != 0:
#         m = n % m
#         n = m
#         print(m,n)
#     return n

# print(gcb(4, 6))
# class Node: #创建结点
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next
#     def get_value(self):
#         return self.value

#     def get_next(self):
#         return self.next

# class Linelist: #单链表类
#     def __init__(self): #链表初始化，创建空链表
#         self.head = None #定义表头？
#     def list_length(self): #获取链表长度
#         p = self.head
#         length = 0 
#         while p != None:
#             length += 1
#             p = p.next
#         return length

# ## 这里构造一个链表，1，2，3 head是指向头节点的引用
# head = Node(1, Node(2, Node(3)))

# ## 初始化一个链表类
# l = Linelist()
# # 给这个链表类传递链表的头引用
# l.head = head
# # 调用这个对象的方法获取长度
# print(l.list_length())

## 定义一个节点
# class Node :
#     def __init__(self, data, next = None) :
#         self.data = data
#         self.next = next 

# ## 构造一个链表
# head = Node("a", Node("b", Node("c", Node("d"))))
# ## 遍历这个链表
# index = 0
# p = head
# while p != None :
#     print("node index " + str(index) + " data is " + str(p.data))
#     p = p.next
#     index += 1

# ## 定义一个函数，获取第n个节点
# def get_index_node(head, n) :
#     index = 1
#     while index < n :
#         head = head.next
#         index += 1
#     return head  ## 此时head指向的第n个节点

# ## 翻转链表,翻转后的链表头引用为head2 ,暂时先指为空
# head2 = None
# ## 获取链表的长度
# def get_len(head) :
#     index = 0
#     while head != None :
#         index += 1
#         head = head.next
#     return index

# ## 传入开始定义的链表头的引用,获取链表长度
# len = get_len(head)
# p = None
# for i in range(0, len) :
#     index = len - i ## index就是我要获取的节点
#     node = get_index_node(head,index)
#     if (index == len) :
#         head2 = Node(node.data)
#         p = head2
#     else :
#         p.next = Node(node.data)
#         p = p.next

# ## 翻转结束
# while head2 != None :
#     print(head2.data)
#     head2 = head2.next
    
# 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
# 函数返回True/False
# def duplicate(numbers, duplication):
    
#     for i in numbers :
#         count = 0
#         for j in numbers :
#             if (i == j) :
#                 count += 1
#         if (count > 1) :
#             duplication[0] = i
#             return True
#     return False

# l = [2,1,3,1,4]
# l2 = [1]
# print(duplicate(l, l2))
# print(l2)


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# n = ListNode("a")
# n2 = ListNode("b")
# n3 = ListNode("c")
# n.next = n2
# n2.next = n3

# def FindKthToTail(head, k):
#     m = get_length(head)
#     if k < 0 or k > m:
#         return False
#     n = m - k
#     t = 0
#     p = head
#     while t != n:
#         p = p.next
#         t += 1
#     return p

# def get_length(head):
#     p = head
#     length = 0
#     while p is not None:
#         length += 1
#         p = p.next
#     return length

# # 定义一个head引用指向第一个节点
# head = n
# k = FindKthToTail(head,2)
# print(k.val)

# a = 1
# def incre(n) :
#     n += 1
# incre(a)
# print(a)

# class User :
#     def __init__(self,name) :
#         self.name = name


# def change_name(user, name) :
#     user.name = name

# u = User("micro")
# change_name(u, "zhou ning")
# print(u.name)

# class Node : 
#     def __init__(self, val, next = None) :
#         self.val = val
#         self.next = next

#     def get_val(self) :
#         return self.val

#     def set_next(self, next) :
#         self.next = next

#     def get_next(self) :
#         return self.next


# class LinkedList :
#     def insert_node_into(self, head, index, node) :
#         # if (index < 0 or index > self.get_len(head)) :
#         #     return
#         if (index == 1) :
#             node.set_next(head)
#             head = node
#         else :
#             p = head
#             count = 0
#             while (p != None) :
#                 count += 1
#                 if (count == index - 1) :
#                     ## 插入的位置 
#                     node.set_next(p.get_next())
#                     p.set_next(node)
#                 p = p.get_next()
#         return head

    # def get_len(self, head) :
    #     if (head == None) :
    #         return 0
    #     p = head
    #     count = 0
    #     while (p.get_next() != None) :
    #          count += 1
    #          p = p.get_next()
    #     return count

# l = LinkedList()
# head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# head = l.insert_node_into(head,2, Node(9))

# p = head
# while (p != None) :
#     print("node val is : " + str(p.get_val()))
#     p = p.get_next()

# print("end")
# n1 = Node(1, Node(2, Node(3)))
# p = n1
# while (p != None) :
#     print("node is " + str(p.get_val()))
#     p = p.get_next()

# 5
# p = n1
# p.set_next(p.get_next().get_next())

# print("移除第二个元素")

# while p != None :
#     print(" node is " + str(p.get_val()))
#     p = p.get_next()

# print("end...")

# def yield_test() :
#     yield 1
#     yield 4
#     yield 7

# for i in yield_test() :
#     print(i)

# def b_list(list_1):
#     n = len(list_1)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if list_1[j] < list_1[j + 1]:
#                 list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]


## 插入排序
# def insert_sort(list):
#     new_list = [list[0]]
#     for s in list[1:]:
#         count = 0
#         for n in new_list:
#             if s < n:
#                 new_list.insert(count, s)
#                 break
#             count += 1
#         if count == len(new_list):
#             new_list.append(s)
    
#     return new_list


# l = [1,5,6,2,8,0]
# l = insert_sort(l)
# print(l)


class Node :
    def __init__(self, data, left = None, right = None) :
        self.data = data
        self.left = left
        self.right = right

root = Node(4, Node(7, Node(8, Node(3), Node(1, Node(11, Node(15)))), Node(5, Node(2,None, Node(7)), Node(6))))

a = "s"
print(isinstance(a, tuple))
a = [1,2,3]
print(isinstance(a, tuple))
a = (1,2)
print(isinstance(a, tuple))