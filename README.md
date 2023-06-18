# Guild Network Map
A network map of all Discord Members in mutual servers.

![Network Map](/assets/network-map.png)

## What do the colours mean?
- Red: Friends
- Orange/Yellow: Bots
- Blue: Other Discord Users
- Green: Discord Servers

## How to use
1. Clone the repository
2. Install the dependencies
   3. `pip install -r requirements.txt`
3. Run the script
4. Open the `map.html` file in your browser
5. Enjoy!

## How it works
The script will iterate through all the members of all the mutual servers of the bot and create a node for each member. It will then iterate through all the mutual servers of each member and create an edge between the member and all the other members in the mutual servers.

## NOTICE
This script requires a selfbot to work. Selfbots are against the Discord Terms of Service. Use at your own risk.

This script was made for educational purposes only. I am not responsible for any damage caused by this script.