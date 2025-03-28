# Steam Review Crawler / Steam评论爬虫
## 中文说明
### 项目概述
这是一个用于从Steam平台抓取游戏评论的Python爬虫工具，可将数据保存为CSV格式。

### 功能特点
1. 支持分页获取全部评论

2. 自动去重处理

3. 定期保存检查点

4.完善的错误处理机制

5. 可自定义请求参数

### 使用说明
环境要求

Python 3.6+

安装依赖库：
```
pip install requests pandas
```
配置参数

修改appid为目标游戏ID

调整params中的参数：

day_range: 时间范围

language: 评论语言

num_per_page: 每页数量

**运行程序**
```
python steam_review_crawler.py
```

**输出文件**

检查点文件: checkpoint_xxx.csv

**最终结果**: steam_reviews_[appid]_final.csv

### 注意事项

请遵守Steam的robots.txt规则

合理设置请求间隔(默认1.5秒)

商业用途需获得Valve授权

## English Description

### Project Overview
A Python crawler tool for scraping game reviews from Steam platform, saving data in CSV format.

### Key Features
1. Pagination support for complete review collection

2. Automatic duplicate removal

3. Periodic checkpoint saving

4. Robust error handling

5. Customizable request parameters

### Usage Instructions
**Requirements**

Python 3.6+

**Install dependencies**:

```
pip install requests pandas
```

**Configuration**

Modify appid to target game ID

Adjust parameters in params:

day_range: Time range filter

language: Review language

num_per_page: Items per page

**Execution**

```
python steam_review_crawler.py
```

**Output Files**

Checkpoint files: checkpoint_xxx.csv

**Final results**: steam_reviews_[appid]_final.csv

### Important Notes

Comply with Steam's robots.txt rules

Maintain reasonable request intervals (default 1.5s)

Commercial use requires Valve's authorization
