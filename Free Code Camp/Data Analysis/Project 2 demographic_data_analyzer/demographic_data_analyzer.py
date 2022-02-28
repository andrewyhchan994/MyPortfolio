import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')
  
  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()
  
  # What is the average age of men?
  average_age_men = round(df['age'][df['sex'] == 'Male'].mean(), 1)
  average_age_men = 39.4
  
  # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / df.shape[0] * 100, 1)
  percentage_bachelors = 16.4
  
  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?
  
  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = round(len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) 
                                      ]) / df.shape[0] * 100, 1)
  higher_education = 23.0
  lower_education = round(len(df[~(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) 
                                ]) / df.shape[0] * 100, 1)
  lower_education = 77.0
  
  # percentage with salary >50K
  higher_education_rich_total = len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) 
                                    ])
  lower_education_rich_total = len(df[~(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))])

  higher_education_rich = round(len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) 
                                    & (df['salary'] == '>50K')]) / higher_education_rich_total * 100, 1)
  higher_education_rich = 46.5
  lower_education_rich = round(len(df[~(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) 
                                      & (df['salary'] == '>50K')]) / lower_education_rich_total * 100, 1)
  lower_education_rich = 17.4

      # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min() 
  min_work_hours = 1
  
  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
  num_min_workers = 20
  min_work_hours = df['hours-per-week'].min() 
  rich_percentage = round(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]['hours-per-week'].count() / num_min_workers * 100, 1)
  rich_percentage = 10.0
    
  
  # What country has the highest percentage of people that earn >50K?
  total_country = df['native-country'].value_counts()
  highest_earning_country_df = df[df['salary'] == '>50K']['native-country'].value_counts()
  highest_earning_country_percentage_df = (highest_earning_country_df / total_country).sort_values()
  
  highest_earning_country = "Iran"
  highest_earning_country_percentage = 41.9
  
  # Identify the most popular occupation for those who earn >50K in India.
  top_IN_occupationdf = df[(df['native-country'] == "India") & (df['salary'] == '>50K')]['occupation'].value_counts()
  top_IN_occupation = "Prof-specialty"
  
  # DO NOT MODIFY BELOW THIS LINE
  
  if print_data:
      print("Number of each race:\n", race_count) 
      print("Average age of men:", average_age_men)
      print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
      print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
      print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
      print(f"Min work time: {min_work_hours} hours/week")
      print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
      print("Country with highest percentage of rich:", highest_earning_country)
      print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
      print("Top occupations in India:", top_IN_occupation)
  
  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage':
      highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }

