import re
import numpy as np



with open('Special_test_ttpva.txt') as f:
    list_encrypt = []
    list_decrypt = []
    list_key = []
    times = []

    for line in f:
        if "Time to encrypt:" in line:
            list_encrypt.extend(re.findall(r'\d+',line))
        elif "Time to decrypt:" in line:
            list_decrypt.extend(re.findall(r'\d+',line))
        elif "Time to set key:" in line:
            list_key.extend(re.findall(r'\d+',line))


mean_array_enc = np.array(list_encrypt).astype(np.float)
mean_encrypt = np.mean(mean_array_enc)

print ("Time encrypting:")
print(np.sum(mean_array_enc))

print ("Mean encrypt:")
print (mean_encrypt)
print ("Standard deviation of encrypting:")
print (np.std(mean_array_enc))
print ("Fastest time encrypting:")
print (np.amin(mean_array_enc))
print ("Slowest time encrypting:")
print (np.amax(mean_array_enc))

print ("")


mean_array_dec = np.array(list_decrypt).astype(np.float)
mean_decrypt = np.mean(mean_array_dec)

print ("Time decrypting:")
print(np.sum(mean_array_dec))
print ("Mean decrypt:")
print (mean_decrypt)
print ("Standard deviation of decrypting:")
print (np.std(mean_array_dec))
print ("Fastest time decrypting:")
print (np.amin(mean_array_dec))

print ("Slowest time decrypting:")
print (np.amax(mean_array_dec))

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
