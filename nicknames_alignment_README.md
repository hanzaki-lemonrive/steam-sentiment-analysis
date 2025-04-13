# Steam Nicknames Alignment Script

Personanames returned from won't keep the original order of the provided SteamIDs. Therefore, this script is designed to re-arrange the sequence of the nicknames to align with IDs listed in the sample.

# Contents
1. [Functionality](#functionality)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Example](#example)
6. [Error Handling](#error-handling)
8. [License](#license)

## Functionality
The script reads two input files (one containing the original Steam IDs and another has the disordered nicknames and their corresponding userIDs), then aligns the nicknames along with their IDs in accordance to the sequence in the other file, and saves the aligned version to a new Excel (.xlsx) file.

## Prerequisites
- Python 3.x
- `pandas` library (install using `pip install pandas`)
- `openpyxl` library (install using `pip install openpyxl`)
- Two Excel files:
  - One containing the original Steam IDs (`userid_600.xlsx`).
  - Another containing the nicknames (`player_nicknames.xlsx`).

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries by running:
   ```bash
   pip install pandas openpyxl
   ```

## Usage
1. Update the file paths in the script to point to your input files (`file1` and `file2`) and specify the desired output file path (`output_file`).
2. Run the script:
   ```bash
   python Nicknames_Alignment.py
   ```

## Example
Assume you have the following input files:

### `userid_600.xlsx` (Original Steam IDs)
| Steam ID       |
|----------------|
| 76561198974937503 |
| 76561198851352005 |
| 76561197980828688 |

### `player_nicknames.xlsx` (Nicknames in random order)
| Steam ID       | Nickname |
|----------------|----------|
| 76561197980828688 | PlayerC  |
| 76561198974937503 | PlayerA  |
| 76561198851352005 | PlayerB  |

After running the script, the output file `sorted_nicknames.xlsx` will contain:

| Steam_ID       | Nickname |
|----------------|----------|
| 76561198974937503 | PlayerA  |
| 76561198851352005 | PlayerB  |
| 76561197980828688 | PlayerC  |

## Error Handling
The script includes checks for duplicate Steam IDs in the nickname file. If duplicates are found, they will be printed to the console. Additionally, the script handles cases where a Steam ID in the original file does not have a corresponding nickname by assigning "Unknown".

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
