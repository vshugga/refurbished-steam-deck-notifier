[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y41BZ8SM)

[![](https://dcbadge.limes.pink/api/server/5gpFTMkvJn)](https://discord.gg/5gpFTMkvJn)
# Steam Deck Availability Notifier

This script checks the availability of refurbished Steam Decks on Steam and sends notifications to a specified Discord webhook. It runs by querying Steam's API and comparing the current stock status with previously stored values.

## 🚀 Features
- Checks the availability of refurbished Steam Decks for a specified country.
- Sends notifications via a **Discord webhook** when stock availability changes.
- Supports different Steam Deck models (LCD & OLED versions).
- Prevents duplicate notifications by storing the last known stock status.

## 📋 Requirements
### Install Dependencies
Ensure you have **Python 3.x** installed. Then, install the required dependencies using:
```sh
pip install requests discord-webhook
```

## 🛠 Setup
1. **Edit the script** to set your preferred country.
   - The `country_code` variable defines which region to check for stock.
   - Find valid country codes [here](https://github.com/RudeySH/SteamCountries/blob/master/json/countries.json).
   ```python
   country_code = 'DE'  # Change this to your preferred country
   ```

2. **Set up your Discord webhook**
   - Replace `https://discord.com/api/webhooks/some_webhook` with your actual **Discord webhook URL**.
   ```python
   webhook = DiscordWebhook(url="https://discord.com/api/webhooks/YOUR_WEBHOOK", content="error")
   ```
   **⚠️ Never share your webhook publicly!**

3. **Run the script**
   - Execute the script in the terminal:
   ```sh
   python steam_deck_checker.py
   ```

## 🔧 How It Works
1. The script requests stock availability for various Steam Deck models from the Steam API.
2. It compares the latest availability status with the previously stored value in text files.
3. If availability changes, it sends a **Discord notification**.
4. The message pings specific Discord roles (modify this if needed).

## 🖥 Customization
- **Add More Steam Deck Models:**
  - Modify `superduperscraper()` calls at the end of the script to check for additional package IDs.
- **Change Notification Format:**
  - Modify the `webhook.content` message inside the script.

## ❗ Important Notes
- This script **does not continuously run**—use a cron job (Linux/macOS) or Task Scheduler (Windows) to automate execution.
  
   **Configuring a cron job (for Linux/macOS):**
   ```bash
   $ crontab -e
   ```
   ```bash
   */3 * * * *     <path to python(f.e. /usr/bin/python3)> /path/to/script.py >> path/to/logfile.log
   ```
   Save and exit the editor you shouldn't need to restart. Normally the crontab should start doing its job now!
   It will call the script every 3 minutes.
- You need **a Raspberry Pi or a server** if you want it running 24/7.

## 📝 License
This script is provided **as-is** with no guarantees. Use at your own risk!

## ❤️ Support
If you find this useful, consider buying me a coffee on [**Ko-fi**](https://ko-fi.com/Y8Y41BZ8SM)

