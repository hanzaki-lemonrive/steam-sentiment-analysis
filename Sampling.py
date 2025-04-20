import pandas as pd
from chardet import detect

# 文件路径配置
input_path = r"D:\kcl\sem2\data collection and analysis\steam_reviews_242760_final.csv"
output_path = r"D:\kcl\sem2\data collection and analysis\steam_reviews_242760_sample_600.csv"


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        rawdata = f.read(10000)  # 读取前10000字节检测编码
    return detect(rawdata)['encoding']


try:
    # 检测文件编码
    file_encoding = detect_encoding(input_path)
    print(f"检测到文件编码：{file_encoding}")

    # 读取CSV文件（使用检测到的编码）
    df = pd.read_csv(input_path, encoding=file_encoding)

    # 检查数据量
    if len(df) < 600:
        print(f"警告：文件只有 {len(df)} 条记录，将抽取全部数据")
        sample_size = len(df)
    else:
        sample_size = 600

    # 随机抽样
    sample = df.sample(n=sample_size, random_state=42)

    # 保存结果（统一保存为UTF-8编码）
    sample.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"成功生成抽样文件：{output_path}")
    print(f"抽样数量：{sample_size}条（原文件共{len(df)}条）")

except FileNotFoundError:
    print(f"错误：文件未找到，请检查路径 - {input_path}")
except Exception as e:
    print(f"发生错误：{str(e)}")
    print("常见解决方法：")
    print("1. 尝试手动指定编码：encoding='gbk' 或 encoding='latin1'")
    print("2. 检查文件是否被其他程序占用")
