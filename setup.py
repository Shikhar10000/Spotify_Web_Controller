from distutils.core import setup
setup(
  name = 'spotify_web_controller',         # How you named your package folder (MyLib)
  packages = ['spotify_web_controller'],   # Chose the same as "name"
  version = '0.1.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Spotify_Web_Controller using Selenium',   # Give a short description about your library
  author = 'Shikhar Maheshwari',                   # Type in your name
  author_email = 'shikhar10000@Live.com',      # Type in your E-Mail
  url = 'https://github.com/Shikhar10000/Spotify_Web_Controller',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Shikhar10000/Spotify_Web_Controller/archive/0.1.1.tar.gz',    # I explain this later on
  keywords = ['Spotify', 'Controller', 'Selenium','Chromedriver','spotify-web','play','pause'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'selenium',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.8',
  ],
)