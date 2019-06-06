#SHA256 Bruteforcing Tool

#importing libraries
import hashlib
import argparse

#reads in the encrypted password that you are cracking and cleans it
def read_encrypted_pass(encrypted_pass_file):
	encrypted_pass = open(encrypted_pass_file, "r")
	e_p = encrypted_pass.readlines()
	string_e_p = e_p[0]
	string_e_p = string_e_p.strip()
	return string_e_p

def sha2_384_crack(encrypted_password, password_list):
	print("You have selected to crack a SHA2-384 hashed password")
	print("Press enter to continue: ")
	input()
	counter = 0
	password_list = open(password_list, "r")
	for line in password_list:
		line = line.strip()
		sha_signature = hashlib.sha384(line.encode()).hexdigest()
		counter = counter + 1
		if sha_signature == encrypted_password:
			print("Password succesfully cracked after " + str(counter) + " attempts!")
			print("The password is: " + line)

#compares a sha256 hashed password against a password list
def sha2_256_crack(encrypted_password, password_list):
	print("You have selected to crack a SHA2-256 hashed password")
	print("NOTE: Before trying to bruteforce the password, enter the hash into a site such as hashkiller.co.uk/CRacker/SHA256")
	print("Press enter to continue: ")
	input()
	counter = 0
	password_list = open(password_list, "r")
	for line in password_list:
		line = line.strip()
		sha_signature = hashlib.sha256(line.encode()).hexdigest()
		counter = counter + 1
		if sha_signature == encrypted_password:
			print("Password succesfully cracked after " + str(counter) + " attempts!")
			print("The password is: " + line)

def sha2_224_crack(encrypted_password, password_list):
	print("You have selected to crack a SHA2-224 hashed password")
	print("Press enter to continue: ")
	input()
	counter = 0
	password_list = open(password_list, "r")
	for line in password_list:
		line = line.strip()
		sha_signature = hashlib.sha224(line.encode()).hexdigest()
		counter = counter + 1
		if sha_signature == encrypted_password:
			print("Password succesfully cracked after " + str(counter) + " attempts!")
			print("The password is: " + line)

#compares an md5 hashed passowrd against a password list
def md5_crack(encrypted_password, password_list):
	print("You have selected to crack an MD5 hashed password")
	print("NOTE: Before trying to bruteforce the password, enter the hash into a site such as hashkiller.co.uk/CRacker/MD5")
	print("Press enter to continue: ")
	input()
	counter = 0
	password_list = open(password_list, "r")
	for line in password_list:
		line = line.strip()
		md5_signature = hashlib.md5(line.encode()).hexdigest()
		counter = counter + 1
		if md5_signature == encrypted_password:
			print("Password succesfully cracked after " + str(counter) + " attempts!")
			print("The password is: " + line)

#Takes in filepaths from command line
def parse_in_arguments():
	parser = argparse.ArgumentParser(description = 'Take in the file names', usage="python3 SHA2BF.py [algorithm] [path/to/password_list] [path/to/encrypted_password]")
	parser.add_argument('ea', action="store", type=str, help='what encryption algorithm to use')
	parser.add_argument('pl', action="store", type=str, help='password list file path')
	parser.add_argument('ep', action="store", type=str, help='encrypted password file path')
	args = parser.parse_args()
	return args

#Main code
def main():
	args = parse_in_arguments()
	encrypted_password = read_encrypted_pass(args.ep)
	if args.ea == "sha256":
		sha2_256_crack(encrypted_password, args.pl)
	elif args.ea == "md5":
		md5_crack(encrypted_password, args.pl)
	elif args.ea == "sha224":
		sha2_224_crack(encrypted_password, args.pl)
	elif args.ea == "sha384":
		sha2_384_crack(encrypted_password, args.pl)

		
main()