# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/28 15:50
# @File = beautifulsoupdemo.py


from bs4 import BeautifulSoup

html = """
<title>哈哈哈</title>
<p class ="title" name ="dream"><b>什么都是浮云</b></p>
		<div class="clear"></div>
            			<!-- BEGIN #main-nav -->
			<nav id="main-nav" class="grid-12 menu-nav">
                <div class="menu-sub-menu-container"><ul id="main-nav-menu" class="menu"><li id="menu-item-80741" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-80741"><a href="http://python.jobbole.com/">首页</a></li>
<li id="menu-item-80740" class="menu-item menu-item-type-post_type menu-item-object-page current_page_parent menu-item-80740"><a href="http://python.jobbole.com/all-posts/">所有文章</a></li>
<li id="menu-item-83414" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-83414"><a href="http://python.jobbole.com/category/news/">观点与动态</a></li>
<li id="menu-item-83410" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-83410"><a href="http://python.jobbole.com/category/basic/">基础知识</a></li>
<li id="menu-item-83411" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-83411"><a href="http://python.jobbole.com/category/guide/">系列教程</a></li>
<li id="menu-item-83412" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-83412"><a href="http://python.jobbole.com/category/project/">实践项目</a></li>
<li id="menu-item-83413" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-83413"><a href="http://python.jobbole.com/category/tools/">工具与框架</a></li>
<li id="menu-item-80742" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-80742"><a href="http://hao.jobbole.com/?catid=144">工具资源</a></li>
<li id="menu-item-85851" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-85851"><a href="http://group.jobbole.com/category/tech/python/">Python小组</a></li>
</ul></div>				<div class="clear"></div>
			</nav>
"""
soup = BeautifulSoup(html,"lxml")
print(soup.p["class"])

