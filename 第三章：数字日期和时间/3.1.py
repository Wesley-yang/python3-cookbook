#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

# 数字的四舍五入，对浮点数进行制定精度的舍入运算
# 对于简单的舍入运算，使用内置的round(value,ndigits)函数即可。比如：
print(round(1.23, 1), round(1.3454, 2))
# 当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。 也就是说，对1.5或者2.5的舍入运算都会得到2。
print(round(1.5, 0), round(2.5, 0))

# 传给 round() 函数的 ndigits 参数可以是负数，这种情况下， 舍入运算会作用在十位、百位、千位等上面。比如：
print(round(12405, -1), round(12340, -2))

# 不要将舍入和格式化输出搞混淆了。 如果你的目的只是简单的输出一定宽度的数，你不需要使用 round() 函数。 而仅仅只需要在格式化的时候指定精度即可。比如：
x = 1.3456
print(format(x, '0.2f'), format(x, '0.3f'))
print('value is {:0.3f}'.format(x))
# 同样，不要试着去舍入浮点值来”修正”表面上看起来正确的问题。比如，你可能倾向于这样做：
a = 2.1
b = 4.2
print(a + b, round(a + b, 2))
"""
对于大多数使用到浮点的程序，没有必要也不推荐这样做。 尽管在计算的时候会有一点点小的误差，但是这些小的误差是能被理解与容忍的。
如果不能允许这样的小误差(比如涉及到金融领域)，那么就得考虑使用 decimal 模块了，下一节我们会详细讨论。
"""
