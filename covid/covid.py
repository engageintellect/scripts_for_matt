import os
import requests as req
from bs4 import BeautifulSoup
import time
import sys

os.system('clear')

    
# BEAUTIFUL SOUP SCRAPE
URL = 'https://www.worldometers.info/coronavirus/#countries'
page = req.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='nav-today')
content = results.find_all('td')

# COLLECTED SCRAPING DATA (LISTS)
us_list = []
world_list = []
newlist = []
world_pop = float(7800000000)

# LOOP TO ADD DATA TO LISTS
for x in content:
    x = x.text.strip()
    if x != '':
        us_list.append(x)
        world_list.append(x)
        newlist.append(x)

# SEARCH NEW DATA
#print(newlist.index('search'))

# sorted scraping range
#us_data = us_list[74:92]
# set startpoint for us list(to find correct line to read from)

if 'USA' in us_list:
    us_start_point = us_list.index('USA')
    us_start_point = us_start_point + 1
    us_data = us_list[us_start_point:]

#if 'Total:' in world_list:
#    world_start_point = world_list.index('Total:')
#    world_data = world_list[world_start_point:]
#
#    print(world_data)
#    quit()
#
world_data = world_list[-11:]

# conversions
cases = us_data[0].replace(',', '')
deaths = us_data[1].replace(',', '')
population = us_data[9].replace(',', '')

# statistics
infection_rate = float(cases)/float(population)*100
death_rate = float(deaths)/float(cases)*100
population_death = float(deaths)/float(population)*100

# PRINT DATA
print("   ▄▄▄   ▄▄▄▄  ▄    ▄ ▄▄▄▄▄  ▄▄▄▄          ▄▄▄     ▄▄▄▄")
print(" ▄▀   ▀ ▄▀  ▀▄ ▀▄  ▄▀   █    █   ▀▄          █    █▀  ▀▄")
print(" █      █    █  █  █    █    █    █          █    █▄  ▄█")
print(" █      █    █  ▀▄▄▀    █    █    █  ▀▀▀     █     ▀▀▀ █")
print("  ▀▄▄▄▀  █▄▄█    ██   ▄▄█▄▄  █▄▄▄▀         ▄▄█▄▄  ▀▄▄▄▀")
print("\n")
print(" (data scraped from www.worldometers.info/coronavirus/) ")
print("\n")
time.sleep(2)
os.system('clear')

print('CURRENT COVID-19 STATUS:')
time.sleep(1)
print('\n')


#print(us_data[0:14])
#quit()

# DISPLAY RESULTS

if us_data[10] == "North America":
    print('        =====[ US CASES ]=====        ')
    print('INFECTED:                   ' + us_data[0])
    print('DEATHS:                     ' + us_data[1])
    print('RECOVERED:                  ' + us_data[2])
    print('ACTIVE CASES                ' + us_data[3])
    print('CRITIAL CASES               ' + us_data[4])
    print('TEST GIVEN:                 ' + us_data[7])
    print('        =====[ US STATS ]======        ')
    print('US POPULATION:              ' + us_data[9])
    print('US INFECTION RATE:         ', '%', infection_rate)
    print('US DEATH RATE:             ', '%', death_rate)
    print('AMERICANS DEAD:            ', '%', population_death)
    print('\n')

elif us_data[11] == "North America":
    print('11 is NORTH AMERICA')
    print('        =====[ US CASES ]=====        ')
    print('INFECTED:                   ' + us_data[0])
    print('NEW CASES:                  ' + us_data[1])
    print('DEATHS:                     ' + us_data[2])
    print('RECOVERED:                  ' + us_data[3])
    print('ACTIVE CASES                ' + us_data[4])
    print('CRITIAL CASES               ' + us_data[5])
    print('TEST GIVEN:                 ' + us_data[8])
    print('        =====[ US STATS ]=====        ')
    print('US POPULATION:              ' + us_data[10])
    print('US INFECTION RATE:         ', '%',float(us_data[0].replace(',',''))/float(us_data[10].replace(',',''))*100)
    print('US DEATH RATE:             ', '%',float(us_data[2].replace(',',''))/float(us_data[0].replace(',',''))*100)
    print('AMERICANS DEAD:            ', '%',float(us_data[2].replace(',',''))/float(us_data[10].replace(',',''))*100)
    print('\n')

elif us_data[12] == "North America":
    print('12 is NORTH AMERICA')
    print('        =====[ US CASES ]=====        ')
    print('INFECTED:                   ' + us_data[0])
    print('NEW CASES:                  ' + us_data[1])
    print('DEATHS:                     ' + us_data[2])
    print('NEW DEATHS:                 ' + us_data[3])
    print('RECOVERED:                  ' + us_data[4])
    print('ACTIVE CASES                ' + us_data[5])
    print('CRITIAL CASES               ' + us_data[6])
    print('TEST GIVEN:                 ' + us_data[9])
    print('        =====[ US STATS ]=====        ')
    print('US POPULATION:              ' + us_data[11])
    print('US INFECTION RATE:         ', '%',float(us_data[0].replace(',',''))/float(us_data[11].replace(',',''))*100)
    print('US DEATH RATE:             ', '%',float(us_data[2].replace(',',''))/float(us_data[0].replace(',',''))*100)
    print('AMERICANS DEAD:            ', '%',float(us_data[2].replace(',',''))/float(us_data[11].replace(',',''))*100)
    print('\n')

elif us_data[13] == "North America":
    print('        =====[ US CASES ]=====        ')
    print('INFECTED:                   ' + us_data[0])
    print('NEW CASES:                  ' + us_data[1])
    print('DEATHS:                     ' + us_data[2])
    print('NEW DEATHS:                 ' + us_data[3])
    print('RECOVERED:                  ' + us_data[4])
    print('ACTIVE CASES                ' + us_data[6])
    print('CRITIAL CASES               ' + us_data[7])
    print('TEST GIVEN:                 ' + us_data[10])
    print('        =====[ US STATS ]=====        ')
    print('US POPULATION:              ' + us_data[12])
    print('US INFECTION RATE:         ', '%',float(us_data[0].replace(',',''))/float(us_data[12].replace(',',''))*100)
    print('US DEATH RATE:             ', '%',float(us_data[2].replace(',',''))/float(us_data[0].replace(',',''))*100)
    print('AMERICANS DEAD:            ', '%',float(us_data[2].replace(',',''))/float(us_data[12].replace(',',''))*100)
    print('\n')


else:
    print('US LIST FUCKED UP...CODE A SLUTION FOR DATA FLUCTUATIONS ON WORLDOMETERS.COM...')

print("\n")
print('        =====[ WORLD CASES ]=====        ')
print('INFECTED:                   ' + world_data[0])
print('NEW CASES                   ' + world_data[1])
print('DEATHS:                     ' + world_data[2])
print('NEW DEATHS:                 ' + world_data[3])
print('RECOVERED:                  ' + world_data[4])
print('ACTIVE CASES:               ' + world_data[6])
print('        =====[ WORLD STATS ]=====        ')
print('WORLD POPULATION:           ' + '7,800,000,000')
print('WORLD INFECTION RATE:      ', '%', float(world_data[0].replace(',',''))/world_pop*100)
world_pop_dead =  str(float(world_data[2].replace(',',''))/world_pop*100)
print('WORLD POP DEAD:            ', '%',float(world_data[2].replace(',',''))/world_pop*100)
print('WORLD DEATH RATE:          ', '%',float(world_data[2].replace(',',''))/float(world_data[0].replace(',',''))*100)
print('\n')


#======[ EXTRA ]======#

def extra():
    print('NOW THE CDC IS SAYING THAT THEY ESTIMATE ONLY 6% OF THE CONFIRMED DEATHS')
    print('HAVE ACTUALLY BEEN CAUSED BY CORONA VIRUS...')
    print('\n')
    print('6% of ' + us_data[1] + ' deaths in US is ' , int(us_data[1].replace(',','')) * .06)
    print('6% of ' + world_data[2] + ' deaths WORLDWIDE is ' , int(world_data[2].replace(',','')) * .06)
    time.sleep(30)
    os.system('clear')
    print('IN OTHER WORDS... CORONA VIRUS HAS BEEN 94% BULLSHIT.')
    time.sleep(3)

#extra()
