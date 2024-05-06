# Last updated on 06 May 24

varName=input("Your name:") 
varOrg=input("Origin IATA code:")
varDes=input("Destination IATA code:")
varDate=input("Date in the format DDMMYY:")

print("Booking Confirmed! \nYour PNR is:", varDes[0:2],varDate[1:2],varOrg[0:3],varName[-2:-1] )
print( "Name:", varName.upper() )
print( "Destination:", varDes.upper() )
print( "Date:", varDate.upper() )
