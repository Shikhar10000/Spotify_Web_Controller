# First releae of spotify_web_controller
## Version 0.1.3
## A web based spotify player

### Note:-
Chromedriver/GeckoDriver musht be dowloaded and path must be provided to the login function in order for package to work correctly

and make sure 

chromeDriver version= Version of your chrome

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
