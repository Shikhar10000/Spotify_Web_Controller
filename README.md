# First release of spotify_web_controller
## Version 0.1.3
## A web based spotify player
spotify_web_controller is a wrapper library to control spotify using chromedriver/GeckoDriver. Ideas for implementation of more features will be greatly appreciated. 

### Note:-
Chromedriver/GeckoDriver must be downloaded and path must be provided to the login function in order for package to work correctly.

and make sure 

chromeDriver version = Version of your chrome

#### chrome driver download link:-

https://chromedriver.chromium.org/downloads

#### GeckoDriver download link:-

https://github.com/mozilla/geckodriver/releases

### Available functions:-

#### 1a. Login

```
import spotify_web_controller as spy
driver=spy.login('spotify_username','spotify_pass','path_to_chromedriver')
```

#### 1b. Login using Facebook

```
import spotify_web_controller as spy
driver=spy.login_fb('fb_username','fb_pass','path_to_chromedriver')
```

#### 2. play_playlist

```
spy.playlist("playlist_name",driver)
```

#### 3. delete_playlist

```
spy.del_play(driver,"playlist_name")
```

#### 4. Exit

```
spy.closedr(driver)
```

## How to Use
### Steps:
1. Clone the repo or download the zip file.
2. Install the package, for eg. 'pip3 install spotify_web_controller'.
3. Open basic_usage.py showcase the already implemented basic functionalities.
4. Replace spotify username, password and the path to chrome driver. For path to the chrome driver, first check your chrome browser version by going to Help < About Google Chrome. Then download the appropriate driver from the chrome driver download link provided above. Once downloaded, move the .exe file to the spotify_web_controller directory/folder. 
5. At this point, you're ready to implement the package. Feel free to play around with the settings in __init.py__.

