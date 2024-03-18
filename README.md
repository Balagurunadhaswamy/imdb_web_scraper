# IMDB Web Scraping Engine.

[![Bala](https://github.com/Balagurunadhaswamy)]

Clone this repository using "git clone https://github.com/Balagurunadhaswamy/imdb_web_scraper.git"

Create a python environment.
```py
pip install virtualenv
```

Activate the environment by running the following command, the command might differ according to the OS
I have followed Ubuntu commands, Alter the command according to the OS

```py
source venv/bin/activate
```

Once the environment is activated, run the following command in the same location of the 'requirements.txt' file.

```py
pip install -r requirements.txt
```
## Usage
Run the following command in the terminal
```py
python scraper.py
```

All keywords and genres as shown on the IMDB site presently works with the search engine as shown below

![image](https://github.com/Balagurunadhaswamy/imdb_web_scraper/assets/84098148/84675670-8251-460f-88cc-d285eca7ef8e)

![image](https://github.com/Balagurunadhaswamy/imdb_web_scraper/assets/84098148/06b0dbad-84f3-48bd-8e0b-97392627b786)


Once the key-word or genre is typed in, the search will be executed. After execution the json file will be created at the same root location.

Features:

- Error handled for all routines and logging enabled
- Automated pagination for all search results.
- Combination of Genre and Keywords, can be used independently as well
- Search results generated with single loop of execution for each page. Page progress shown on runtime.

Connect for more : 

[Linkedin](https://www.linkedin.com/in/balagurunadhaswamy-t-s-791410209/)
