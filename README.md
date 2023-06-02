# PwnGrab

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A powerful Python script to extract websites from different sources, including Zone-Xsec and Zone-H. It automates the process of gathering website URLs and saves them to files for further analysis or use.

## Features

- Extract websites from Zone-Xsec
- Extract websites from Zone-H
- Save the results to separate files

## Prerequisites

- Python 3.7 or higher
- `requests` library
- `colorama` library
- `bs4` (BeautifulSoup) library

## Installation

1. Clone the repository:

```
   git clone https://github.com/Sic4rio/PwnGrab
```
Change into the project directory:

```
cd PwnGrab
```
Install the required dependencies:

```
pip install -r requirements.txt
```
Run the script:

```
python pwn-grab.py
```
Follow the on-screen instructions to choose the desired option:

Option 1: Extract websites from Zone-Xsec
Option 2: Extract websites from Zone-H
Provide the required input information, such as page numbers, PHPSESSID, ZHE cookie, etc., as prompted.

The script will extract the websites and save the results to separate files (zonexecweb.txt for Zone-Xsec and zonehWeb.txt for Zone-H).

# Contributing
Contributions are welcome! If you find any issues or want to enhance the script, feel free to open a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.


Feel free to customize the content, formatting, and add any additional sections you think would be relevant.
