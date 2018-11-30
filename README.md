# Python3.6

## 学习爬虫
------
>由于爬虫经常需要自己拼接头部信息等字符，而这些信息一般都是key-value形式(字典)，每次都需要处理过，例如字符两边添加引号或者行尾加逗号。
尝试了多种批量处理的方法，现在本人只了解到一种一次性处理的方法，其他的都需要挺多的步骤。

> 打开`notepad++`
将待处理的字符复制到`notepad++`中
例如：
```
offset: 0
format: json
keyword: 街拍
autoload: true
count: 20
cur_tab: 1
from: search_tab
```

> 按`CTRL+F`呼出替换，将查找模式选为正则表达式
查找目标设置为
```re
\s*(.*?)\s*:\s*(.*?)\s*$
# 其中\s*用来匹配多余空格
# ()中内容表示需要匹配的字符 $字符匹配末尾
```
> 替换目标设置为
```re
'$1':'$2',
# ''代表我们需要在字符两边加上的引号
# $1匹配的是上述()内的内容，如有多个括号则用$2,$3等代替
```
>最后选择全部匹配即可
