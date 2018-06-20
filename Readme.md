## Scripts for CryptoBench

This scripts are prepared to work together with [CryptoBench](https://github.com/juanpas97/CryptoBench) as an easy way to analyze the results of the different tests.

### How to use

As you can see, there are different folders that contain a different script for the different algorithms.
* AES: This script analyzes AES-CBC, AES-OFB, AES-CTR, AES-GCM.
* Key Agreement: This script analyzes DH and ECDH
* Hash: This script analyzes MD-5
* RSA: This script analyzes RSA

There is an example of result in every folder to test that everything works. If you decide to change the sample to analyze, just open the script and in the line

```
with open('Special_test_ttpva.txt') as f:
```
and change the name of the .txt