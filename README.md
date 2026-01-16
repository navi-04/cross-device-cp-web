# Cross-Device Clipboard Web App

A simple web application that allows you to share text across devices on the same local network.

## Features

- Add text entries via a text input box
- Each entry has Copy and Delete buttons
- Accessible from any device on your local network
- Data persists between sessions
- Beautiful, responsive UI

## Setup

1. Install Python (3.7 or higher)

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Access the application:
   - On the same computer: http://localhost:5000
   - From other devices on the network: http://YOUR_LOCAL_IP:5000
   
   To find your local IP:
   - Windows: Run `ipconfig` and look for IPv4 Address
   - Mac/Linux: Run `ifconfig` or `ip addr`

## Usage

1. Enter text in the input box at the top
2. Click "Add" or press Enter
3. Your text will appear below with Copy and Delete buttons
4. Use Copy to copy the text to your clipboard
5. Use Delete to remove the entry
6. Access the same page from any device on your network to share the clipboard!

## Notes

- Make sure your firewall allows connections on port 5000
- All devices must be on the same local network
- Data is stored in `clipboard_data.json` file
