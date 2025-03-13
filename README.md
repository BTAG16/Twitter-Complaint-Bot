# Twitter Complaint Bot

This Python project uses Selenium to check internet speeds using Speedtest.net and automatically tweets at your internet service provider if the speed is below the promised threshold.

## Features
- Check your current internet speed (download/upload) using Speedtest.net.
- Automatically log in to Twitter and tweet a complaint if the internet speed is lower than the promised speed.
- Use environment variables to securely store sensitive information like Twitter credentials.

## Prerequisites

- Python 3.x
- Selenium
- Chrome WebDriver
- `python-dotenv` for handling environment variables
- A Twitter account

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Twitter-Complaint-Bot.git
   cd Twitter-Complaint-Bot
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project to store your sensitive data:
   ```plaintext
   EMAIL=your_twitter_email
   USERNAME=your_twitter_username
   PASSWORD=your_twitter_password
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. The script will:
   - Go to Speedtest.net, check your internet speed.
   - If the download or upload speed is below the promised speed (defined by the constants `PROMISED_DOWN` and `PROMISED_UP`), it will log into Twitter.
   - It will post a complaint to your internet provider mentioning the speed discrepancy.

## Configuration

- `PROMISED_DOWN`: The expected download speed in Mbps (e.g., 85).
- `PROMISED_UP`: The expected upload speed in Mbps (e.g., 90).
- `TWITTER_EMAIL`: Your Twitter account email.
- `TWITTER_USERNAME`: Your Twitter account username.
- `TWITTER_PASSWORD`: Your Twitter account password.

You can adjust the speed thresholds or Twitter login credentials by modifying the values in the `.env` file.

## Notes

- Ensure you have Google Chrome installed on your machine.
- The WebDriver (`chromedriver`) should be installed and available in your PATH. You can download it from [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).
- The script uses a headless browser configuration with Chrome, but you can adjust the options based on your environment.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Selenium documentation: https://www.selenium.dev/documentation/en/
- Speedtest API: https://www.speedtest.net/
