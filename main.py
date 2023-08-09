'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')

# online Quiz game

options=[["(A) Pura","(B) Sawa","(C) Adha","(D) Pauna"],
        ["(A) Agni","(B) Indra","(C) Hanuman","(D) Ganesha "], 
        ["(A) One","(B) Two","(C) Three","(D) Four"],
        ["(A) Krishna and Kanhaiya","(B) Kanha and Madhav","(C) Ghanshyam and Murari","(D) Girdhar and Gopal"],
        ["(A) Brazil","(B) India","(C) Russia","(D) China"],
        ["(A) P.B. Shelley","(B) Alfred Tennyson","(C) W.B. Yeats","(D) T.S. Elliot"],
        ["(A) Anandiben Patel","(B) Vasundhara Raje Scindia","(C) Uma Bharti","(D) Mamata Banerjee"],
        ["(A) K.D.Jadav","(B) Dhyan Chand","(C) Prakash Padukone","(D) Milkha Singh"],
        ["(A) CM of Gujarat","(B) Took oath as","(C) Joined BJP","(D) Became RSS Pracharak"],
        ["(A) Dirghaayu","(B) Suhagan","(C) Chiranjeevi","(D) Sushil"]] 
questions=["MCQ.1 Which of the following corresponds to ‘ek bataa do’?","MCQ.2 Which of the following gods is also known as ‘Gauri Nandan’?","MCQ.3 In the game of ludo the discs or tokens are of how many colours?","MCQ.4 Which of these are names of national parks located in Madhya Pradesh?","MCQ.5 Where was the BRICS summit held in 2014?","MCQ.6 Who wrote the introduction to the English translation of Rabindranath Tagore’s Gitanjali?","MCQ.7 Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving two girls from drowning?","MCQ.8 The wife of which of these famous sports persons was once captain of Indian volleyball team?","MCQ.9 Starting with the earliest, arrange the following events in Narendra Modi’s life in chronological order. FFF (Fastest Finger First)","MCQ.10 Which of these terms can only be used for women?"]
ans=["C","D","D","B","A","C","A","D","D","B"]

print("Welcome to Quiz")
marks=0

for index,question in  enumerate(questions,start=0):
    print(question)
    print(options[index])
    Ans=input("Please select the correct option : ")
    if(Ans.capitalize()==ans[index]):
        marks=marks+1

print("congratulations quiz is complete !")

print(f"Your score is out of 10 is :{marks} ")

if(marks<3):
    print("you should work to hard")
if(marks>=3 and marks<=5):
    print("Good Work")
if(marks>=5 and marks<=10):
    print("Excellent!")
    



        
        
        