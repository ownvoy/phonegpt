import os
import openai
from termcolor import colored
import argparse
parser = argparse.ArgumentParser()
# parser.add_argument('-q')

path = os.getcwd()
import sys
print(sys.argv[2:])
file_path = f'{path}/api.txt'

if os.path.exists(file_path):


    file = open(file_path,'r')
    data = file.read()
    openai.api_key = data
    file.close()
    args=sys.argv[2:]
    # args = parser.parse_args()
    prompt = ' '.join(args)
    print(prompt)

    response = openai.Completion.create(
    engine='text-davinci-003',  # Use 'text-davinci-003' for gpt-3.5-turbo model
    prompt=prompt,
    max_tokens= 500 )
    # generated_text = response.choices[0].text.strip()
    print(response["choices"][0])
    results = response["choices"][0].text.strip()
    print('￦n')
    print('______________________')
    
    # print(generated_text)
    
    with open("result.txt","w") as file:
        file.write(results)




else:
    with open("api.txt","w") as file:
        file.write(input("Enter your api key: "))

    file.close()

