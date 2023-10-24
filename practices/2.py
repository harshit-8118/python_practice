import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# st = input()
# v = [int(i) for i in st if i != ' ']
# print(v)
# print(st)
# print(type(v))
# for i in v:
#     print(i, end=' ')

# prev = 1
# curr = 2

# prev, curr = curr, prev
# print(prev, curr)
# prev, curr = curr, prev
# print(prev, curr)
# prev, curr = curr, prev
# print(prev, curr)

'''     question-1      '''
# n = int(input())
# a = [int(i) for i in input().split()]
# print(len(a))
# b = sorted(a)
# c = sorted(a, reverse=True)
# print(a)
# print(b)
# print(c)

'''     question-2    '''
# def partition(a, s, e):
#     temp = a[s]
#     j = s - 1
#     for i in range(s, e + 1):
#         if temp >= a[i]:
#             j += 1
#             a[j], a[i] = a[i], a[j]
    
#     a[s], a[j] = a[j], a[s]
#     return j

# def quicksort(a, s, e):
#     if s < e:
#         ind = partition(a, s, e)
#         quicksort(a, s, ind - 1)
#         quicksort(a, ind + 1, e)


# or
def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)-1]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    a = quicksort(a)
    print(a)


'''     question-3      '''
def func():
    a = list()
    print(a, type(a))
    b = list([1, 2, 3, 4, 5])
    print(b, type(b))
    c = list(1, 2, 2, 3, 34)
    print(c, type(c))

# func()


'''     question-4      '''
# l = [int(x) for x in input().split()]
# print(sum(l)/len(l))
# print(max(l))
# print(min(l))

'''     question-5      '''
# import random

# l = [int(x) for x in input().split()]
# random.shuffle(l)
# print(l)


'''     question-7      '''
# l = [1, 2, 3, 6, 5, 1, 7, 3]
# print(l[:-1])
# print(l[-4:-2])
# print(l[2:-3])


'''     question-7      '''
# def extendList(val, list=[]):
#     list.append(val)
#     return list

# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')
# print("list1 = %s" % list1)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)


'''     question-#      '''
# v = '.'*10
# print(v)
# # v[3] = '#'
# v = v[:3] + '#' + v[4:]
# print(v)


'''     question-8      '''
# class A():
#     x = 1

# a = A()
# print(a.x)

# b = [A()] * 10
# for i in b:
#     print(i.x, end=", ")

# print()
# b[2].x = 5
# for i in b:
#     print(i.x, end=", ")

# print()
# c = [A() for i in range(10)]
# for i in c:
#     print(i.x, end=", ")

# c[2].x = 5
# print()
# for i in c:
#     print(i.x, end=", ")


'''     question-9      '''
# class obj:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# if __name__ == '__main__':
#     objects = [obj(1, 2), obj(5, 4), obj(7, 3), obj(11, 42), obj(8, 0), obj(5, 9)]
#     aa = sorted(objects, key=lambda x: x.a)
#     bb = sorted(objects, key=lambda x: x.b)
#     for i in aa:
#         print("@ ", i.a, i.b)
#     for i in bb:
#         print("# ", i.a, i.b)



'''     question-10      '''
# s = "This is introduction to python for web development"
# print(s.split())


'''     question-12      '''
# string = "cabacdaegakialaop"
# print(string.split('a'))
# print(string.split('a', 2))
# print(string.split('a', 3))
# print(string.split('a', 12))
