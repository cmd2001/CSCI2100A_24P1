# CSCI2100A_24P1
Project Template for CUHK CSCI2100A Fall 2024

## Supported Languages

- C++
- Java
- Python**3**

**Note that python2 is deprecated and you should never use it in any new projects.**

## Quick Start Guide

### Step 1: Fork the repository on GitHub

### Step 2: Clone the repository

### Step 3: Install the required libraries

Assume you are using **debian-based linux distributions**, you can install the required libraries by running the following commands specified below.

For macOS and Windows users, you should look for VM or WSL to run debian-based linux distributions.

**We do not provide official support for macOS and Windows, but you can try to install the required libraries by yourself, then provide a PR to update this document and help those in need**

#### For C++

```bash
sudo apt install build-essential
sudo apt install libcurl4-openssl-dev nlohmann-json3-dev
```

#### For Java

```bash
sudo apt install openjdk-17-jdk
sudo apt install libgoogle-gson-java
```
#### For Python

```bash
sudo apt install python3
```

### Step 4: Obtain your API key

Signup for a free account at [financialmodelingprep](https://site.financialmodelingprep.com/login)

Visit [https://financialmodelingprep.com/api/v3/market-capitalization/AAPL](https://financialmodelingprep.com/api/v3/market-capitalization/AAPL), the browser should automatically fill in the API key for you, copy the API key and paste it into `entry.sh`.

### Step 5: Run the example eval script

The entry point for the project is `entry.sh`, and by default its for C++.

Commend out the C++ part and uncomment the Java or Python part if you want to run the Java or Python version.

Finally, run the following command to execute the script.

```bash
bash entry.sh
```

### Step6: Write your own code

You can start writing your own code in the corresponding language directory, change `entry.sh` to run your code.

