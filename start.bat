IF NOT EXIST venv (
    python -m venv venv
    REM Activate the python environment
    CALL venv\Scripts\activate.bat
    REM Install the requirements
    pip install -r requirements.txt
    REM Execute main-gpt4all.py
    python main-gpt4all.py
) ELSE (
    REM Activate the python environment
    CALL venv\Scripts\activate.bat
    REM Execute main-gpt4all.py
    python main-gpt4all.py
)