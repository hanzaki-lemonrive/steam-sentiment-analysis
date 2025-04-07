import requests
import csv
import os

def get_player_nicknames(steam_ids, api_key):
    """
    通过 Steam API 批量获取玩家昵称
    :param steam_ids: 玩家的 Steam ID 列表
    :param api_key: Steam API 密钥
    :return: 包含玩家昵称的字典
    """
    # 将 Steam ID 列表转换为逗号分隔的字符串
    steam_ids_str = ",".join(steam_ids)
    
    # 构造 API 请求 URL
    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={steam_ids_str}"

    try:
        # 发送 HTTP 请求
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()  # 解析 JSON 数据
        
        # 提取玩家昵称
        player_nicknames = {}
        for player in data['response']['players']:
            steam_id = player['steamid']
            nickname = player.get('personaname', 'Unknown')
            player_nicknames[steam_id] = nickname
        
        return player_nicknames
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {}

def save_to_csv(player_nicknames, filename="player_nicknames.csv"):
    """
    将玩家昵称数据保存到 CSV 文件
    :param player_nicknames: 包含玩家昵称的字典
    :param filename: 保存的文件名，默认为 player_nicknames.csv
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Steam ID", "Nickname"])  # 写入表头
        for steam_id, nickname in player_nicknames.items():
            writer.writerow([steam_id, nickname])  # 写入每行数据

if __name__ == "__main__":
    # 替换为你的 Steam API 密钥
    api_key = "96FB04E5028FF5551F93B0295385BDC0"
    
    # 替换为你的玩家 Steam ID 列表
    steam_ids = [
        "76561198974937503",
        "76561198851352005",
        "76561197980828688",
        "76561199073760453",
        "76561198312975380",
        "76561198005696798",
        "76561199136610767",
        "76561198405059532",
        "76561199027167607",
        "76561199056894256",
        "76561198088700442",
        "76561199122109393",
        "76561198892904946",
        "76561198089332801",
        "76561198052532259",
        "76561198333376916",
        "76561198175287266",
        "76561199328274501",
        "76561198062035833",
        "76561198153956655",
        "76561198850179563",
        "76561198057452485",
        "76561199251562099",
        "76561198979288261",
        "76561199345237039",
        "76561199560685825",
        "76561199121502671",
        "76561198319480160",
        "76561199070582135",
        "76561198004435259",
        "76561197981744495",
        "76561199155332479",
        "76561198106851597",
        "76561197979481459",
        "76561198090599096",
        "76561199093704932",
        "76561198032975226",
        "76561198170503355",
        "76561198034333276",
        "76561198152106534",
        "76561198008559233",
        "76561198407997106",
        "76561198976347837",
        "76561198068464575",
        "76561199161430518",
        "76561199489085299",
        "76561199547311719",
        "76561198360666921",
        "76561198058016073",
        "76561198857663232",
        "76561199012567485",
        "76561198801888389",
        "76561197995001220",
        "76561198141024725",
        "76561199122234798",
        "76561199157375162",
        "76561199126090629",
        "76561199166279764",
        "76561199064738070",
        "76561198240011768",
        "76561197993515393",
        "76561198415238614",
        "76561198033686448",
        "76561198350960151",
        "76561198018860202",
        "76561198063200438",
        "76561198136033327",
        "76561199059444112",
        "76561198161420125",
        "76561198432917912",
        "76561198241566932",
        "76561198377548427",
        "76561198165480804",
        "76561198308569943",
        "76561199115306235",
        "76561198272164236",
        "76561198383803231",
        "76561198968643925",
        "76561198113699776",
        "76561198427046314",
        "76561198151980696",
        "76561198273736530",
        "76561198383328985",
        "76561198958200294",
        "76561199227835173",
        "76561198320703784",
        "76561198004468758",
        "76561199247783567",
        "76561199017632064",
        "76561198818481505",
        "76561198036124867",
        "76561199051009330",
        "76561198212487512",
        "76561198804259213",
        "76561198006063283",
        "76561198202353447",
        "76561198296271062",
        "76561199134679701",
        "76561198267720906",
    ]
    
    # 获取玩家昵称
    nicknames = get_player_nicknames(steam_ids, api_key)
    
    # 打印结果
    for steam_id, nickname in nicknames.items():
        print(f"Steam ID: {steam_id}, Nickname: {nickname}")

    output_path = r"E:\Carla\King's\Data Collection\data_Steam\player_nicknames.csv"
    save_to_csv(nicknames, output_path)