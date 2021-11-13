1. Start the local webserver by using the following command in command prompt (Windows) or terminal (*nix).
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8008

2. Once started, open another cmd/terminal, and run the following command. Change the target currency and file, as required. 
python cli.py --target-currency usd --file "input.json"