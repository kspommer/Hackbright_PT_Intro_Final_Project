## Final Project for Hackbright Academy
## Part-Time Introduction to Python Workshop
## Susan Pommer
## December 2016
## Question File
## See Program Spec for Details
################################

import csv

def get_question(option, count):
	
	with open('questionandanswer.csv') as csvfile: 
		reader = csv.DictReader(csvfile)

		selected_option = option 
		str_question_number = str(count)
		question_number = count 

		for row in reader:
			if (row['topic'] == selected_option and row['question_num'] == str_question_number):
				if 	question_number==1: 
					print("Here is your first question:")
					print(" ")
				else: 
					print("Here is your next question:")
					print(" ")
				print(row['question'])
				print("1: ", row['answer1'])
				print("2: ", row['answer2'])
				print("3: ", row['answer3'])
			