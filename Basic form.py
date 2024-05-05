varName=input("Your name:") 
varOrg=input("Origin IATA code:")
varDes=input("Destination IATA code:")
varDate=input("Date in the format DDMMYY:")

print("Ticket Confirmed! \nYour PNR is:", varDes[0:2],varDate[1:2],varOrg[0:3],varName[-2:-1] )