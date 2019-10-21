# First releae of spotify_web_controller
## Version 0.1
## A web based spotify player
### Available functions:-

#### 1. Login

```
import spotify_web_controller as spy
driver=spy.login('spotify_username','spotify_pass','path_to_chromedriver')
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