@echo off
if exist venv (
    echo "venv" file found. Skipping installation...
    echo Opening autototem.py...
    start autototem.py
) else (
    echo "venv" file not found. Creating a virtual environment...
    python -m venv venv
    call venv\Scripts\activate

    echo Installing dependencies...
    pip install -r requirements.txt

    echo Installation complete.
    echo Opening autototem.py...
    start autototem.py
)
