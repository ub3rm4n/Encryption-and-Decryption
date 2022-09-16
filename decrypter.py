### Author: Bryan Le
### Course: CSc 110
### Description: A program that takes an input of a file name and then decrypts the contents of
### whatever is inside.
def decrypter():
    '''
    This function will ask for the encrypted text and index file you created from encrypter.py
    Then it will read and append the stuff from those files to two empty lists. After which,
    a new list equivalent to the length of the index list is created and then the indexes of the
    randomized content are restored to their original position through a loop. Then it'll write the
    new file for the original content and close out of it.
    '''
    encrypted_text_file = str(input("Enter the name of an encrypted text file: \n"))
    encryption_index_file = str(input("Enter the name of the encryption index file: \n"))
    encrypted_list = []
    index_list = []

    open_encrypted_file = open(encrypted_text_file, 'r')
    for line in open_encrypted_file:
        encrypted_list.append(line)

    open_index_file = open(encryption_index_file,'r')
    for indexes in open_index_file:
        index_list.append(indexes)

    original_list = [' '] * len(encrypted_list)
    i= 0
    while i < len(index_list):
        num = int(index_list[i]) - 1
        original_list[num]=encrypted_list[i]
        i+=1

    open_decrypted_file = open('decrypted.txt','w')
    for lines in original_list:
        open_decrypted_file.write(str(lines))
    open_decrypted_file.close()

def main():
    decrypter()

main()