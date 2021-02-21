# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla',
         'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch',
         'Isabel', 'Ivan', 'Emily', 'Katrina',
         'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October',
          'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August',
          'October', 'September', 'September',
          'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September',
          'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005,
         2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180,
                       185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'],
                  ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'],
                  ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'],
                  ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'],
                  ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M',
           '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B',
           '23.3B', '1.01B', '125B', '12B',
           '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:
conversion = {"M": 1000000,
              "B": 1000000000}


def damage_in_float(damages_list):
    updated_damages_list = []
    for dmg in damages_list:
        if dmg != 'Damages not recorded':
            if dmg[-1] == 'M':
                updated_damages_list.append(float(dmg.strip('M')) * conversion['M'])
            else:
                updated_damages_list.append(float(dmg.strip('B')) * conversion['B'])
        else:
            updated_damages_list.append(dmg)
    return updated_damages_list


updated_damages = damage_in_float(damages)


print("Updated Damage:\n" + str(updated_damages))


# write your construct hurricane dictionary function here:
def construct_dict(names_list, months_list, years_list, max_sustained_winds_list, area_affected_list, damage_list,
                   deaths_list):
    hurricane_dict = {}
    for i in range(len(names_list)):
        hurricane_dict[names_list[i]] = {'Name': names_list[i], 'Month': months_list[i], 'Year': years_list[i],
                                         'Max Sustained Wind': max_sustained_winds_list[i],
                                         'Area affected': area_affected_list[i],
                                         'Damage': damage_list[i], 'Death': deaths_list[i]}

    return hurricane_dict


hurricanes = construct_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

print("\nlist of all hurricanes:\n" + str(hurricanes))


# write your construct hurricane by year dictionary function here:
def arrange_hurricanes_by_year(names_list, months_list, years_list, max_sustained_winds_list, areas_affected_list,
                               updated_damages_list, deaths_list):
    hurricane_by_year_dict = {}
    i = 0
    while i < len(years_list):
        values = []
        for j in range(years_list.count(years_list[i])):
            values.append({'Name': names_list[i + j], 'Month': months_list[i + j], 'Year': years_list[i + j],
                           'Max Sustained Wind': max_sustained_winds_list[i + j],
                           'Area affected': areas_affected_list[i + j],
                           'Damage': updated_damages_list[i + j], 'Death': deaths_list[i + j]})
        hurricane_by_year_dict[years_list[i]] = values
        i += 1 + years_list.count(years_list[i]) - 1

    return hurricane_by_year_dict


hurricane_by_year = arrange_hurricanes_by_year(names, months, years, max_sustained_winds, areas_affected,
                                               updated_damages, deaths)


print("\nHurricanes by year:\n" + str(hurricane_by_year))


# write your count affected areas function here:
def times_affected(hurricanes_dict):
    unique_areas = {}
    for value_dict in hurricanes_dict.values():
        for area in value_dict['Area affected']:
            if not (area in unique_areas):
                unique_areas[area] = 1
            else:
                unique_areas[area] += 1

    return unique_areas


num_areas_affected = times_affected(hurricanes)


print("\nNumber of times an area got affected:\n" + str(num_areas_affected))


# write your find most affected area function here:
def most_affected_area(num_areas_affected_dict):
    max_affected = ''
    count = 0
    for key, val in num_areas_affected_dict.items():
        if val > count:
            count = val
            max_affected = key
    print(f"\n{max_affected} was affected the highest by {count} hurricanes.")


most_affected_area(num_areas_affected)


# write your greatest number of deaths function here:
def max_deaths(hurricane_dict):
    max_death = 0
    hurricane = ''
    for val in hurricane_dict.values():
        if val['Death'] > max_death:
            max_death = val['Death']
            hurricane = val['Name']

    print(f'\n{hurricane} caused the maximum deaths of {max_death}.')


max_deaths(hurricanes)

# write your categorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}


def mortality_rating(hurricane_dict):
    mort_rating_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for key, val in hurricane_dict.items():
        if val['Death'] == 0:
            mort_rating_dict[0].append(key)
        elif 0 < val['Death'] <= 100:
            mort_rating_dict[1].append(key)
        elif 100 < val['Death'] <= 500:
            mort_rating_dict[2].append(key)
        elif 500 < val['Death'] <= 1000:
            mort_rating_dict[3].append(key)
        elif 1000 < val['Death'] <= 10000:
            mort_rating_dict[4].append(key)
        elif 10000 < val['Death']:
            mort_rating_dict[5].append(key)

    return mort_rating_dict


mortality_rating_hurricanes = mortality_rating(hurricanes)
print("\nHurricane mortality rating:\n" + str(mortality_rating_hurricanes))


# write your greatest damage function here:
def max_damage(hurricane_dict):
    max_dmg = 0
    hurricane = ''
    for key, val in hurricane_dict.items():
        try:
            if val['Damage'] > max_dmg:
                max_dmg = float(val['Damage'])
                hurricane = key
        except:
            continue
    print(f'\n{hurricane} caused the maximum damage of worth {max_dmg}.')


max_damage(hurricanes)

# write your categorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


def damage_rating(hurricane_dict, dmg_scale):
    dmg_rating_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, val in hurricane_dict.items():
        try:
            if val['Damage'] == 0:
                dmg_rating_dict[0].append(key)
            elif 0 < val['Damage'] <= dmg_scale[1]:
                dmg_rating_dict[1].append(key)
            elif dmg_scale[1] < val['Damage'] <= dmg_scale[2]:
                dmg_rating_dict[2].append(key)
            elif dmg_scale[2] < val['Damage'] <= dmg_scale[3]:
                dmg_rating_dict[3].append(key)
            elif dmg_scale[3] < val['Damage'] <= dmg_scale[4]:
                dmg_rating_dict[4].append(key)
            elif dmg_scale[4] < val['Damage'] <= dmg_scale[5]:
                dmg_rating_dict[5].append(key)

        except:
            continue

    return dmg_rating_dict


hurricane_damage_rating = damage_rating(hurricanes, damage_scale)
print("\nHurricane Damage Rating:\n" + str(hurricane_damage_rating))
