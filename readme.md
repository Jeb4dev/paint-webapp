# real time chat made* in 50 min


## Purpose
This project was made as part of the weekly programming challenge hosted by [DevJam].
The project was made for learning purposes. Made by Jeb and mihett05.

### Why is this such a dissapointment

Olimme kunnianhimoisia ja yritimme tehdä liian laajan projektin. arvioimme väärin ajan, joka meillä menisi projektin tekoon. Lisäksi yritimme tehdä projektin minulle (jeb) vieraalla frameworkilla. I still wanted to participate and this is what I wrote in 50 minutes from what we had done in paint app. have mercy on me.
[Repository](https://github.com/mihett05/nice-chat) for original chat-app we tried to do, that we didn't finnish. 
### What I learned
Don't try to do too much, especially when eorking with such a little of time and new framework. Will do better next time. Thank you.

## [Live Demo](https://jeb-chatapp.herokuapp.com/)
Chat page, no styling
![image](https://user-images.githubusercontent.com/76889226/145431138-11618ce5-d3d8-42da-ba20-1321762afdf2.png)



## About the Challenge
#### 🛠 Difficulty Level: Intermediate 
📅 Start: December 3rd<br>
📅 Deadline: December 9th 16:00 (4PM) GMT

#### 📝 Project Description
Create digital artwork on a canvas on the web to share online and also export as images.


##### 📑User Stories
-  ✔️ User is prompted to enter a username when he visits the chat app. The username will be stored in the application
-  ✔️ User can see an `input field` where he can type a new message
-  ✔️ By pressing the `enter` key or by clicking on the `send` button the text will be displayed in the `chat box` alongside his username (e.g. `John Doe: Hello World!`)

##### 🌟 Bonus features

-   ✔️ The messages will be visible to all the Users that are in the chat app (using WebSockets)
-   [ ] When a new User joins the chat, a message is displayed to all the existing Users
-   [ ] Messages are saved in a database
-   [ ] User can send images, videos and links which will be displayed properly
-   [ ] User can select and send an emoji
-   [ ] Users can chat in private
-   [ ] Users can join `channels` on specific topics



## Tech

The app is written in python using Flaks-library. 
Client communicates with server using post request, sockets and api. 
Images are drawn using canvas and uploaded to external server using api. 
"Draw and Guess" -game uses' flask socketIO-sockets.

#### Frameworks and libraries:

- [Flask] - Micro web framework written in python.
- [Flask-Socketio](https://flask-socketio.readthedocs.io/en/latest/) - Flask-SocketIO gives Flask applications access to low latency bi-directional communications between the clients and the server.
- [Flask-login] - Flask-Login provides user session management for Flask.
#### Deployment
- [Heroku](https://www.heroku.com) - Heroku is a cloud platform as a service supporting several programming languages.



## Installation and running

This app requires [python 3.7+](https://www.python.org/downloads/) to run.

Clone git repo
```sh
git clone https://github.com/JesperKauppinen/keyboard-race.git
```

After cloning or downloading this git repo, install required python libraries

```sh
pip install -r requirements.txt
```

run app.py
```sh
python app.py
```
### Deployment
App is hosted in heroku. Use `HEROKU` branch for herou deployment as it also contains `Procfile`.


## Contribute?
Want to contribute? Awesome!  
This project was part of weekly challenges hosted by [DevJam] and won't be updated.
Maybe you would like to work with us, hit me up and let's talk. :)

## Credits
none

## License
MIT


   [Flask]: <https://flask.palletsprojects.com/en/2.0.x/>
   [Flask-login]: <https://flask-login.readthedocs.io/en/latest/>
   [DevJam]: <https://discord.gg/nZBxGEudY6>
   [emojipedia]: <https://emojipedia.org/artist-palette/>
   [icons8]: <https://icons8.com/>
   [sharingbuttons]: <https://sharingbuttons.io/>
   [Handdrawn]: <https://fxaeberhard.github.io/handdrawn.css/>
   [imgbb]: <https://imgbb.com/upload>
