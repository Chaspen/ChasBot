# ChasBot
Basic Discord bot

# Setup
- Get an account at the [Discord Developer Portal](https://discord.com/developers)
- Make a new application and name it
- Go under "Bot"
- Check any permissions nescessary ('Send Messages', 'Attach Files', 'Connect', and 'Speak' are required for functionality provided here)
- Get token on this same page
- in ```main.py```, put in privided token:

```python
tkn = 'YOUR_TOKEN_HERE'
```


# Running

[Python 3.8](https://www.python.org/) or above is required.

## Windows
  Open up a CMD or Powershell window and run:
  ```
  py -3 -m pip install -U discord.py[voice]
  ```
  
  
## Linux
  Open up a terminal and run:
  ```
  python3 -m pip install -U discord.py[voice]
  ```
  
  
Navigate to the project directory and run ```main.py`` with either ```python3 main,py``` for Linux or ```py -3 main.py``` for Windows.
