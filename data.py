## Find Delimiter 
import csv

def get_delimiter(file_path: str) -> str:
    with open(file_path, 'r') as csvfile:
        delimiter = str(csv.Sniffer().sniff(csvfile.read()).delimiter)
        return delimiter

get_delimiter(downloaded_file_1)
