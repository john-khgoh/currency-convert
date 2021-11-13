## Web API conversion

1. To use the web API directly, you can visit the following url: https://currency-convert-1.herokuapp.com/  

2. The input format is as follows:  
https://currency-convert-1.herokuapp.com/convert/original_currency/target_currency/input_value

For example,  
https://currency-convert-1.herokuapp.com/convert/USD/EUR/1.0  
https://currency-convert-1.herokuapp.com/convert/eur/jpy/2  

3. The expected output should be:  
{"value":"0.87","currency":"eur"}  
{"value":"260.68","currency":"jpy"}   

Note: Heroku, the web hosting service requires all free applications to sleep for 6 hours every day.  
The web API should be up and running between 8am - 2am CET. Should you encounter errors, please contact jkh.goh@gmail.com.

## Web API update

The currency exchange rate can be updated from an external site using:
https://currency-convert-1.herokuapp.com/update-rate

## CLI using the web API  

Run the batch file using the following command. Change the target currency and input file, as required.  
python cli.py --file "input.json" --target-currency EUR  

## CLI using the localhost API  

1. To use the API in localhost mode, first uncomment the "127.0.0.1:8008" address in cli.py and comment out the website address.  

2. Run the following command in command prompt (Windows) or terminal (*nix):  
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8008  

3. In another command prompt or terminal, run the batch file using the following command. Change the target currency and input file, as required.
python cli.py --file "input.json" --target-currency EUR
