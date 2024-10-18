import pandas as pd
import csv
import langdetect
from langdetect import detect

# Specify the path to your CSV file
csv_file_path = 'test_data.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)


data = {
    'UID': [1, 2, 3, 4, 5, 6],
    'TEXT': ["hello,world,foo,bar", " נִיב, נִיב, נִיב", "hola,mundo", "游泳| 散步| 跳舞| 睡觉", "смысл: мочь :рабо́та",
             "خوش آمدید, عصر بخی,  خوبم "]
}

# df = pd.DataFrame(data)

def determine_orientation(text):
    rows = text.split('\n')
    max_commas = 0
    for row in rows:
        max_commas = max(max_commas, row.count(','))
    if max_commas > 1:
        return "Horizontal"
    else:
        return "Vertical"

def has_headers(text):
    sniffer = csv.Sniffer()
    try:
        return sniffer.has_header(text)
    except:
        return False
    
def detect_delimiter(text):
    delimiters = [',', '\t', ';', '|', ':']
    sniffer = csv.Sniffer()
    for delimiter in delimiters:
        try:
            dialect = sniffer.sniff(text, delimiters)
            return dialect.delimiter
        except csv.Error:
            continue
    return "Unknown"

def detect_language(text):
    try:
        return detect(text)
    except:
        return    


df['Language'] = df['TEXT'].apply(detect_language)
df['Delimiter'] = df['TEXT'].apply(detect_delimiter)
df['HasHeaders'] = df['TEXT'].apply(has_headers)
df['Orientation'] = df['TEXT'].apply(determine_orientation)

print(df)
