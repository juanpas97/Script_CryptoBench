import re
import numpy as np



with open('Special_test_tupnz.txt') as f:
    list_agreement = []
    list_decrypt = []
    list_key = []
    times = []

    for line in f:
        if "Time to generate hash:" in line:
            list_agreement.extend(re.findall(r'\d+',line))

mean_array_hash = np.array(list_agreement).astype(np.float)
mean_hash = np.mean(mean_array_hash)

print ("Time generating key agreements:")
print(np.sum(mean_array_hash))

print ("Mean generating hash:")
print (mean_hash)
print ("Standard deviation of hashinh:")
print (np.std(mean_array_hash))
print ("Fastest time hashing:")
print (np.amin(mean_array_hash))
print ("Slowest time hashing:")
print (np.amax(mean_array_hash))

print ("")
