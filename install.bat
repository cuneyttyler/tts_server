echo Installing packages

winget install -e --id Python.Python.3.10 --scope machine
SET PATH="%PATH%;C:\Program Files\Python310"
SET PYTHONUTF8=1
py -3.10 -m venv venv
call venv/scripts/activate

pip install --upgrade pip
pip install torch==2.5.1+cu118 torchaudio==2.5.1+cu118 --index-url https://download.pytorch.org/whl/cu118
pip install -r .\requirements.txt --use-deprecated=legacy-resolver

echo Install complete.
pause