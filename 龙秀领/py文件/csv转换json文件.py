import csv
import json

csv_file_path = '../top/网站排行.csv'
json_file_path = '网站排行.json'

# 读取CSV文件并将数据存储在列表中
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# 写入JSON文件
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(rows, jsonfile, ensure_ascii=False)