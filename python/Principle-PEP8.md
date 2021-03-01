# 首要原则 : Readability counts.

> 根据PEP 8编写。

## 代码布局

### 缩进

使用4个空格作为每一级的缩进。更推荐使用空格而非制表符。

```python
# Correct

# When called, ailgned with open delimiter
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# When creating, aligned with extra level of indentation
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    do_something()

my_list = [
    1, 2, 3,
    4,5, 6,
]
```

### 换行

请在适当的地方进行换行，最长的行长度不应该超过79个字符；说明文档内和注释行，则不应超过72个字符。

但不要在二元操作符后换行，保证操作符不要离操作数/变量太远。

```python
# Wrong
number =  (number_one +
           number_two +
           number_three)

# Correct
number = (number_one
          + number_two
          + number_three)
```
## 空白行

对于顶级方法和类的定义，上下各自空两行。

对于类内方法，上下各自空一行。
```python
...


def top_level_function():
    do_something()


class OneClass():
    
    def __init__(self, arg):
        self.arg = arg
    
    def another_function(self):
        do_another()


...
```

可以在类内或是顶级空间使用额外的空白行，来根据功能划分功能组。

### 编码

源码文件请始终使用UTF-8编码格式（对于Python2为ASCII）。

### 导入

通常情况下，在一行只导入一个包。

```python
# Correct
import sys
import os

# Wrong
import sys, os
```

当然，对于一个包内的多个方法，则可以在一行导入。

```python
# Correct
from subprocess import Popen, PIPE
```

包的导入必须在文件的开头部分，接在模块说明以及文档说明之后（如果有的话），在全局变量和常量声明之前。

使用空白行来进行包导入的分组。通常情况下，按照如下顺序进行分组：
- Python标准库
- 第三方库
- 本地/自定义库

```python
import sys
import os
import subprocess

import numpy as np
import pandas
import torch

import MyTools
import MyUtils
```

推荐使用绝对路径导入包，但使用相对路径导入仍然是可以接受的，尤其是在包的层级和结构过于复杂时，使用绝对路径导入会显得过分冗长。

```python
# Not Recommended But Acceptable if package level are too complex
from .ImportTools import *

# Recommended
from ImportTools import *
```

对于标准库来说，请避免复杂的调用方式，并使用绝对路径进行导入。

对于类的导入，如果类名无冲突，则直接导入类；若存在冲突，则导入包含类的包，再进行分别调用。

```python
# Non-Crash
from myclass import MyClass

# If Crash
import myclass
import anotherclass

mc = myclass.MyClass()
ac = anotherclass.MyClass()
```

应当避免直接使用`from <module> import *`导入，这会使得包的导入过程存在不可见的部分。

特殊情况： 如果需要使用模块级别的dunders（那些使用两个下划线包裹的特殊变量），请在导入之前进行赋值，但如果要从`__future__ `导入，则要放在这之后，样例代码如下：

```python
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

### 字符串的引号使用

单引号和双引号均可，无推荐。如果需要转义的引号，请使用另一种引号来避免使用反斜杠。

```python
# Correct
print("'Hello World'")  # if you'd like to print single quote
print('"Hello World"')  # if you'd like to print double quote

# Wrong
print("\"Hello World\"")  # this destorys the readability!
```

### 空格的使用

```python
# Correct 
spam(ham[1], {eggs: 2})

# Wrong
spam( ham[ 1 ], { eggs: 2 } )

# Correct
foo = (0,)

# Wrong
foo = (0, )

# Correct
if x == 4: print(x, y); x, y = y, x

# Wrong
if x == 4 : print( x , y ) ; x , y = y , x
```

切片是一种相对特殊且复杂的情况，请把冒号看成是一种二元操作符，保证冒号的两边有相同数量的空格。例外：当切片变量被省略时，那一侧的空格也同时需要被省略。

```python
# Correct
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# Wrong
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

不要试图用多个空格对齐变量的赋值。

```python
# Correct
x = 1
y = 2
long_variable = 3

# Wrong
x             = 1
y             = 2
long_variable = 3
```

对于这些二元操作符，请保证两侧始终留有一个空格：`=, +=, -=, ==, <, >, !=, <>, <=, >=, in, not, is, is not, and, or, not `

但当`=`应用于方法的默认的未指定类型的参数赋值时，请不要使用空格。
```python
# Correct
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
    
# Wrong
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```
又，如果该参数指定了类型且被赋予了默认值，则使用单个空格包裹`=`。
```python
# Correct
def munge(sep: str = None): ...
def munge(input: str, sep: str = None, limit=1000): ...

# Wrong
def munge(input: str=None): ...
def munge(input: str, limit = 1000): ...
```

当存在多种运算优先级的符号时，考虑在低优先级的符号两侧加入空格（即使他们本来并不需要空格），但不要使用多于一个的空格，也不要让二元操作符两侧的空格数量不等。

```python
# Correct
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# Wrong
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

## 注释

首字母请大写，但如果该单词是被定义的变量或是标识符，请不要改变大小写。
块注释的每一行都是用单个#和空格开头，每一句结尾都请使用句号。如果是多行注释，请在每一句的句号后面跟上两个空格（意义不明），最后一行不需要空格。
块注释使用包含单个#的单行来进行分段。

```python
# Here is paragraph one line one.  
# Here is paragraph one line two.
#
# Here is paragraph two line one.  
# Here is paragraph two line two.
```

请尽可能少地使用行内注释。行内注释至少要在该行末尾的两个空格后，使用单个#和空格开头。
务必假设看注释的人的代码水平不比你差，这意味着你不需要说明那些显而易见的现实。

```python
# Useless
x = x + 1   # Increase x

# Useful
x = x + 1   # Reward for x
```

### 文档字符串

对于公开/可见的模块，方法，或是类，请编写文档字符串。对于那些不可见，私有的，则不必要。当然，也非常推荐编写基本的文档，来保证阅读代码的人知道该模块做了什么。

使用三个双引号来编写文档字符串，并且在注释的最后一行，仅包含三个结束的双引号。如果是单行注释，则紧跟在同一行的最后。

该类注释应该紧跟在def行后。

```python
# Multi lines
def one_public_method():
"""Return a string

Here is what we do.
"""

# Single line
def one_public_method():
"""Return a string."""
```

## 命名规范

以下命名风格是推荐的：
```
y(single lowercase letter)
Y(single uppercase letter)
lowercase
lower_case_with_underscores
UPPERCASE
UPPER_CASE_WITH_UNDERSCORES
CamelCase
mixedCase
```
包和模块名应该使用短且全小写或带下划线的小写的命名格式。

类名应该使用驼峰命名格式。

不推荐使用全局变量，但可以在顶级空间定义全局常量，使用全大写或带下划线的大写命名格式。
方法名和变量名使用全小写或带下划线的小写的命名格式。

当变量名和保留关键字冲突时，请使用后置下划线来避免冲突，而不是使用自定的缩写和其他省略写法。例如对于关键字`class`，使用`class_`比使用`clss`更好。

对于私有的变量和方法，请使用起始下划线进行区分，例如`_score`。如果要避免与子类的冲突，可以使用两个连续的起始下划线，例如`Student`类的`__score`，这样，就不能通过`Student.__score`直接调用该属性（仍然可以使用`Student._Student__score`来访问，所以可能会导致一些问题，非必要不使用）
