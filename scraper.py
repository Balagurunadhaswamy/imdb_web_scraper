# -*- coding: utf-8 -*-
# scraper.py
# This file contains scrape core and utility functions
# Author - Akash S
##################################################################

import datetime
import json
import logging
import requests
import sys

from time import sleep

from bs4 import BeautifulSoup
from settings import url, headers

stdlogger = logging.getLogger(__name__)

def create_bsobj(response):
    """_summary_

    Args:
        response: Requests response object

    Returns:
        soup (BeautifulSoupObj): Active Beautiful soup html parser

    """
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def fetch_details(keyword, genre, page = 1):
    """_summary_

    Args:
        keyword (str): Search keyword input by user
        genre (str): Genre input by user
        page (int, optional): Page number. Defaults to 1.

    Returns:
        response: Requests response object
    """
    if keyword and genre:
        params = {"keywords": keyword, "genres":genre, "title_type":"movie", "page":page}
    elif genre:
        params = {"genres":genre, "title_type":"movie", "page":page}
    else:
        params = {"keywords":keyword, "title_type":"movie","page":page}
    response = requests.get(url, params, headers=headers)
    return response

def get_pages(soup_obj):
    """Get the total number of pages for parsing

    Args:
        soup_obj (BeautifulSoupObj): Active Beautiful soup html parser

    Returns:
        total_page: total number of pages
        total_count : total count of records found 
    """
    total_page = 1
    try:
        total_count = int(soup_obj.select(".desc")[0].text.strip().split()[4].replace(",",""))
    except:
        sys.exit("No search results found for keyword. Try again!")
    if total_count > 50:
        total_page = round(int(float(total_count/50))) + 1
    return total_page, total_count

def create_data(keyword, genre, page=1):
    """Create data dictionary from scrapped info for json object

    Args:
        keyword (str): Search keyword input by user
        genre (str): Genre input by user
        page (int, optional): Page number. Defaults to 1.

    Returns:
        imdb_data: list of imdb search record objects
        pages : total number of search result pages
    """
    response = fetch_details(keyword, genre, page)
    imdb_data = []
    soup_obj = create_bsobj(response)
    pages = get_pages(soup_obj)
    (directors, stars, summaries, imdb_rates, 
     genres, titles, years) = fetch_imdb_data(soup_obj)
    for i, each in enumerate(titles):
        imdb_data.append({
            "title" : titles[i],
            "release_year":years[i],
            "genre":genres[i],
            "imdb_ratings":imdb_rates[i],
            "directors": directors[i],
            "cast":stars[i],
            "summary":summaries[i]
        })
    return imdb_data, pages

def fetch_imdb_data(soup_obj):
    """
    Fetches imdb data from the parsed beautiful soup html content
    in a single loop extraction.

    Args:
        soup_obj (BeautifulSoupObj): Active Beautiful soup html parser

    Returns:
        directors, stars, summaries, 
        imdb_rates, genres, titles, years (lists): Contains respective page 
        search result details
    """
    lister_items = soup_obj.select(".lister-item-content")
    dir_stars, summaries = [], []
    directors, stars = [], []
    imdb_rates, genres = [], []
    titles, years = [], []
    for i, each in enumerate(lister_items):
        
        # Detect and extract director and stars data
        try:
            dir_stars.append(each.select("p")[2].text)
        except:
            dir_stars.append("Directors:N/A | Stars:N/A")
        director_star_data = dir_stars[i].split("|")
        if len(director_star_data) > 1:
            directors.append((director_star_data[0]
                                .replace("\n", "")
                                .replace("Director:", "")
                                .replace("Directors:", "")).strip())
            stars.append((director_star_data[1]
                                .replace("\n", "")
                                .replace("Stars:", "")
                                .replace("Star:", "")).strip())
        elif len(director_star_data) == 1:
            directors.append("N/A")
            stars.append((director_star_data[0]
                                .replace("\n", "")
                                .replace("Stars:", "")
                                .replace("Star:", "")).strip())
        
        # Detect and extract summaries
        try:
            summaries.append(each.select("p")[1]
                             .text.split("  ")[0].strip())
        except:
            summaries.append("No Plot")

         # Detect and extract ratings
        try:
            imdb_rates.append(each.select(
                ".ratings-imdb-rating strong")[0].text)
        except:
            imdb_rates.append("N/A")
        
         # Detect and extract genres
        try:
            genres.append(each.select(".genre")[0].text)
        except:
            genres.append("N/A")
       
         # Detect and extract titles
        try:
            titles.append(each.select(".lister-item-header a")[0].text)
        except:
            titles.append("N/A")
    
         # Detect and extract release years
        try:
            years.append(each.select(".lister-item-year")[0].text)
        except:
            years.append("N/A")
    return directors, stars, summaries, imdb_rates, genres, titles, years

def main(): 
    """Main function
    """

    genre = input("Enter genre > ")

    try:
        keyword = input("Enter keyword > ")
    except Exception as e:
        stdlogger.exception(e)
        
    final_data = []
    page = 1 
    
    while True:
        data, is_more = create_data(keyword, genre, page)
        if page == 1:
            print("\nTotal Search results found : " + str(is_more[1]) +'\n')    
        final_data.extend(data)
        if len(data) < 50:
            break
        print("Saving Pages "+str(page)+" of "+ str(is_more[0])+" ...")
        page += 1
    now = datetime.datetime.now().strftime("%H:%M:%S")
    with open('search-results_'+keyword+'_'+str(now)+'.json', 'w') as f:
        json.dump(final_data, f)
    print("\nSearch results saved successfully! Results are saved in file - "+ 
          'search-results_'+keyword+'_'+now+'.json')
    
if __name__ == '__main__':
    main()


