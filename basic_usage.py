import spotify_web_controller as spy 

driver=spy.login('spotify_username or email','spotify_password','path_to_Chromedriver')

spy.playlist("playlist_name",driver)

spy.del_play(driver,"playlist_name")

spy.closedr(driver)