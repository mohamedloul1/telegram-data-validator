# Telegram Mini App Validation Project

This is a small project that provides a quick overview of how validation works in Telegram using Python. The application consists of a backend and a frontend that work together to verify the integrity of Telegram Mini App data.

## Overview

- **Backend:** A Python Flask application that validates the received data.
- **Frontend:** A simple HTML/JavaScript page that demonstrates interaction with the Telegram WebApp API and triggers the validation process.
- **Validation:** The backend checks the integrity of the data using HMAC, comparing the computed hash with the received hash.
- **Tunnel Hosting:** Both the backend and frontend can be hosted using Cloudflared tunnels, which are free. Cloudflared allows you to run multiple tunnels simultaneously.

## Requirements

- Python 3.x
- pip (Python package manager)
- A Telegram Bot Token (available via [BotFather](https://t.me/BotFather))
- Cloudflared (for setting up tunnels)

## Installation

1. **Clone the Repository:**

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Create a `.env` File:**

    In the root of the project, create a `.env` file and add the following line (replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual token):

    ```env
    BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    ```

3. **Install the Required Python Packages:**

    ```bash
    pip install flask flask-cors python-dotenv
    ```

4. **Download and Install Cloudflared:**

    Follow the instructions on the [Cloudflare Tunnel documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation) to install Cloudflared on your system.

## Project Structure

- `app.py` - The backend Flask application.
- `index.html` - The frontend HTML page.
- `script.js` - The JavaScript code for the frontend.
- `.env` - Contains your Telegram Bot Token.

## Usage

### Starting the Backend

Run the Flask application with:

```bash
python app.py
