# Online Drawing and Guessing Game


## Purpose
This project was made as part of the weekly programming challenge hosted by [DevJam].
The project was made for learning purposes. Made by Jeb and mihett05.


## [Live Demo](https://art-race.herokuapp.com)
### Gallery Page
![image](https://user-images.githubusercontent.com/76889226/144460258-92261a05-eb47-4703-9cb7-878d041160e5.png)

### Drawing in Guessing game (like scribble.io)
![image](https://user-images.githubusercontent.com/76889226/144343961-fc555104-fd68-4764-9fd8-d36898d5e250.png)



## About the Challenge
#### 🛠 Difficulty Level: Intermediate 
📅 Start: November 26th<br>
📅 Deadline: December 2nd 16:00 (4PM) GMT

#### 📝 Project Description
Create digital artwork on a canvas on the web to share online and also export as images.


##### 📑User Stories

-   ✔️ User can draw in a `canvas` using the mouse
-   ✔️ User can change the color
-   ✔️ User can change the size of the tool
-   ✔️ User can press a button to clear the `canvas`

##### 🌟 Bonus features (optional)

-   ✔️ User can save the artwork as an image (`.png`, `.jpg`, etc format)
-   ✔️ User can draw different shapes (`rectangle`, `circle`, `star`, etc)
-   ✔️ User can share the artwork on social media
-   ✔️ Users can start a game, and compete in a game of Pictionary

##### ✨ Custom features (not part of the challenge)
- ✔️ Users can like images
- ✔️ Users can go same session and chat
- ✔️ User can upload their artwork to the server
- ✔️ All artworks are listed in Gallery
- ❌    User get 3 words and can choose whitch word to draw
-  ✔️ Other users try to guess this word



## Tech

The app is written in python using Flaks-library. 
Client communicates with server using post request, sockets and api. 
Images are drawn using canvas and uploaded to external server using api. 
"Draw and Guess" -game uses' flask socketIO-sockets.

#### Frameworks and libraries:

- [Flask] - Micro web framework written in python.
- [Flask-Socketio](https://flask-socketio.readthedocs.io/en/latest/) - Flask-SocketIO gives Flask applications access to low latency bi-directional communications between the clients and the server.
- [Flask-login] - Flask-Login provides user session management for Flask.
- [Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) is used for drawing shapes.
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
#### imfbb Api
Images are uploaded on imfbb servers.
If you want to save images on the server, you need api key from [imgbb]. Save api key in environment variable: `IMG_BB_API_KEY`.

### Deployment
App is hosted in heroku. To host app in heroku you need to enable `heroku-postgresq`. You also need to add the api key as convar environment variable. 
Use `HEROKU` branch for herou deployment as it also contains `Procfile`.


## Contribute?
Want to contribute? Awesome!  
This project was part of weekly challenges hosted by [DevJam] and won't be updated.
Maybe you would like to work with us, hit me up and let's talk. :)

## Credits
- [emojipedia] - Whatsapp artist-palette emoji for favicon.
- [icons8] - Icon in svg.
- [emojipedia] - Social media sharing buttons.
- [Handdrawn] - Hand drawn font and icons

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
