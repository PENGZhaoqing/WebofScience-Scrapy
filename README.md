# WebofScience-Scrapy

爬取WebofScience网站中17年所有中科院发表的论文信息

## 安装

请自行安装Python和Scrapy

## 使用


1. 进入WebofScience网站，在高级搜索中填入AD=Chinese Acad Sci，选取年份2017-2017，然后点击查询，在下面会有一个查询结果
2. 进入查询结果，复制URL，然后替换WebofScience/science.py中的start_url
3. 在终端中运行：`scrapy crawl science `

若希望爬虫设置断点，以便下次继续爬取，请执行：`scrpy crawl science -s JOBDIR=WebofScience/backup/sciencespider`


### 数据文件

抓取的数据可以在根目录下的`papers.json`查看

## To do

将爬虫用Web API封装，提供爬虫的网页界面，降低使用门槛

