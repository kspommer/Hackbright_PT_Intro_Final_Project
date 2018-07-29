## Final Project for Hackbright Academy
## Part-Time Introduction to Python Workshop
## Susan Pommer
## December 2016
## See Program Spec for Details
################################

from getquestion import get_question
from getanswer import get_answer

def menu():
	print("1:  General Python Questions")
	print("2:  Git and Github")
	print("3:  Lists")
	print("4:  Loops & Functions")
	print("5:  Tuples and Dictionaries")
	
def menu_selection():
	menu()
	print(" ")
	selected_topic = input("Which of those topics would you like to review? (1-5 or exit): ")
	return selected_topic

def call_questions(selected_topic, questioncount):
	while(True):
		if selected_topic == "exit":
			exit()	
		elif selected_topic < '1' or selected_topic > '5':
			print("Sorry, that's not a valid option.")
			print(" ")
			selected_topic = menu_selection()
		elif selected_topic >= '1' and selected_topic <= '5':
			questioncount = topic_logic(selected_topic, questioncount)
			if questioncount ==7: 
				break

def topic_logic(selected_topic,questioncount):
	while(True):
		if questioncount >=1 and questioncount <=5:
			print(" ")
			get_question(selected_topic, questioncount)
			questioncount = get_answer(selected_topic, questioncount)
		elif questioncount == 6: 
			print(" ")
			print("Woo-hoo! You completed that quiz!")
			questioncount = 7
			return questioncount
	
def to_go_on():
	print (" ")
	go_on = input("Do you want to take another quiz? (Y/N): ").lower()
	return go_on

def new_quiz(go_on):       
	selected_topic = menu_selection()
	questioncount = 1
	call_questions(selected_topic, questioncount)
	go_on = to_go_on()
	while(True):
		if go_on == 'y':
			new_quiz(go_on)
		else:
			exit()


def main():
	print(" ")
	print("Welcome to the Python Quiz!")
	print("You will be presented 5 questions on the topic of your choice.")
	print(" ")

	selected_topic = menu_selection()
	questioncount = 1

	call_questions(selected_topic, questioncount)
		
	go_on = to_go_on()

	while(True):
		if go_on == 'y':
			new_quiz(go_on)
		else:
			exit()

if __name__ == '__main__':
	main()
