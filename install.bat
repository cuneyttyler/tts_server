echo Installing packages

winget install -e --id Python.Python.3.10
python -m venv venv
call venv/scripts/activate

pip install torch==2.5.1+cu118 torchaudio==2.5.1+cu118 --index-url https://download.pytorch.org/whl/cu118
pip install -r .\requirements.txt

echo Install complete.
pause