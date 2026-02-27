# Introduction

I will be creating a programme which will be a quiz for the different SME’s, Tech Sellers, and Sellers in my business unit at my organisation. The quiz will consist of 5 questions and be in the form of asking who the Seller/SME/Tech Seller for a specific area of products within my team is. Once each question has been answered, you are able to see if you got it correct or incorrect, if the answer you submit is incorrect, it will give you the right answer. Once you have answered all 5 of the questions, you will get a score at the end, and you will then be able to save the results to a text file so you can review your quiz attempt and the answers you gave to further improve your knowledge and correct any wrongdoings.

This will be beneficial for my team as they need to be able to quickly identify the relevant people within the desired sector when working on deals with clients or pushing new initiatives. For example, if I were selling a database product and I needed information quickly on the limitations of a certain product, it would be beneficial for me to know who to reach out to so I could get a swift result. Use cases for it within the team could consist of new starters to the team who would like to learn their colleagues’ roles, and standing members of the team who want to refresh their memory or relearn after a shuffle in roles.

# Design Section

## GUI

GUIDIAGRAM

## Functional Requirements

*   The programme must load the staff information from the CSV, and turn each row into a ‘Person’ object containing domain, name, and role.
*   The programme has to allow the user to start the quiz by pressing the ‘Start Quiz’ button that must appear when the user starts the programme.
*   The programme needs to generate questions by selecting a random person, and creating a question based on their job role and area of the business.
*   The programme needs to compare the users input for the answer with the persons job role and validate it.
*   The programme needs to save the results for that quiz attempt by writing it to a text file.

## Non-functional requirements

*   The GUI needs to be simple and easy to understand for all the users.
*   The programme must be responsive and respond without any delays or errors.
*   The code must be easy to read and clearly set out with classes and functions to ensure that it can be maintained.
*   The programme should run on any computer with Python 3.9 or above and TKInter installed.

## Tech Stack Outline

Python 3 was the programming language that I will use for this programme, this is because it has built in support for a GUI with TKinter and for file handling which are two features I will be using throughout the quiz programme. I will be using the PyCharm IDE for this programme to write the code and run it.

As mentioned, I will be using TKInter to buld the GUI, it allows me to make windows, buttons, labels, and text boxes. Additionally, I will be using CSV to read the csv file containing the individual’s names for the quiz. Random will be used for random selection and creation of quiz questions.

I will be storing the staff information in a CSV file, with reach row containing a domain, name, and role. This allows for easy alteration in the need of business changes. Additionally, users can save their quiz attempt, which will also be stored in a separate CSV.

## Class Diagram

CLASSDIAGRAM

# Testing / Development

## Bringing data from CSV to Programme

I started this programme by writing the data from my CSV file ‘business\_unit\_names.csv’ which contains the relevant individuals and roles for the quiz.

To test that this is working correctly, I will be printing the list ‘People’ which is created from the ‘read\_csv’ function, and I expect for it to show me the domain ‘Person’ followed by all of the individual’s names, areas, and roles from the CSV. This will show that the data has been exported from the CSV correctly, and that this data can be inputted into the quiz. Additionally, I added two checks, one for the role and one for the name. This is to ensure that these functions return the correct True and False values, demonstrating working input validation.

TEST1

TEST2

| Description | Expected Output | Actual Output | Result |
| --- | --- | --- | --- |
| Load CSV | List of people | Correct list printed | Pass |
| Validate role | True | True | Pass |
| Validate role | False | False | Pass |
| Validate name | True | True | Pass |
| Validate name | False | False | Pass |

This was a successful test as all the outputs are as expected. I used a mix of both manual testing which confirmed that the CSV file was loaded in correctly and that the list objects matched that data. Unit style testing was used for the functions to confirm the outputs.

## Quiz logic

I next moved onto the logic of the quiz, which includes selecting a random person from the list and generating a question based on the role and domain. This also validates if the user’s answer is correct or not.

To test that this is working correctly, I have started by ensuring my function for picking a random person works by calling it and printing the result. I then did the same for the ‘making\_question’ function. Additionally, I completed answer checks in which I ensured that it returned True for a correct name and False for an incorrect name.

For this test, I have used unit-testing as I can test all aspects of the quiz logic in isolation, allowing for swift verification that they are working before I implement it into the full programme.

TEST3

TEST4

| Description | Expected Output | Actual Output | Result |
| --- | --- | --- | --- |
| Random person selection | Returns a person's name, area, and role | Returned a person's name, area, and role | Pass |
| Question generation | Generating a question | Generated a question | Pass |
| Correct answer check | True | True | Pass |
| Incorrect answer check | False | False | Pass |

## Exporting and saving results

After completing the quiz, users are given the option to save the results. This is done by clicking the save results button on the GUI at the end of the quiz and should result with the results being exported to the ‘results.txt’ file that is generated. For this I will be using manual testing as it involves user interaction with clicking the button, feedback from the GUI, and file content verification. A successful test will result in the answers from that attempt being inserted into the text file.

TEST5

TEST6

TEST7

This was a successful test showing that the GUI responds correctly, the file writing system works correctly, and that the user is seeing the confirmation message on the screen.

# Documentation

## User documentation

### Starting the quiz

After you press start, a question will appear at the top of the window. It will ask who the correct person is for a business unit or role. You can type your answer into the white box below the question by clicking inside the box and typing the answer. When you are ready, click the submit answer button and the programme will review your answer and show you if you are right or wrong. You can then move onto the next question, repeating the same steps.

### Feedback messages

When you have submitted your answer, you can look at the bottom of the screen to see if the answer to the quiz is correct or not. If the answer is correct, the message ‘Correct’ will appear. Else it will say ‘Wrong, the correct answer was \[Correct Answer\]’. This will help you learn the correct information.

### Saving your results

When you have finished the quiz, you are able to save your answers to a file by clicking the ‘Save Results’ button. A message will appear saying ‘Results saved!’. A file called ‘results.txt’ will then be created in the same folder as the quiz, and will contain the questions you were asked, the answers you submitted, and if the answer was correct or incorrect. This is beneficial for your training and record keeping.

## Technical documentation

### How the code works

This quiz programme was written in Python and uses several different libraries to help it execute.

1.  TKInter is used for the GUI
2.  CSV is for reading the data from the business unit names CSV file
3.  Random is used for picking questions

A class called ‘Person’ is used to store everyone’s details. Each row from the CSV is turned into a ‘Person’ object.

### How the programme starts

At the bottom of the code we have two lines which start the programme.

1.  People = read\_csv(filepath)

This line of code loads the CSV into a list we have created called ‘people’

1.  QuizGUI(people)

This line of code is what starts the GUI, you can see we have passed our ‘people’ list into it. This GUI controls the quiz.

### GUI

The GUI for the quiz programme is built inside a class called ‘QuizGUI’. Inside this class, all the elements of the GUI are created. This consists of:

*   The window the quiz runs in
*   The question label
*   The answer box
*   The start, submit, and save results button
*   The feedback label, which displays correct or incorrect and the correct answer.

When the user clicks on the ‘Start Quiz’ button, the GUI picks a random person and creates a question, it is then shown on the top of the screen.

When the user clicks the ‘Submit Answer’ button, the GUI checks the users answer from the answer box text field with the correct data from the list, shows the feedback such as if it correct or incorrect, adds the results to the results list, and then moves onto the next question. After the 5 questions have been answered, the GUI shows the final score.

### Saving the users results

The save button calls the ‘save\_results’ function calling both the text file ‘results.txt’ and the results from the GUI. This will write each result into the text file, each time the user saves it, it overwrites the file, meaning only the latest quiz attempt is saved.

### Testing the programme

You can test the programme in two ways, depending on what functions you want to test.

Manual testing can be used when testing GUI behaviour, feedback messages, and saving results. To test manually please follow these steps:

1.  Run the programme
2.  Click through the quiz
3.  Check that each part behaves as expected
4.  Open the ‘results.txt’ to ensure the file contents are correct

Unit style testing can be used when testing the logic functions. To do this, it is first important to disable the GUI by following these steps:

1.  Delete the line of code ‘QuizGUI(people)’

You can then call upon the function and see the result in the console by following this layout:

print(\[Function(\[Input\]))

This will confirm if the logic is correct or not by outputting the result, you can compare this with the expected output.

### Classes and Functions explained

| Component Type | Name | Responsibility |
| --- | --- | --- |
| Class | Person | Stores the domain, name, and role of individuals in the quiz |
| Class | QuizGUI | Handles the GUI, question flow, scoring, and saving |
| Function | Read_csv | Loads the data from the CSV into the program |
| Function | Pick_random_person | Selects a random person from the list |
| Function | Make_question | Creates the quiz question |
| Function | Check_answer | Validates the user’s answer |
| Function | Save_results | Writes the user’s results to the text file |

# Evaluation section

The quiz programme works well and meets all the aims I set out for myself at the [start of the project](#_Introduction). It [loads data from the CSV file](#_Bringing_data_from), shows questions clearly, [checks the users answer, gives the user feedback](#_Quiz_logic), and [saves the users results to a text file](#_Exporting_and_saving). This has resulted in a simple and easy-to-use programme, with an easy-to-understand and intuitive interface.

I found the use of object-oriented programming in Python a good learning experience for myself. I have previously mainly used C# as a programming language and rarely used Python aside from basic procedural programming. This has allowed me to understand more about the language and will enable me to further develop my skills on a new language, while using previous knowledge.

I believe I could have improved the programme by allowing for multiple results text files to be created as [opposed to the file being overwritten](#_User_documentation), allowing for multiple quiz attempts to be saved. Additionally, I believe I could have added functionality for the quiz by allowing the users to see the individual results in the programme as opposed to having to read the text file, which would have improved the user experience and helped with learning and retention of the quiz content.

Overall, the project is successful and [meets all the needs I set out at the beginning](#_Functional_Requirements), and has provided me with good knowledge for future development in which I can add some of these features.
