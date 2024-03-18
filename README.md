# IMDB Web Scraper.

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
Accepted Genres during execution.
All the Genres are from the IMDB website. So please make sure you type in only the provided Genres

Drama, Sci-Fi, Action, Comedy, Adventure, History, Animation, Thriller, Fantasy, Mystery, Short, Romance, War, Family, Horror, Music, Crime, Biography, Documentary, Western, Musical.

Accepted Keywords.

Music Video, Non Fiction, Tv Mini Series, 20th Century, Tv Special, Character Name In Title, Independent Film, Love, Murder, Female Nudity, Based On Novel, Number In Title, Year In Title, F Rated, Death, Family Relationships, Teenager, Father Son Relationship, Husband Wife Relationship, Bare Chested Male, Pandemic, Covid 19, Virus, Police, Dog, Coronavirus, Deadly Virus, 2010s, Health Crisis, Public Health Epidemic, Car, Lockdown, National Emergency, Interview

Once the key-word or genre is typed in the program will be executed. After execution the json file will be created in the same location as the program file. 
The json file would contain the data that was scraped from IMDB website.
