import csv
from collections import Counter 


dest_ip = dict()

with open('sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if (row[7].find('[SYN]') != -1):
                ip_key = row[3]
                if ip_key in dest_ip.keys():
                    dest_ip[ip_key] += 1
                else:
                    dest_ip[ip_key] = 1
            line_count += 1

count_ip = Counter(dest_ip)
most_visited = count_ip.most_common(3)
for i in most_visited:
    print(i[0]," : ",i[1])
