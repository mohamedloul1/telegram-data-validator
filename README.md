# Telegram Mini App Validation Project

![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-green?style=for-the-badge&logo=flask)

## 📌 Overview
This project demonstrates how validation works in a Telegram Mini App using Python. It consists of a **backend** and a **frontend** that work together to verify the integrity of Telegram Mini App data.

### 🔹 Components
- **Backend:** A Python Flask application that validates the received data.
- **Frontend:** A simple HTML/JavaScript page that interacts with the Telegram WebApp API and triggers the validation process.
- **Validation:** The backend verifies the integrity of the data using HMAC, comparing the computed hash with the received hash.
- **Tunnel Hosting:** The backend and frontend can be hosted using Cloudflared tunnels, allowing you to run multiple tunnels for free.

## 🚀 Requirements
- Python 3.x
- pip (Python package manager)
- A Telegram Bot Token (available via [BotFather](https://t.me/BotFather))
- Cloudflared (for setting up tunnels)

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2️⃣ Create a `.env` File
Create a `.env` file in the root of the project and add your Telegram Bot Token:
```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

### 3️⃣ Install Dependencies
```bash
pip install flask flask-cors python-dotenv
```

### 4️⃣ Install Cloudflared
Follow the instructions on the [Cloudflare Tunnel documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation) to install Cloudflared on your system.

## 📂 Project Structure
```
📁 telegram-mini-app-validation
│── app.py          # Backend Flask application
│── index.html      # Frontend HTML page
│── script.js       # JavaScript code for frontend interaction
│── .env            # Contains your Telegram Bot Token
│── requirements.txt # Dependencies (optional)
```

## ▶️ Usage

### Starting the Backend
Run the Flask application:
```bash
python app.py
```

### Hosting with Cloudflared
Run the Cloudflared tunnel to expose your application:
```bash
cloudflared tunnel --url http://localhost:5000
```
This will provide a public URL for your Telegram Mini App.

## 📜 License
This project is open-source and available under the MIT License.

---
💡 *Contributions are welcome! Feel free to fork this repository and submit a pull request.*

