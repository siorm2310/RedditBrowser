import sys
import webbrowser
# URL is https://redditp.com/r/sub1+sub2+sub3/?t=TypeOfTop

BASE_URL = "https://redditp.com/r"

def add_subs(subs_list):
    subs_string = ''
    for sub in subs_list:
        subs_string+=f"{sub}+"
    return subs_string[:-1] # Drop last "+"

def main():
    Subs_select = input("Please select subreddits (seperate by space) : ")
    Top_select = input("Please select : Top of today / week / month / year / all time : ")
    incognito = input("Incoginto mode? :) y/n : ")
    
    Subs_list = Subs_select.split()
    Subs_string = add_subs(Subs_list)
    try:
        TopType = {
        "today" : "t=today",
        "week" : "t=week",
        "month" : "t=month",
        "year" : "t=year",
        "all time" : "t=all",
        }[Top_select]
    except Exception as e:
        print("Error reading Top selection. defaulting to Top of all time")
        TopType = "t=all"

    try:
        incognito_select = {
            "y" : True,
            "n" : False
        }[incognito]
    except Exception as e:
        incognito_select = False

    if incognito_select:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
        webbrowser.get(chrome_path).open_new(f"{BASE_URL}/{Subs_string}/top/?{TopType}")
    else:
        webbrowser.open_new_tab(f"{BASE_URL}/{Subs_string}/top/?{TopType}")

    return

if __name__ == "__main__":
    main()