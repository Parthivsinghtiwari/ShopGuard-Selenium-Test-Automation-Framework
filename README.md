# ShopGuard — Selenium Automation Framework

ShopGuard is a beginner-friendly Python + Selenium + pytest project for practising UI automation against the public SauceDemo training application.

## Current scope

- Valid login opens the Products page
- Invalid password displays an error
- Locked-out user is rejected
- Product listings are displayed
- Adding the Sauce Labs Backpack updates the cart badge

These are implemented test cases, not a claim that they have already passed in every environment. Run the suite and report the actual results.

## Tech stack

- Python
- Selenium WebDriver
- pytest
- Page Object Model (POM)
- Selenium Manager for browser driver management

## Prerequisites

- Windows 10/11
- Python 3.10 or newer
- Google Chrome
- Visual Studio Code (recommended)

## Setup on Windows

Open the project folder in VS Code. In Terminal, run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks virtual-environment activation, you can use Command Prompt and run:

```bat
.venv\Scripts\activate.bat
```

Then run the tests:

```powershell
python -m pytest
```

Generate an HTML report:

```powershell
python -m pytest --html=reports/report.html --self-contained-html
```

Create the `reports` folder first if it does not exist:

```powershell
New-Item -ItemType Directory -Force reports
```

## Project structure

```text
ShopGuard/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   └── test_inventory.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test credentials

SauceDemo publicly documents `standard_user` / `secret_sauce` for its demo environment. The suite also checks the documented `locked_out_user` scenario. Use only the public demo; do not use real accounts.

## Design notes

- Page classes hold locators and browser actions.
- Tests contain assertions about expected behaviour.
- Each test gets a fresh browser session through a pytest fixture.
- Explicit waits are used for elements that need to become visible or clickable.
- Selenium Manager can resolve a compatible driver automatically in supported setups; Chrome and network access may still be required.

## Known limitations / next steps

- Checkout and remove-from-cart flows are not implemented yet.
- API testing and GitHub Actions are not configured yet.
- Browser execution has not been certified in your local environment. Run the tests and update this README with the actual outcome.
- Add screenshots, logging, and CI only after the basic suite runs reliably.

## Resume description (use after running and verifying)

**ShopGuard — Selenium Test Automation Framework**
- Developed a Python-based UI automation suite using Selenium WebDriver and pytest for a public demo e-commerce application.
- Applied the Page Object Model to separate page interactions from test assertions.
- Automated login validation, product listing checks, and cart badge verification using explicit waits.

Only list the features you have actually run and can explain in an interview.
