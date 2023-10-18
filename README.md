# EVM Chain Native Token Auto Transfer Bot

## Overview

The EVM Chain Native Token Transfer Bot is a Python-based bot that automates the process of sending out native tokens (e.g., BNB, MATIC, ETH) from YOUR EVM-based wallet. The primary goal of this bot is to enhance the security of crypto owners wallet by automating the transfer of illicit funds in the event of a compromise. By automating this process, the wallet owner can quickly respond to security breaches and protect their assets. Personally, I'd suggest the receiving address to be an hardware wallet (it gives a sense of protection)

## Features

- Automated transfer of native tokens upon predefined conditions.
- Monitoring of wallet address for incoming transactions.
- Customizable configuration for various EVM chain networks.
- Notification and logging mechanisms for tracking transfers.

## Prerequisites

Before using the bot, ensure you have the following prerequisites installed:

- Python 3.12 or a compatible Python version.
- Required Python packages, which can be installed via `pip`. See the [Installation](#installation) section.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/nsisongltd/EVM-AutoTransfer-Bot.git

2. Change into the project directory:

   ```bash
   cd EVM-AutoTransfer-Bot

3. Install the required Python packages:

   ```bash
   pip3 install -r requirements.txt

// I would list the requirements detail in that file.  I don't want to forget

4. Install the required Python packages:

   ```bash
   pip3 install -r requirements.txt


# Usage

To run the bot, execute the main Python script:
    ```bash
    python3 bot.py

    Make sure to configure the bot settings and wallet address in the **config,json** file before running it.


# Configuration

The **config,json** file allows you to customize the bot behaviour, including wallet addresses to monitor, network settings, and notification preferences. Please check the **config.example.json** as a template for your own configuration.

# Contributing 

I'd appreciate contributions to this project. I made it open-source because I feel a bit rusty with my python skill. If you have ideas for imrpovements, bug fixes, or even new features, feel free to submit pull requests. I would review it.

