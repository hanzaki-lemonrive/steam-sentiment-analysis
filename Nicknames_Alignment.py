import pandas as pd

# 读取两个文件
file1 = r"E:\Carla\King's\Data Collection\data_Steam\userid_600.xlsx"  # 包含原始 UserID 的文件
file2 = r"E:\Carla\King's\Data Collection\data_Steam\player_nicknames.xlsx"      # 包含乱序 Nickname 的文件
output_file = r"E:\Carla\King's\Data Collection\data_Steam\sorted_nicknames.xlsx"

# 使用 pandas 读取 Excel 文件
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

df1 = pd.read_excel(file1, engine='openpyxl')
df2 = pd.read_excel(file2, engine='openpyxl')

df1['Steam ID'] = df1['Steam ID'].astype(str).str.replace('.', '').str.replace('e+', '').str.strip()
df2['Steam ID'] = df2['Steam ID'].astype(str).str.replace('.', '').str.replace('e+', '').str.strip()
df2['Nickname'] = df2['Nickname'].astype(str).str.strip()

duplicates = df2[df2.duplicated(subset=["Steam ID"], keep=False)]
if not duplicates.empty:
    print("存在重复的 Steam ID：")
    print(duplicates)

# 创建一个字典，以 Steam ID 为键，Nickname 为值
nickname_dict = dict(zip(df2["Steam ID"], df2["Nickname"]))

# 按照 File 1 中的 UserID 顺序提取昵称
sorted_nicknames = [nickname_dict.get(Steam_id, "Unknown") for Steam_id in df1["Steam ID"]]

# 将结果保存到新的 DataFrame 中
result_df = pd.DataFrame({
    "Steam_ID": df1["Steam ID"],
    "Nickname": sorted_nicknames
})

result_df.to_excel(output_file, index=False, engine='openpyxl')

print("昵称已按照原始 SteamID 的顺序重新排列并保存到 sorted_nicknames.xlsx 文件中。")