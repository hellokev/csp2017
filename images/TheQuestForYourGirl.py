#APCSP
#The Quest for your Girl!
#The Quest
#By Kevin Loi and Haytham Gaber


def introduction():
  print "The Quest for your Girl!"
  print "You are going to marry a princess, but a royal family takes her away to force marry their prince."
  print ""
  part1A()

def part1A():  
  print "Fight back for princess or let them take her for now?"
  print "Type Y to fight or N to let them take her for now" #decisionpoint1
  answer = raw_input()
  if answer == "Y":
   print "You decide to fight back against the armed royal guard and you couldn't take them all on your own. You get arrested and your girlfriend marries the prince."
   print ""
   partRestart()
  else:
   print ""
   print "You decide that in the moment it may be too risky to fight off the Majesty's guard without any back up. So you let them take her at the moment and go home to start planning a way to get her back."
   print ""
   part2()
  
def partRestart():
  print "Type R to restart"
  answer = raw_input()
  if answer == "R":
   introduction()
  
def part2():
  print "So now you are planning, but you are now stressing and you think that planning might take too long and it'll be too late. "
  print "Type P to stay  home and plan a strategy to break in and save her from the prince or Type B to go in blind and rush in." #decisionpoint2
  answer = raw_input()
  if answer == "P":
   print ""
   print "You decide to stay home and plan out a strategy. You think it's best to take an ally with you to help with the rescue."
   print ""
   part3()
  else:
   print "You go in blind, get caught by the royal guards and get arrested, therefore you have to watch the force marriaged."
   partRestart()

def part3():
  print "You remember that you have a friend in the royal guard who owes you a favor, but you don't know if you should ask him because he might be too loyal to his kingdom and his prince."
  print "Type C to contact him to ask for help to get in or Type L to not." #decisionpoint3
  print ""
  answer = raw_input()
  if answer == "C":
    print ""
    print "You have contacted him and he says he'll help. He tells you a secret underground tunnel that leads to the Marriage Hall where you can intercept and stop the wedding."
    print""
    part4()
  else:
    print "You decide you can't trust your friend and instead, you go alone and get caught by the royal guards and the marriage continues."
    partRestart()
    
def part4():
  print "You take your friend's advice and you go through the underground tunnel. But you come across a problem, there is two guards guarding the passage to the Marriage Hall. There are armed but you figured you came so far and don't want to give up."
  print "Type Y to take them on with your ally or Type N to try to sneak pass them." #decisionpoint4
  print ""
  answer = raw_input()
  if answer == "Y":
    print ""
    print "With a string of luck, you were able to take down both guards without getting caught and you proceed to enter the Marriage Hall."
    print ""
    part5()
  else:
    print "You try to sneak pass them, but you get caught and now you have to watch the force marriage."
    partRestart()

def part5():
  print "You have made it in Marriage Hall. The prince and your girlfriend are about to get married. The prince spots you and you guys seem like you are about to fight. You noticed your girlfriend and she looks surprised to see you. You remember you had the ring in your pocket from when you first wanted to propose to her. You are thinking of whether to propose to her right now or fight the prince."
  print ""
  print "Type P to propose or F to fight along with your ally."
  answer = raw_input()
  if answer == "P":
    print "The prince had time to call his guards and then he steals your ring. You are now captured by the guards and have to watch the marriage happen."
    partRestart()
  else:
    print ""
    print "You have defeated the prince in the fight! You take her back to your city and you propose to her afterwards."
    print ""
    print "Thank you for playing this story!"
    partRestart()
introduction()