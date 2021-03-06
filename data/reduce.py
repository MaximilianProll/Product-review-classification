num_reviews = 222240 # Number of reviews per category
final_out_fn = 'deskewed_shuffled_dataset.json'

import random

entries = []
new_line_char = '\n'

for i in range(5):
    dataset_i = 'dataset' + str(i) + '.json'
    num_recorded = 0
    file_handler = open(dataset_i).readlines()
    random.shuffle(file_handler)

    for line in file_handler:
        if line[-1] == new_line_char:
            line = line[:-1]
        entries.append(line)
        num_recorded += 1
        if num_recorded == num_reviews:
            break

random.shuffle(entries)

out = open(final_out_fn, 'a')
for entry in entries:
    out.write(entry + new_line_char)
out.close()
