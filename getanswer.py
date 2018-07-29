## Final Project for Hackbright Academy
## Part-Time Introduction to Python Workshop
## Susan Pommer
## December 2016
## Get Answers Program
## See Program Spec for Details
################################

def check_answer(selected_topic, questioncount, selected_answer):
	import csv

	with open('questionandanswer.csv') as csvfile: 
		reader = csv.DictReader(csvfile)
		question_number = str(questioncount)

		for row in reader:	
			if (row['topic'] == selected_topic and row['question_num'] == question_number):
				while(True):
					if (bool(row[selected_answer]) == False): 
						print(" ")
						print("Sorry, that's the wrong answer.")
						selected_answer = input("Select another answer: ")
					else:
						break		

				if (bool(row[selected_answer]) == True): 
					print(" ")
					print("Yeah!  That's the correct answer!")
					questioncounter = questioncount + 1
					return questioncounter
					

def get_answer(selected_topic, questioncount):
	print(" ")
	selected_answer = input("Enter the correct answer for this question:  ")

	while(True):
		if selected_answer < '1' or selected_answer > '3':
			print(" ")
			print("Sorry, that's not a valid answer.")
			selected_answer = input("Select another answer: ")
		else: 
			break

	if selected_topic >= '1' and selected_answer <= '3':		
			questioncounter = check_answer(selected_topic, questioncount, selected_answer)
			return questioncounter	