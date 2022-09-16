### Author: Bryan Le
### Course: CSc 110
### Description: A program that takes an input of a file name and then encrypts the contents of
### whatever is inside with the random module.
import random
def encrypter():
    '''
    This function will ask for the input file then it'll loop through the file
    and append the index of the line and actual contents of the line to two empty lists that are
    respectively named. Then after it'll randomize the order of the lists with the random
    integers (set from 0 to the length of index list) for the amount of the length of the index
    list multiplied by 5. After that the function will open 2 files respective to the list they
    belong to and write the new randomized information there and then close the files.
    '''
    encrypting_question = str(input("Enter a name of a text file to encrypt: \n"))
    open_file = open(encrypting_question, 'r')
    index_list = []
    encryption_list = []
    i = -1
    for line in open_file:
        i += 1
        index_list.append(i+1)
        encryption_list.append(line)
    t = 0
    while t < len(index_list) * 5:
        rand_int = random.randint(0, i)
        rand_int_2 = random.randint(0, i)
        index_list[rand_int], index_list[rand_int_2] = index_list[rand_int_2], index_list[rand_int]
        encryption_list[rand_int], encryption_list[rand_int_2] = encryption_list[rand_int_2], \
                                                                 encryption_list[rand_int]
        t += 1

    open_encrypted_file = open("encrypted.txt",'w')
    for encrypted_lines in encryption_list:
        open_encrypted_file.write(str(encrypted_lines))
    open_encrypted_file.close()

    open_index_file = open("index.txt",'w')
    for indexes in index_list:
        open_index_file.write(str(indexes)+'\n')
    open_index_file.close()

def main():
    random.seed(125)
    encrypter()

main()
