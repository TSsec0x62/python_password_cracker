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

#compares the encrypted password against a password list
def compare_to_passlist(encrypted_password, password_list):
	counter = 0
	password_list = open(password_list, "r")
	for line in password_list:
		line = line.strip()
		sha_signature = hashlib.sha256(line.encode()).hexdigest()
		counter = counter + 1
		if sha_signature == encrypted_password:
			print("Password succesfully cracked after " + str(counter) + " attempts!")
			print("The password is: " + line)

#Takes in filepaths from command line
def parse_in_arguments():
	parser = argparse.ArgumentParser(description = 'Take in the file names', usage="python3 SHA2BF.py [path/to/password_list] [path/to/encrypted_password]")
	parser.add_argument('pl', action="store", type=str, help='password list file path')
	parser.add_argument('ep', action="store", type=str, help='encrypted password file path')
	args = parser.parse_args()
	return args

#Main code
def main():
	args = parse_in_arguments()
	encrypted_password = read_encrypted_pass(args.ep)
	compare_to_passlist(encrypted_password, args.pl)

main()