# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 17:36
# @File = redemo.py


# 正则表达式练习
import re


html = """
<li class="item_3">
<a href="http://v.baidu.com/tv/" target="_blank" title="电视剧">电视剧</a></li>
<li class=""><a href="http://v.baidu.com/movie/" target="_blank" title="电影">电影</a></li><li class="">
<a href="http://v.baidu.com/show/" target="_blank" title="综艺">综艺</a></li><li class="">
<a href="http://v.baidu.com/comic/" target="_blank" title="动漫">动漫</a></li><li class="item_3">
<a href="http://v.baidu.com/channel/shaoer" target="_blank" title="动画片">动画片</a></li>
<li class="">
<a href="http://v.baidu.com/channel/amuse" target="_blank" title="搞笑">搞笑</a></li>
<li class=" no-margin">
<a href="http://v.baidu.com/channel/star" target="_blank" title="娱乐">娱乐</a></li>
<li class="">
<a href="http://v.baidu.com/live/" target="_blank" title="卫视">卫视</a></li>
<li class="">
<a href="http://v.baidu.com/channel/xiaopin" target="_blank" title="小品">小品</a></li>
<li class="">
<a href="http://v.baidu.com/sportindex/" target="_blank" title="体育">体育</a></li>
<li class="item_3">
<a href="http://v.baidu.com/channel/rr" target="_blank" title="看欧美">看欧美</a>
</li><li class="beauty-area-limit">
<a href="http://v.baidu.com/channel/beauty" target="_blank" title="美女">美女</a></li>
<li class="">
<a href="http://v.baidu.com/channel/history" target="_blank" title="揭秘">揭秘</a></li>
<li class=" no-margin"><a href="http://v.baidu.com/channel/music" target="_blank" title="音乐">音乐</a>
</li></ul></div>
"""

result = re.findall('<a.*?href="(.*?)".*?title="(.*?)">',html,re.S)
print(type(result))
for r in result:
    #print(r)
    print("分类:",r[1],"地址:",r[0])














