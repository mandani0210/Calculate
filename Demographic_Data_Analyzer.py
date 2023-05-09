import pandas as pd

# Load the dataset into a DataFrame
data = pd.read_csv("adult.data")

# 1. Count the number of people of each race
race_count = data["race"].value_counts()

# 2. Calculate the average age of men
avg_age_men = data.loc[data["sex"] == "Male", "age"].mean()

# 3. Calculate the percentage of people with a Bachelor's degree
percentage_bachelors = (data["education"] == "Bachelors").mean() * 100

# 4. Calculate the percentage of people with advanced education who make more than 50K
higher_education = data.loc[data["education"].isin(["Bachelors", "Masters", "Doctorate"])]
higher_education_rich = (higher_education["salary"] == ">50K").mean() * 100

# 5. Calculate the percentage of people without advanced education who make more than 50K
lower_education = data.loc[~data["education"].isin(["Bachelors", "Masters", "Doctorate"])]
lower_education_rich = (lower_education["salary"] == ">50K").mean() * 100

# 6. Calculate the minimum number of hours a person works per week
min_work_hours = data["hours-per-week"].min()

# 7. Calculate the percentage of the people who work the minimum number of hours per week and have a salary of more than 50K
num_min_workers = data.loc[data["hours-per-week"] == min_work_hours]
rich_percentage = (num_min_workers["salary"] == ">50K").mean() * 100

# 8. Identify the country with the highest percentage of people who earn >50K
highest_earning_country = (data.loc[data["salary"] == ">50K", "native-country"]
                           .value_counts(normalize=True)
                           .mul(100)
                           .idxmax())
highest_earning_country_percentage = (data.loc[data["salary"] == ">50K", "native-country"]
                                      .value_counts(normalize=True)
                                      .mul(100)
                                      .max())

# 9. Identify the most popular occupation for those who earn >50K in India
top_IN_occupation = (data.loc[(data["salary"] == ">50K") & (data["native-country"] == "India"), "occupation"]
                     .value_counts()
                     .idxmax())
# Print the answers
print(race_count)
print(avg_age_men)
print(percentage_bachelors)
print(higher_education_rich)
print(lower_education_rich)
print(min_work_hours)
print(rich_percentage)
print(highest_earning_country, highest_earning_country_percentage)
print(top_IN_occupation)

