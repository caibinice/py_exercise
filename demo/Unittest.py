import unittest
import testMyFunc as my_func

# def my_div(a, b):
#     return a / b
#
# class TestFunc(unittest.TestCase):
#     def test_div(self):
#         self.assertEqual(2, my_div(2,0))
#         self.assertEqual(-2, my_div(2,-1))
#
#
#
# if __name__ == "__main__":
#     unittest.main()


class TestFunc(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(2, my_func.my_func1(1))
        self.assertEqual(3, my_func.my_func1(-1))
        for i in range(-100, 100):
            if i == 1 or i == -1:
                continue
            self.assertEqual(1, my_func.my_func1(i))

    def test_func2(self):
        self.assertTrue(my_func.my_func2("no"))
        with self.assertRaises(ValueError):
            my_func.my_func2("nononono")


# if __name__ == "__main__":
#     unittest.main()

# 定义一个 suite 替换 unittest.main()
suite = unittest.TestSuite()
suite.addTest(TestFunc('test_func2'))
unittest.TextTestRunner().run(suite)
