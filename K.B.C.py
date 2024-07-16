print("enter your name :")
name=input()
print("Good to have you here ",name)
print("lets get started")
print("Here are your question :")
questions = [
    {
        "question": "Who is the current President of India (as of 2024)?",
        "options": ["a) Ram Nath Kovind", "b) Pranab Mukherjee", "c) Droupadi Murmu", "d) A.P.J.         Abdul Kalam"],
        "answer": "c"
    },
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
        "answer": "c"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "b"
    },
    {
      "question": "In which year did India win its first Cricket World Cup?",
      "options": ["a) 1983", "b) 2007", "c) 2011", "d) 1996"],
      "answer": "a"
    },
  {
    "question": "What is the powerhouse of the cell?",
    "options":["a) Nucleus" , "b)Ribosome" , "c)Mitochondria" , "d)Endoplasmic Reticulum"],
    "answer":"c"
  },
  {
  "question": "Which of the following is a play written by William Shakespeare?",
  "options":["a) The Great Gatsby" , "b)Crime and Punishment" , "c)Hamlet" , "d)The Catcher in the Rye "], 
  "answer":"c"
  },
  {
    "question": "Which is the largest continent by area?",
    "options":["a) Africa" , "b)Asia" , "c)Europe" , "d)North America"] ,
    "answer":"b"
  },
  {
    "question": "Which river is the longest in the world?",
    "options":["a) Amazon River" , "b) Nile River" , "c)Yangtze River" , "d)Mississippi River"] ,
    "answer":"b"
  },
  {
    "question": "'War and Peace' is a novel written by which author?",
    "options":["a) Charles Dickens" , "b)Leo Tolstoy" , "c)Mark Twain" , "d) Ernest Hemingway"] ,
    "answer":"b"
  },
  {
    "question": "Who is known as the 'Father of the Nation' in India?",
    "options":["a) Jawaharlal Nehru" , "b)Mahatma Gandhi" , "c)Bhagat Singh" , "d) Subhas Chandra Bose"] ,
    "answer":"b"
  }
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
for i in questions:
  print("\n"+ i["question"])
  #print("\n" i["options"])
  for option in i["options"]:
    print(option)
  user_ans=input("enter your answer :")
  if(user_ans==i["answer"]):
    print("correct")
    if(i==questions[4]):
      money=10000
      print("money :",money)
    elif(i==questions[7]):
      money=80000
      print("money :",money)
    elif(i==questions[9]):
      money=320000
      print("money :",money)
    
  else:
    print("wrong answer")
    break
print("Take your money Rs{money}home :",money)    

