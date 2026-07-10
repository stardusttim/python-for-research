'''
import csv

with open('dataset.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print("Features:", reader.fieldnames) 
    
    for row in reader:
        feature_1 = float(row['feature_1'])
        label = int(row['label'])
'''

'''
import csv

fieldnames = ['epoch', 'loss', 'accuracy']

with open('experiment_log.csv', mode='a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writerow({'epoch': 1, 'loss': 0.456, 'accuracy': 0.85})
'''