passid = input("Please enter your passport code.         \nCode: ")
lpassid = passid.split('<')
numofthings = passid.count('<')

if numofthings<28:
	print('Verification failed. Error code: 281')
elif numofthings>28:
	print('Verification failed. Error code: 282')
lpassid = [lid for lid in passid.split('<') if lid]

if len(lpassid) == 6:
	print(f"TYPE: {lpassid[0][:2]}\nISSUING COUNTRY: {lpassid[0][2:][:3]}\nPASSPORT NO.: {lpassid[4].split(lpassid[0][2:][:3])[0][:len(lpassid[4].split(lpassid[0][2:][:3])[0])-1]}\nLAST NAME: {lpassid[0][5:]}\nGIVEN NAMES: {lpassid[1]} {lpassid[2]} {lpassid[3]}\nNATIONALITY: {lpassid[4][len(lpassid[4].split(lpassid[0][2:][:3])[0]):][:3]}\nDATE OF BIRTH: 20{lpassid[4][len(lpassid[4].split(lpassid[0][2:][:3])[0]):][3:][:2]} {lpassid[4][len(lpassid[4].split(lpassid[0][2:][:3])[0]):][5:][:2]} {lpassid[4][len(lpassid[4].split(lpassid[0][2:][:3])[0]):][7:][:2]}\nDATE OF EXPIRY: 20{lpassid[4][22:24]} {lpassid[4][23:25]} {lpassid[4][25:27]}\nSEX: {lpassid[4][21]}")
elif len(lpassid) == 5:
	print(f"TYPE: {lpassid[0][:2]}\nISSUING COUNTRY: {lpassid[0][2:][:3]}\nPASSPORT NO.: {lpassid[3].split(lpassid[0][2:][:3])[0][:len(lpassid[3].split(lpassid[0][2:][:3])[0])-1]}\nLAST NAME: {lpassid[0][5:]}\nGIVEN NAMES: {lpassid[1]} {lpassid[2]}\nNATIONALITY: {lpassid[3][len(lpassid[3].split(lpassid[0][2:][:3])[0]):][:3]}\nDATE OF BIRTH: 20{lpassid[3][len(lpassid[3].split(lpassid[0][2:][:3])[0]):][3:][:2]} {lpassid[3][len(lpassid[3].split(lpassid[0][2:][:3])[0]):][5:][:2]} {lpassid[3][len(lpassid[3].split(lpassid[0][2:][:3])[0]):][7:][:2]}\nDATE OF EXPIRY: 20{lpassid[3][22:24]} {lpassid[3][23:25]} {lpassid[3][25:27]}\nSEX: {lpassid[3][21]}")
else:
	print(f"Malformed code! Error code: 13{len(lpassid)}")
