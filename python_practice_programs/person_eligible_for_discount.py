Rajdhani_ticket=1000
New_Ticket_Price=None

a=int(input("Enter the age of the client:"))

if (a>60):
        print("The Client is eligible for the senior citizen discount")
        New_Ticket_Price=(Rajdhani_ticket) - (Rajdhani_ticket *10/100)
        print("New Price for Rajdhani_Ticket for the client : " +str(New_Ticket_Price))
else:
    print("The client is not eligible for senior citizen discount")
    



