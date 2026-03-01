# Spammer Selfbot

> ⚠️ Heads-up: selfbots violate Discord’s Terms of Service. Run this project only in controlled environments and at your own risk.

## Overview

This project uses `discord.py-self` to run a private selfbot that do a bunch of stuff. The entry point is `main.py`. Group features by Cogs in `cogs/`. Integrate other services in `libs/`.

## Requirements

- Python 3.8 – 3.12 (discord.py-self does not yet support 3.13+)
- `pip` for dependency management
- A Discord account with a valid user token (again, selfbots breach ToS)
- Git for collaboration

## Quick Start

```bash
git clone https://github.com/<username>/spammer-selfbot.git
cd spammer-selfbot
python -m venv .venv # the default Python version must be 3.8 - 3.12
# or use Python Install Manager
py -3.12 -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate
pip install -r requirements.txt # Install dependencies
cp .env.example .env # Create .env from example
```

## Configuration
Create .env in the project root (never commit real tokens):
```env
DISCORD_TOKEN=your_token_here
ADMIN_ID=your_admin_id_here
...
```

- DISCORD_TOKEN is your account token.
- ADMIN_ID is the numeric user ID that should receive the startup DM. Enable Discord “Developer Mode” to copy IDs.
- ...

## Running the Bot

```bash
python main.py
```

## Contributing
- Fork the repository and create a topic branch (git checkout -b feature/short-name).
- Update documentation/tests if you alter behavior.
- Update 'requirement.txt' if you add new dependencies.
- Update '.env.example' if you add new environment variables.

Happy hacking, and keep secrets safe!
