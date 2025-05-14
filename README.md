# Trade Novation Tool

A web application for novating executed trades, built with Python Flask and Bootstrap 4.1.3.

## Features

- Trade novation form with dynamic entry addition
- Input validation for trader IDs
- Dry run option
- Success message display
- Theme selector
- User avatar display

## Requirements

- Python 3.9
- Flask and other dependencies listed in requirements.txt

## Setup

1. Create a virtual environment:
```bash
python -m venv myenv
```

2. Activate the virtual environment:
- Windows:
```bash
myenv\Scripts\activate
```
- Unix/MacOS:
```bash
source myenv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask application:
```bash
python src/app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter the required trade information:
   - Trade ID
   - Clearing House LEI (defaults to 123456)
   - Clearing House Trade ID (must be at least 10 alphanumeric characters)

2. Click the "Add Entry" button to add more trade entries if needed

3. Toggle the "Dry Run" checkbox as needed

4. Click "Submit" to process the novation

5. A success message will be displayed when the novation is complete 