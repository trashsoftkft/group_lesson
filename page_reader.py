import time
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

#links
gym_list_path = "https://allyoucanmove.hu/elfogadohelyek"

#strings
group_string = "Csoportos óra "

#selector
lesson_dropdown_css_sel = "div.col-sm-6:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"
group_lesson_css = "div.option:nth-child(%d)"
gym_css = "#gym-list > div.item"
lesson_list_dropdown = "div.option"

#create driver
driver = webdriver.Firefox(executable_path='/home/botond/developer_tools/geckodriver')

driver.get(gym_list_path)
lesson_dropdown = driver.find_element_by_css_selector(lesson_dropdown_css_sel)

#move second line These commands are for avoiding to activate an unnecessarry dropdown which hides lesson type selector
def move_second_line():
    second_line = driver.find_element_by_css_selector("div.item:nth-child(8) > a:nth-child(2)")
    webdriver.ActionChains(driver).move_to_element(second_line).move_to_element(lesson_dropdown).click(lesson_dropdown).perform()
    time.sleep(2)

#get position od grouplesson in lesoon type dropdown
def get_grouplesson_list_position():
    lesson_list = driver.find_elements_by_css_selector(lesson_list_dropdown)
    for lesson in lesson_list:
        if (lesson.get_attribute("innerHTML") == group_string):
            return lesson_list.index(lesson)
    return -1

#Select grouplesson
def select_grouplesson(position):
    group_lesson = driver.find_element_by_css_selector(group_lesson_css % position)
    webdriver.ActionChains(driver).move_to_element(group_lesson).click(group_lesson).perform()

#get list of all gym.
def get_list_of_gym():
    list = driver.find_elements_by_css_selector(gym_css)
    previous_list = []
    while len(list) > len(previous_list):
        driver.execute_script("window.scrollTo(0, 20000)")
        time.sleep(3)
        previous_list = list[:]
        list = driver.find_elements_by_css_selector(gym_css)
        break
    return list

#get address and name of gym
def get_details(gym):
    name = gym.find_element_by_css_selector("div.item-text > div.item-name").get_attribute("innerHTML")
    address = gym.find_element_by_css_selector("div.item-text > div.item-address").get_attribute("innerHTML")
    gym_link = gym.find_element_by_css_selector("div.item > a").get_attribute("href")

    return [name, address, gym_link]


move_second_line()
position = get_grouplesson_list_position()
select_grouplesson(position)
list_of_gym = get_list_of_gym()
for gym in list_of_gym:
    print(get_details(gym))

driver.close()
