### **Steam Review Crawler User Guide / Steam评论爬虫使用说明**

---

### **1. 基本使用方法 / Basic Usage**

**中文**

1. 确保安装Python 3.6+
2. 安装依赖库：`pip install requests pandas`
3. 直接运行脚本即可爬取《火箭联盟》的英文评论
4. 结果会保存为`RLHotel_YYYYMMDD_HHMMSS.csv`文件

**English**

1. Ensure Python 3.6+ is installed
2. Install dependencies: `pip install requests pandas`
3. Run the script to crawl English reviews for Rocket League
4. Results will be saved as `RLHotel_YYYYMMDD_HHMMSS.csv`

---

### **2. 更换游戏 / Changing Games**

**中文**

修改代码第12行的`appid`：

python

复制

```
appid = "435120"  # 改为目标游戏的Steam ID
```

**如何查找游戏ID**：

- 访问Steam商店页面，URL中`app/`后的数字就是ID
- 示例：《Dota 2》的商店页为`store.steampowered.com/app/570`，ID就是570

**English**

Modify the `appid` in line 12:

python

复制

```
appid = "435120"  # Change to target game's Steam ID
```

**How to find Game ID**:

- Visit Steam store page, the number after `app/` in URL is the ID
- Example: Dota 2's page is `store.steampowered.com/app/570`, so ID is 570

---

### **3. 自定义筛选条件 / Custom Filters**

| **参数 Parameter** | **中文选项** | **English Options** | **修改位置 Line #** |
| --- | --- | --- | --- |
| `language` | 语言（如"schinese"） | Language (e.g. "english") | 14 |
| `day_range` | 时间范围（天） | Day range (max: 365) | 17 |
| `review_type` | "all"/"positive"/"negative" | 同上 | 15 |
| `num_per_page` | 每页评论数（max:100） | Reviews per page | 18 |

---

### **4. 注意事项 / Important Notes**

**中文**

- 请勿设置`time.sleep()`低于1秒，否则可能被封IP
- 大量爬取建议使用代理IP
- 默认只爬取90天内的评论（修改`day_range`可调整）
- 如需完整历史评论，需多次修改日期范围分段爬取

**English**

- Never set `time.sleep()` below 1s to avoid IP ban
- Use proxy IPs for large-scale crawling
- Default crawls last 90 days only (modify `day_range`)
- For full history, crawl in date segments

---

### **5. 输出文件格式 / Output Format**

| **字段 Field** | **中文说明** | **English Description** |
| --- | --- | --- |
| ReviewID | 评论唯一ID | Unique review ID |
| UserID | 用户Steam ID | User's Steam ID |
| content | 评论文本 | Review text content |
| time | 评论时间（YYYY-MM-DD HH:MM:SS） | Timestamp |
| vote | "upvote"(推荐)/"downvote"(不推荐) | Review type |
| playtime_hrs | 用户游戏时长（小时） | Playtime in hours |

---

### **6. 常见问题 / Troubleshooting**

**Q: 没有生成CSV文件 / No CSV generated**

- 检查是否出现错误（控制台红字）
- 可能网络问题导致没有获取到数据

**Q: 想爬取其他语言评论 / Other languages**

修改`language`参数，例如：

- 简体中文: `schinese`
- 法语: `french`

**Q: 如何续爬中断的任务 / Resume interrupted crawl**

保存并重用最后的`cursor`值即可继续