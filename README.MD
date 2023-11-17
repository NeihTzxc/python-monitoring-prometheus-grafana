# Prometheus Metrics Example

This project demonstrates how to use Prometheus Python client library to create and expose metrics for monitoring purposes.

## Getting Started

These instructions will help you set up and run the example script that generates random metrics and exposes them for Prometheus.

### Prerequisites

- Python 3.x
- Install required packages using:

    ```bash
    pip install -r requirements.txt
    ```

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/prometheus-metrics-example.git
    cd prometheus-metrics-example
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python script.py
    ```

   This will start an HTTP server on port 8000, allowing Prometheus to scrape metrics.

4. Access Prometheus UI:

    Open your web browser and go to [http://localhost:8000](http://localhost:8000) to access the Prometheus UI and view the metrics.

## Understanding the Code

The `script.py` file contains a simple Python script that generates random metrics (request processing time and update count) and exposes them for Prometheus.

### Metrics

- `request_processing_seconds`: Measures the time spent processing requests.
- `update_count`: Counts the number of updates.

### Prometheus Integration

- The Prometheus metrics are exposed on the `/metrics` endpoint.
- Prometheus is configured to scrape metrics from `http://localhost:8000` in the example.

### Dependencies

- [Prometheus Python Client](https://github.com/prometheus/client_python): Python client for Prometheus monitoring system.

## Database Backup Project

This section describes an extension to the project that automates the backup process for a PostgreSQL database and sends notifications to multiple messaging platforms (Telegram, Slack, Discord) upon successful completion.

### Features

- Automated PostgreSQL database backup.
- Notifications to multiple platforms (Telegram, Slack, Discord) on backup success.

### Getting Started

Follow these instructions to set up and run the database backup script with notifications.

#### Prerequisites

- Python 3.x
- Install required packages using:

    ```bash
    pip install -r requirements.txt
    ```

#### Configuration

1. Open the `config.py` file and update the configuration parameters:

    ```python
    # PostgreSQL Database Configuration
    DB_HOST = "your_db_host"
    DB_PORT = "your_db_port"
    DB_NAME = "your_db_name"
    DB_USER = "your_db_user"
    DB_PASSWORD = "your_db_password"

    # Telegram Configuration
    TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
    TELEGRAM_CHAT_ID = "your_telegram_chat_id"

    # Slack Configuration
    SLACK_TOKEN = "your_slack_token"
    SLACK_CHANNEL = "#your_slack_channel"

    # Discord Configuration
    DISCORD_WEBHOOK_URL = "your_discord_webhook_url"
    ```

2. Save the `config.py` file.

#### Running the Backup

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/database-backup-project.git
    cd database-backup-project
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the backup script:

    ```bash
    python backup_script.py
    ```

   This will perform a database backup and send notifications on success.

### Notifications

Notifications are sent to the configured channels/platforms upon successful completion of the database backup.

#### Supported Platforms

1. **Telegram:**
   - A notification will be sent to the specified Telegram chat.

2. **Slack:**
   - A notification will be posted to the specified Slack channel.

3. **Discord:**
   - A notification will be sent to the configured Discord webhook.

### Contributing

Feel free to contribute to this project. Open issues for suggestions or bug reports.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
