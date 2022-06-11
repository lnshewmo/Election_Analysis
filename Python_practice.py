# use an index to print an item in a list
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if counties[2] != 'Jefferson':
    print(counties[2])
else:
        print("incorrect index")

# membership operators IN and NOT IN
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print('El Paso is not in the list of counties')

# logical operators AND 
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties")

    # logical operators OR
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of countes")
else:
    print("Arapahoe or El Paso is not in the list of counties")

    # repetion statement FOR loop
counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)

    # repetion statement FOR using RANGE funtion
counties = ["Arapahoe","Denver","Jefferson"]
for county in range(len(counties)):
    print(counties[county])

    # repetition statement FOR to get KEYS from a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

 # repetition statement FOR to get KEYS from a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)

# repetition statement FOR to get VALUES from a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.values():
    print(county)

# get VALUES from a dictionary using dictionary_name[key]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict[county])

# get VALUES from a dictionary using .get()
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict.get(county))

# get KEY VALUE pairs from a dictionary using ITEMS
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,voters in counties_dict.items(): # defines variables
    print(county, voters)

# get KEY VALUE pairs from a dictionary using ITEMS
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,voters in counties_dict.items(): # defines variables
    print((county) + " county has " + str(voters) + " registered voters.")  

# get each dictionary i"n a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353}, 
                {"county":"Jefferson", "registered voters": 432438}]
for counties_dict in voting_data:
    print(counties_dict)

# get each dictionary in a list of dictionaries using RANGE()
voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353}, 
                {"county":"Jefferson", "registered voters": 432438}]
for counties_dict in range(len(voting_data)):
    print(voting_data[counties_dict])

# get only KEYS from a list of dictionaries using RANGE()
voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353}, 
                {"county":"Jefferson", "registered voters": 432438}]
for counties_dict in range(len(voting_data)):
    print(voting_data[counties_dict]["county"])

# get only VALUES from a list of dictionaries using RANGE()
voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353}, 
                {"county":"Jefferson", "registered voters": 432438}]
for counties_dict in range(len(voting_data)):
    print(voting_data[counties_dict]["registered voters"])

# get KEY then VALUE from a list of dictionaries using VALUES() and nested FOR
voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353}, 
                {"county":"Jefferson", "registered voters": 432438}]
for counties_dict in voting_data:
    for voters in county_dict.values():
        print(voters)

# get KEY only from a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353}, 
                {"county":"Jefferson", "registered voters": 432438}]
for counties_dict in voting_data:
    print(counties_dict["county"])

# get VALUE only from a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353}, 
                {"county":"Jefferson", "registered voters": 432438}]
for counties_dict in voting_data:
    print(counties_dict["registered voters"])