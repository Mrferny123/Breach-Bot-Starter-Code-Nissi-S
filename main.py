#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts years of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook breach")

#Introduces breach
print("Would you like to learn about the Facebook data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Facebook decided not to notify users individually since they believed that the leak did not include financial information, health information, or passwords. Facebook later had to have a 5 billion settlement with the US Federal Trade Commission.")
  
  elif topic.lower() == "b":
    print("They did not notify users about the breach and tried to patch the bug.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triads (b) my reaction, (c) my advice, (d) none")
  topic = input()

  if topic.lower() == "a":
    print("The data breach made the confidential information of the users public. The company should consider adding more measures to encrypt or protect the data so it stays confidential.")

  elif topic.lower() == "b":
    print("We disagree with the organization's response because it is important to know if your data has been compromised so that you can take the appropriate measures to make sure you are safe but Facebook decided not to notify the individuals affected by the breach.")

  elif topic.lower() == "c":
    print("I would convince victims to take action by showing them the dangers people can do with that data.My advice would be to try to change their email address and change passwords and if possible the phone number as well.")
    
  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")


#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")