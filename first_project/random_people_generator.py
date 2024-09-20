import pandas as pd
from datetime import datetime, timedelta
import random

df = pd.read_csv('assets/brazilian-names-and-gender.csv')

def generate_random_name(row):
    random_first_name = random.choice(df['Name'])
    random_second_name = random.choice(df['Name'])
    random_name = random_first_name + ' ' + random_second_name
    first_name_gender = df.loc[df['Name'] == random_first_name, 'Gender'].iloc[0]

    return random_name, first_name_gender

df[['Name', 'Gender']] = df.apply(generate_random_name, axis=1, result_type='expand')

df = df.head(1000)

df_states = pd.read_csv('assets/estados.csv')

def random_state_generator(row, df_states):
    random_state = random.choice(df_states['NOME'])
    return random_state

df['State'] = df.apply(random_state_generator, df_states=df_states, axis=1)

def generate_random_birthdate(row):
    start_date = datetime.now() - timedelta(days=365 * 100)
    random_birthdate = start_date + timedelta(days=random.randint(0, 365 * 82))
    return random_birthdate

df['Birthdate'] = df.apply(generate_random_birthdate, axis=1)
df['Birthdate'] = df['Birthdate'].dt.date

def calculate_age(birthdate):
    current_date = datetime.now()
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    return age

df['Age'] = df['Birthdate'].apply(calculate_age)

df.to_csv('people.csv', index=False)