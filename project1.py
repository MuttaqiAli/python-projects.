
import random

computer=random.choice([1,-1,0])
youstr=input("Enter the choice. r for rock,s for scissor,p for paper: ")
your_dictionary={"s":-1, "r":1, "p":0}
reverse_dictionary={-1:"scissor", 1:"rock", 0:"paper"}
you= your_dictionary[youstr]

print(f"you chosen \"{reverse_dictionary[you]}\" \n computer chosen \"{reverse_dictionary[computer]}\" ")


    
if(computer==you):
      print("it's a draw!")

else:
      ''' low understanding with short and effective technique by observing patterns '''
      if(computer-you==-2 or computer-you==1):
           print("\t you won!")
      elif(computer-you==-1 or computer-you==2):
           print("\t better LUCK next time!")
           '''for better understanding'''    
    #   if(computer==-1 and you==1):
    #     print("\t you won!")
    #   elif(computer==-1 and you==0):
    #     print("\t better LUCK next time!")
    #   elif(computer==1 and you==0):
    #     print("\t you won!")
    #   elif(computer==1 and you==-1):
    #     print("\t better LUCK next time!")
    #   elif(computer==0 and you==1):
    #     print("\t better LUCK next time!")
    #   elif(computer==0 and you==-1):
    #     print("\t you won!")

      else:
        print("somthing went wrong!")