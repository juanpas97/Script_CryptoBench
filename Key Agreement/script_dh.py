import re
import numpy as np



with open('Special_test_n5mlo.txt') as f:
    list_agreement = []
    list_decrypt = []
    list_key = []
    times = []

    for line in f:
        if "Time for key agreement:" in line:
            list_agreement.extend(re.findall(r'\d+',line))

        elif "Time to set key:" in line:
            list_key.extend(re.findall(r'\d+',line))

mean_array_agree = np.array(list_agreement).astype(np.float)
mean_agree = np.mean(mean_array_agree)

print ("Time generating key agreements:")
print(np.sum(mean_array_agree))

print ("Mean generating key agreement:")
print (mean_agree)
print ("Standard deviation of key agreement:")
print (np.std(mean_array_agree))
print ("Fastest time generating key agreement:")
print (np.amin(mean_array_agree))
print ("Slowest time generating key agreement:")
print (np.amax(mean_array_agree))

print ("")


mean_array_key = np.array(list_key).astype(np.float)
mean_key = np.mean(mean_array_key)

print ("Time setting key:")
print(np.sum(mean_array_key))

print ("Mean setting key:")
print (mean_key)

print ("Standard deviation of setting key:")
print (np.std(mean_array_key))

print ("Fastest time setting key:")
print (np.amin(mean_array_key))

print ("Slowest time setting key:")
print (np.amax(mean_array_key))

print ("")
