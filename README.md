# Cloudflare bypass
<img width="698" alt="image" src="https://github.com/addavriance/cloudflare_bypass/assets/61160742/1275130a-78e4-4b35-8d08-e23624649565">

A simple Python script that bypasses the Cloudflare "Just a moment..." captcha.

## Acknowledgements
- [SeleniumBase](https://seleniumbase.io)
- [ZenRows](https://zenrows.com)

## Overview
The `cloudflare_bypass` script utilizes the SeleniumBase and ZenRows libraries to bypass the Cloudflare captcha on websites. It automates the process of loading the webpage, handling the captcha, and retrieving the page content.

## Features
- Supports macOS and Linux operating systems for free.
- Windows users require a ZenRows account and token to use the script. They are limited to 200 free requests.

## Prerequisites
Before using the script, make sure you have the following installed:

- Python 3.x
- SeleniumBase library
- ZenRows library

## Usage
1. Clone this repository to your local machine.
2. Install the required libraries and dependencies: `pip install -r requirements.txt`.
3. Update the `url` and `zenrows_token` variables in the script with your desired values.
4. Run the script: `python cloudflare_bypass.py`.
5. The script will initiate the bypass process and display the retrieved HTML content in the console.

Please note that for Windows users, you need to provide your ZenRows token to make requests. 

## Disclaimer
This script is intended for educational and research purposes only. Use it responsibly and respect the website's terms of service and captcha protection.
