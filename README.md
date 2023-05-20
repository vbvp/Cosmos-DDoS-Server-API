# Cosmos Stresser API made by Robert
big d00s server api. nothing complicated at all.... i made this in 20 minutes. yet its already better than most of the open source php ones. 

It works with python-flask and waitress. Routes GET arguments are validated with mozilla-bleach and some other validations techniques (ip, port, time....). I also use paramiko to create a ssh request and execute commands (i dont parse any in-out tho.... might do that in the future). The biggest change is using a match-case to parse method and execute different CMDS according to your l33t hacking scripts (most of php ones use if-elif-elif-elif-elif-elif type shit). 

will add more updates in the future..

![2023-02-15 17_14_07-C__Windows_System32_cmd exe - py  main py](https://user-images.githubusercontent.com/70919730/219189832-31fb5b66-d8f9-4b10-bc34-a50b40d82fcb.png)
![2023-02-19 15_42_39-#general _ robert 's server - Discord](https://user-images.githubusercontent.com/70919730/219974109-914cfa4a-b6e1-4097-82ce-abed274e4d37.png)

[Tutorial (not a good tutorial at all)]

1: Install requirements (py -m pip install requirements)

2: Change keys in admin_keys.json

3: Change your webhook in decorators.py

4: Change your commands in the route start_flood.py

5: Start the api (py main.py)

Usage: http://[SERVER_IP]:5000/flood?key=[KEY]&target=[TARGET]&port=[PORT]&time=[TIME]&method=[METHOD]


[To do]

- Add black list using a range of ips on the same network
