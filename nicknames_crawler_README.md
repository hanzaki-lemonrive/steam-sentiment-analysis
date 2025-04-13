# Steam Player_Nicknames Crawler

As the initial review information acquired through Steam API won't directly provide the usernames (personaname), this script is designed to fetch player nicknames (with acquired SteamID) through Steam API.

## Contents
1. [Functionality](#functionality)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Example](#example)
6. [Error Handling](#error-handling)

## Functionality
This script leverages ISteamUser (through GetPlayerSummaries) to retrieve player nicknames based on a list of Steam IDs. It then saves the retrieved nicknames along with their corresponding Steam IDs to a CSV file.

## Prerequisites
- Python 3.x
- `requests` library (install using `pip install requests`)
- A Steam API key (obtainable from the [Steam API Key Registration page](https://steamcommunity.com/dev/apikey))
- A list of Steam IDs

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the required `requests` library by running:
   ```bash
   pip install requests
   ```

## Usage
1. Replace the placeholder `api_key` in the script with your actual Steam API key.
2. Update the `steam_ids` list with the Steam IDs you want to fetch nicknames for. Please DO NOT exceed 100 IDs per request.
3. Run the script:
   ```bash
   python crawler_nicknames_e.g.1-100.py
   ```

## Example
The script will output the player nicknames to the console and save them to a CSV file specified in the `output_path` variable. For example, if the script is run with the provided `steam_ids` and `api_key`, it will generate a CSV file containing the Steam IDs and their corresponding nicknames.

## Error Handling
The script includes basic error handling for HTTP request failures. If an error occurs during the API request, an error message will be printed to the console, and an empty dictionary will be returned.
