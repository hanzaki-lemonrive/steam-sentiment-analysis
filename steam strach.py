import requests
import time
import pandas as pd
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='steam_reviews.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Request parameters
appid = "435120"  # Rocket League's Steam app ID
cursor = "*"  # Initial cursor for pagination
language = "english"  # Filter reviews by language
review_type = "all"  # Can be "all", "positive", or "negative"
purchase_type = "steam"  # Purchase type filter
filter_type = "all"  # Review filter type
day_range = "90"  # Time range in days
num_per_page = 100  # Increased to 100 reviews per page to reduce requests
max_retries = 3  # Maximum retry attempts for failed requests
retry_delay = 5  # Delay between retries in seconds

# Request headers to simulate browser access
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

reviews_data = []  # List to store collected reviews
request_count = 0  # Counter for total requests made

while True:
    request_count += 1
    # Construct API URL with current parameters
    url = f"https://store.steampowered.com/appreviews/{appid}?json=1&cursor={requests.utils.quote(cursor)}&language={language}&day_range={day_range}&review_type={review_type}&purchase_type={purchase_type}&filter={filter_type}&num_per_page={num_per_page}"

    # Request with retry mechanism
    response = None
    for attempt in range(max_retries):
        try:
            start_time = time.time()
            response = requests.get(url, headers=headers, timeout=10)
            elapsed_time = time.time() - start_time
            logging.info(
                f"Request {request_count}: Took {elapsed_time:.2f} seconds. Status Code: {response.status_code}")
            print(f"Request {request_count}: Took {elapsed_time:.2f} seconds. Status Code:", response.status_code)

            if response.status_code == 200:
                break
            elif response.status_code == 429:
                # Handle rate limiting (too many requests)
                wait_time = 30  # Steam may return 429 for rate limiting
                print(f"Rate limit reached, waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue

        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed (attempt {attempt + 1}/{max_retries}): {e}")
            print(f"Request failed (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)

    # Final check if request failed after all retries
    if not response or response.status_code != 200:
        logging.error("Request failed after retries, stopping crawler")
        print("Request failed after retries, stopping crawler")
        break

    # Parse JSON response
    try:
        data = response.json()
        logging.debug(f"Response data: {json.dumps(data, indent=4)}")
    except Exception as e:
        logging.error(f"JSON parsing failed: {e}\nRaw response: {response.text}")
        print("JSON parsing failed:", e)
        print("Raw response:", response.text)
        break

    # Check if request was successful
    if data.get("success") == 1:
        logging.info("Successfully retrieved review data!")
        print("Successfully retrieved review data!")

        if 'reviews' in data and data['reviews']:
            reviews = data["reviews"]
            logging.info(f"Received {len(reviews)} reviews")
            print(f"Received {len(reviews)} reviews.")

            # Process each review
            for review in reviews:
                reviews_data.append({
                    "ReviewID": review["recommendationid"],
                    "UserID": review["author"]["steamid"],
                    "content": review["review"],
                    "time": datetime.fromtimestamp(review["timestamp_created"]).strftime('%Y-%m-%d %H:%M:%S'),
                    "vote": "upvote" if review["voted_up"] else "downvote",
                    "playtime_hrs": review.get("author", {}).get("playtime_forever", 0) / 60  # Convert minutes to hours
                })

            # Update cursor for pagination
            if 'cursor' in data and data['cursor']:
                cursor = data['cursor']
                logging.info(f"Updated cursor: {cursor}")
                print("Updated cursor:", cursor)
            else:
                # No more pages available
                logging.info("No more cursor available, stopping crawler")
                print("No more cursor, stopping.")
                break
        else:
            logging.info("No review data found")
            print("No review data found")
            break
    else:
        logging.error("Failed to get reviews")
        print("Failed to get reviews")
        break

    time.sleep(1.5)  # Delay between requests to avoid being blocked

# Save collected data to CSV
if reviews_data:
    df = pd.DataFrame(reviews_data)
    # Add timestamp to filename
    save_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"RLHotel_{save_time}.csv"
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    logging.info(f"Review data saved to {filename}")
    print(f"Review data saved to {filename}")
else:
    logging.warning("No review data collected")
    print("No review data collected")