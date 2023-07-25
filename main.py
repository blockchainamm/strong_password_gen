# Import required libraries
import string
import secrets
import pandas as pd
from tabulate import tabulate

def gen_password(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    
    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

passworddf = pd.DataFrame(columns=('index' , 'password'))

for _, index in enumerate(range(10)):
    new_pwd = gen_password(50, symbols=True, uppercase=True)
    my_dict = {'index' : index + 1, 'password' : new_pwd}

    # convert dictionary to pandas data frame
    df_dictionary = pd.DataFrame([my_dict])

    # appending new rows to the dataframe
    passworddf = passworddf._append(my_dict,ignore_index=True)
    

# Set index of the data frame with column title index
passworddf = passworddf.set_index('index')

# Printing the pandas dataframe with index and password
print(tabulate(passworddf, headers='keys', tablefmt='psql'))


