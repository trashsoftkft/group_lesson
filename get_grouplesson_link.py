import time
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from gym_handler import Gym
from data_save import save_data
import csv

#selector
time_table_css = ".timetable-btn"

def get_time_table_link(gym):
    #create driver
    driver = webdriver.Firefox(executable_path='/home/botond/developer_tools/geckodriver')
    #wisit gym subsite
    driver.get(gym.link)
    #try get timetable link
    try:
        time_table_element = driver.find_element_by_css_selector(time_table_css)
        return time_table_element.get_attribute("href")
    except:
        return ""
    finally:
        driver.close()
