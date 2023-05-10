class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # 这里我们得处理一个异常
        if b == 0:
            print("b cannot be 0")
        else:
            return a / b

    def mod(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b

    def divideToInt(self, a, b):
        if b == 0:
            print("b cannot be 0")
        else:
            return a // b

    def batch_subtract(self, a_list, b_list):
        res_list = []
        for i in range(len(a_list)):
            res_list.append(self.subtract(a_list[i], b_list[i]))
        return res_list

# 生产一个实例
c = Calculator()
print(c.add(1, 2))
print(c.divide(1, 2))
c.divide(1, 0)

print(c.subtract(2,1))
print(c.batch_subtract([3,2,1], [2,3,4]))