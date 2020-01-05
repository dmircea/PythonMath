# 	This program was created by Mircea Dumitrache. ILA and student at California State University, Fullerton.
#	This program is a simplistic calculator that performs operations on a user defined list.
#	The operations range from a simple average to finding the quartiles.
#	Please see the README file for more information on its current or planned functionalities.

import helperFunct as helper

def main():
	print('Entering main function')
	arrayX = []

	print('Entering main while loop')
	while(True):
		print('Choose an option:')
		print('1. See the array.')
		print('2. Add a number to the array')
		print('3. Take the average of the array.')
		print('4. Find the mode of the array.')
		print('5. Find the range of the array.')
		print('6. Find the median of the array.')
		print('7. Find the 1st and 3rd quartile.')
		print('8. Delete a number from the array. (All duplicates are deleted as well)')
		print('9. Add several numbers to the array')
		print('20. Exit the program.')

		choice = int(input('Your choice: '))

		print(choice)
		if(choice == 20):
			#	Choice to exit the program.
			break

		elif(choice == 1):
			#	Choice to see the current number of the array.
			print(arrayX)

		elif(choice == 2):
			#	Choice to add a number to the array.
			arrayX.append(getNum())

		elif(choice == 3):
			#	Choice to find the average of the array and print it to screen
			print("The average of the array is: " + str(getAverage(arrayX)))

		elif(choice == 4):
			#	Choice to find the mode of the array and print it to screen
			print("The mode of the array is: " + str(getMode(arrayX)))

		elif(choice == 5):
			#	Choice to find the range of the array and print it to screen
			max = getMax(arrayX)
			min = getMin(arrayX)
			print("The range of the array is: " + str(max - min))

		elif(choice == 6):
			#	Choice to find the median of the array
			print("The median of the array is: " + str(getMedian(arrayX)))

		elif(choice == 7):
			#	Choice to find the first and third quartile and print them to the screen
			print("The first quartile is: " + str(getFirstQrt(arrayX)))
			print("THe third quartile is: " + str(getThridQrt(arrayX)))

		elif(choice == 8):
			#	Choice to the delete a number from the array
			number = getNum()
			while (number in arrayX):
				arrayX.remove(number)

		elif(choice == 9):
			#	Choice to add several numbers to the array
			raw = input('Type all number separated by a space: ')

			newNumbers = [int(num) for num in raw.split(' ')]

			#	Extend list
			arrayX.extend(newNumbers)

	#	End of conditionals
	print('Thank you for using this program! Goodbye!')

#	This is the function used for choice number 2
def getNum():
	num = int(input('Choose a number: '))
	return num

#	This is the function used for choice number 3
def getAverage(arr):
	sum = 0
	for i in arr:
		sum += i

	return sum / len(arr)

#	This is the function used for choice number 4
def getMode(arr):
	msFrq = 0
	msFrqNum = 0
	modeDict = {}
	for i in arr:
		if(i not in modeDict):
			modeDict[i] = 0
		modeDict[i]+= 1

	for key in modeDict:
		if(modeDict[key] > msFrq):
			msFrq = modeDict[key]
			msFrqNum = key

	return msFrqNum

#	Those are the functions used to find the range for choice number 5
def getMax(arr):
	max = float('-inf')
	for i in arr:
		if(i > max):
			max = i

	return max

def getMin(arr):
	min = float('inf')
	for i in arr:
		if(i < min):
			min = i

	return min

#	This function will be used to find the median of the array
def getMedian(arr):
	helper.simpleSort(arr)
	if(len(arr) % 2 == 0):	#	The size of array is even
		#	take half of the length and use it as the index of the array.
		#	take half of the lenght minus one and use it as the index for
		#	the other number. return the average of the two numbers
		return (arr[int((len(arr) / 2))] + arr[int((len(arr) / 2 - 1))]) / 2
	else:					#	The size of array is odd.
		return arr[int(len(arr) / 2)]

#	This function will be used to find the 1st quartile
def getFirstQrt(arr):
	helper.simpleSort(arr)
	newArray = arr[:int(len(arr) / 2)]
	print("First quartile array: " + str(newArray))
	return getMedian(newArray)

#	This function will be used to find the 3rd quartile
def getThridQrt(arr):
	helper.simpleSort(arr)
	if(len(arr) % 2 == 0):
		newArray = arr[int(len(arr) / 2):]
	else:
		newArray = arr[int(len(arr) / 2) +1:]
	print("Third quartile array: " + str(newArray))
	return getMedian(newArray)


#	Main function is called here
if(__name__ == '__main__'):
	main()
