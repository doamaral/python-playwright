## System requirements
- Python 3.8 or higher.
- OS:
    - Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL) or
    - macOS 13 Ventura + or
    - Debian 12, Ubuntu 22.04, Ubuntu 24.04, on x86-64 and arm64 architecture or

## Environment Setup
- Clone this repo and `cd` the folder
- (optional) Setup virtualenv
    - `python3 -m pip install virtualenv`
    - Set venv: `python3 -m venv venv`
    - Activate: 
        - linux/macos: `source venv/bin/activate`
        - windows: `.\venv\Scripts\activate`
    - Deactivate: `deactivate`

## Project Setup
- `python3 -m pip install -r requirements.txt`
- Set up the Playwright WebKit: `playwright install`

## Project Structure
```
.
├── pages: Page object modelling of project's pages or components
└── tests: Test functions
└── utils: Utilitary functions to be used on the project
└── .gitignore: Definitions of non tracked files
└── conftest.py: Pytest fixtures
└── requirements.txt: Lybraries utilized on the project
└── README.md: File with project's instructions
```

## Running tests
### Running on HEADED mode:
`python3 -m pytest tests/<test suite to run> --headed`

### Running on HEADLESS mode:
`python3 -m pytest tests/<test suite to run> --headed`

### Adding Allure reports
add `--alluredir <folder containing report files> --clean-alluredir` to the test command

## TODO items
- Finish invoice detail test

