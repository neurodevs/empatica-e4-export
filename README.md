# empatica-e4-export
Export sessions data from the Empatica E4 platform with Selenium/Chrome

## Installation

### Google Chrome & ChromeDriver Installation

To use this script, you need to install Google Chrome and ChromeDriver, the latter of which must match your installed version of Google Chrome.

1. **Check Chrome Version**: Open Chrome and go to `chrome://settings/help` to find your version number.

2. **Download ChromeDriver**: Visit the [ChromeDriver downloads page](https://chromedriver.chromium.org/downloads) and download the version that matches your Chrome installation.

3. **Install ChromeDriver**:
   - **macOS**: 
     ```bash
     unzip chromedriver-mac-x64.zip
     cd chromedriver-mac-x64
     mv chromedriver /usr/local/bin/
     ```

4. **Verify Installation**: Run the following command to ensure it's installed correctly:
   ```bash
   chromedriver --version
   ```

### Environment Setup

To set up the required environment, you can use the provided environment.yml file. This file contains all necessary dependencies.

1. Clone the repository:

```bash
git clone https://github.com/neurodevs/empatica-e4-export.git
cd empatica-e4-export
```

2. Create a conda environment:

```bash
conda env create -f environment.yml
```

3. Activate the environment:

```bash
conda activate empatica-e4-export
```

## Usage

### Start Chrome in Debugging Mode

Start Chrome in debugging mode before running the script:

```bash
open -a "Google Chrome" --args --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev"
```

### Run the Script

Run the script from the command line with the required arguments:

```bash
python run_export.py 
    --email your_email@example.com 
    --password your_password 
    --download_dir ~/Downloads 
    --driver_path /usr/local/bin/chromedriver 
    --should_quit_at_end
```

### Command-Line Arguments

- --email: Your email for logging in (required)
- --password: Your password for logging in (required)
- --download_dir: Directory to save downloaded files (default: ~/Downloads)
- --driver_path: Path to ChromeDriver (default: /usr/local/bin/chromedriver)
- --should_quit_at_end: Optional flag to quit the browser after execution (default: False)

## Further Questions

If you have any questions or issues, feel free to reach out or open an issue!

