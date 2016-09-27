import serial
import csv
import matplotlib
print serial.VERSION
ser = serial.Serial('/dev/ttyACM0', 9600,timeout = 5)
data =''

with open('data.csv','wb') as csvfile:
	datawriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
	while ser.readline():
		packet=ser.readline()
		packet = packet[:-2].split(',')
		print packet
		datawriter.writerow(packet)

print "finished"

with open('data.csv','rb') as csvfile:
	datareader = csv.reader(csvfile,delimiter=',')
	for row in datareader:
		print row

