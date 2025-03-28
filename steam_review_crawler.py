import requests
import time
import pandas as pd
from urllib.parse import quote

appid = "435120"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

params = {
    'json': 1,
    'language': 'english',
    'day_range': '9223372036854775807',  # 最大时间范围
    'review_type': 'all',
    'purchase_type': 'all',
    'filter': 'recent',
    'num_per_page': 100
}


def get_reviews(cursor="*"):
    current_params = params.copy()
    current_params['cursor'] = cursor

    try:
        time.sleep(1.5)  # 适当增加延迟
        response = requests.get(
            f"https://store.steampowered.com/appreviews/{appid}",
            headers=headers,
            params=current_params,
            timeout=20
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"请求失败: {str(e)}")
        return None


def main():
    reviews_data = {}
    cursor = "*"
    request_count = 0
    duplicate_count = 0
    max_duplicates = 3  # 最大允许重复次数

    while duplicate_count < max_duplicates:
        request_count += 1
        print(f"\nRequest #{request_count} | 总评论: {len(reviews_data)} | 当前游标: {cursor}")

        data = get_reviews(cursor)
        if not data:
            break

        if data.get("success") != 1:
            print("API错误:", data.get("message", "Unknown error"))
            print("完整响应:", json.dumps(data, indent=2))
            break

        reviews = data.get("reviews", [])
        print(f"获取到 {len(reviews)} 条评论")
        print(f"新游标: {data.get('cursor')}")

        # 检查是否获取到新评论
        new_reviews = 0
        for review in reviews:
            rid = review["recommendationid"]
            if rid not in reviews_data:
                reviews_data[rid] = {
                    "ReviewID": rid,
                    "UserID": review["author"]["steamid"],
                    "content": review["review"],
                    "time": review["timestamp_created"],
                    "vote": "upvote" if review["voted_up"] else "downvote"
                }
                new_reviews += 1

        print(f"新增评论: {new_reviews} 条")

        # 处理游标和重复检测
        new_cursor = data.get("cursor")
        if not new_cursor or new_cursor == cursor:
            duplicate_count += 1
            print(f"游标未更新 (重复 {duplicate_count}/{max_duplicates})")
        else:
            duplicate_count = 0  # 重置计数器
            cursor = new_cursor

        # 没有新评论且游标未更新时停止
        if new_reviews == 0 and duplicate_count >= max_duplicates:
            print("连续多次未获取新评论，停止爬取")
            break

        # 定期保存
        if len(reviews_data) % 200 == 0:
            pd.DataFrame(reviews_data.values()).to_csv(f"checkpoint_{len(reviews_data)}.csv", index=False)

    # 最终保存
    if reviews_data:
        final_file = f"steam_reviews_{appid}_final.csv"
        pd.DataFrame(reviews_data.values()).to_csv(final_file, index=False)
        print(f"\n完成! 共获取 {len(reviews_data)} 条评论")
        print(f"保存到 {final_file}")
    else:
        print("未获取到任何评论数据")


if __name__ == "__main__":
    import json

    main()
