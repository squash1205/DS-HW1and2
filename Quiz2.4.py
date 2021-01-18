class Node:
    # 定义节点，节点值为数据，nextval为下一个节点，dataval为元素值
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class singleLinkedList:
    # 定义单链表（表头）
    def __init__(self):
        self.headval = None

    # 定义遍历并打印链表的函数
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # 定义寻找最大值的函数
    def maxValue(self):
        max = self.headval.dataval
        listvalue = self.headval
        while listvalue is not None:
            val = listvalue.dataval
            if val >= max:
                max = val
            listvalue = listvalue.nextval
        print(max)


# 创建一个单链表（表头）
list1 = singleLinkedList()
list1.headval = Node(1)

# 创建节点
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(3)
node5 = Node(2)
node6 = Node(1)

# 将节点连接到表上
list1.headval.nextval = node1
node1.nextval = node2
node2.nextval = node3
node3.nextval = node4
node4.nextval = node5
node5.nextval = node6

# 打印检查节点是否正确连接
list1.listprint()
# 打印最大值
print("最大值为：")
list1.maxValue()
