
#剑指offer第1题
#在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        flag = "false"
        row = len(array)
        col = len(array[0])
        if row==1 and col==0:
            return flag
        else:
            for i in range(row):
                for j in range(col):
                    if target == array[i][j]:
                        flag = "true"
                        break
            return flag

target=5
array=[[1,2],[2,5]]
row = len(array)
col = len(array[0])
print(row,col)
solution=Solution()
answer=solution.Find(target,array)
print((answer))

#调试成功！