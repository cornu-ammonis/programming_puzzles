# the problem: construct a method which can determine whether a given "ransom note" (here inputted by the user
# as a string, but it could easly be from a word document or web page) can be constructed by 'cutting' words 
# out of a given "magazine" (also given as a string). so each word in the note must appear in the magazine, 
# and if a word appears x times in the note it must also appear x times in the magazine (no re use).

# this is basically a simplified, inflexible version of what plagiarism detectors do. its also worth noting 
# that this program could execute on notes/magazines which are ridiculously long in a fraction of a second.
# its essentially intantaneous, and youd probably have to run it on an entire book before processing time
# becomes perceptible (much less problematic). 
# 

# the algorithm stated abstractly: separate the note into individual words,
#   count the number of times each distinct word apeears, do the same to the magazine, and then 
# check if, for each word in the note (paired with the number of times it occurs), 
# there are at least that many copies of that word in the magazine. 
# if there are the note can be made from the magazine so you return true, if not you return false. 
# the algorithm is pretty simple: the hardest parts are separating the text into words and 
# creating a data structure which makes it easy to pair each word with an integer representing how many 
# times it appears.  python's built in methods make both tasks trivial, as is often the case for 
# text processing. 
#  
#  for the data structure: python makes this super easy with the built in "dictionary" data structure,
# which is formated like so : my_dictionary = { key:value, key2:value2, key3:3 }
# if one executed " a = my_dictionary[key3]", a would equal 3. 
# if one executed my_dictionary[key4] = 4, the key and value would be added to the dictionary. 
# 
# so in this example what we'll do is have one dictionary for the note and one for the magazine.
# each word will be a key, and the key's value will be the # of occurances in the note or magazine respectively. 
# super easy. the entire function takes < 15 lines; in another language like java itd probably be > 30.


# some syntax review so this will make sense even if youre rusty: 
# any line preceded by # is a comment, which means the computer ignores it entirely when executing code.
# methods aka functions take one or more parameters (like x in f(x)) and execute a block of code 
# using those parameters. methods generally execute until they reach a return statement, which passes a value back to
# where you originally 'called' the method. so in this example --  ransom(note, magazine) -- ransom
# is the name of the function, note and magazine are its two parameters, and it returns either true or false.
# so executing these two lines:
# 
# answer = ransom(note, magazine)
# print(answer)

# will  'print' (display) either true or false to the user, assuming that the variables note and magazine 
#  are strings. if they arent, the program will throw an error.


# a colon followed by indenetation on subsequent lines indicates a block of code 
# (many languages do this by surrounding blocks of code with brackets e.g. 
# method(x)  { 
# code here;
# more code;
# return y; } 
# which imo is less visually intuitive and easier to screw up. you'll also notice each line must end with a semicolon,
# which is yet another easily misplaced detail. python is smart enough to detect line endings on its own. )
# 
# 'for loops' execute the same code on multiple different specific values. in this example, we will use a for loop
# to execute a block of code on each word in the note. in python this is as easy as 
 # "for x in y:" or "for word in my_dictionary:". in other lanugages this must be constructed manually, which takes
 # a minute or so to code each time. 
#
# 'if statements' first evaluate whether the condition in parentheses is true, and then execute the subsequent 
# block of code only if it is true. so in the following example, each time we loop an if statement checks if word 
# appears more times in the note than in the magazine: if it does, a line of code executes which changes the value of 
# can_make to false. if the condition is false for each word checked (ie, each word appears at least as many times
# in the magazine) then the subsequent block of code never executes and the value of can_make remains true. 
# 
# side note -- while this is an intuitive way to execute the algorithm, it's arguably a somewhat sloppy design 
# because it means that the program defaults to returning true. if, for whatever reason, something went wrong
# with checking the if condition -- like the program failed provide the number of times a word appears 
# or theres a logic error -- and the block of code under the if statement fails to execute when it should, the 
# function will incorrectly return true. it would perhaps be more thorough -- but certainly *much* more onerous -- 
# to reverse the logic, ie only set the value to "true" once youve verified every word appears in magazine,
# in a sense positively rather than negatiely verifying the result. these sorts of design questions are 
# ubiquitous, there are always multiple ways to solve even a simple problem with respective tradeoffs.




# def signals that we are defining a function
def ransom(magazine, note):

	#the .split() method separates a string into an array of strings based on a delimiter, the default being 
	# a space. this makes it easy to parse sentences into words, but can also be applied to split 
	# text based on other boundaries, like the ends of sentences via punctuation, or new paragraphs.
	mag_words = magazine.split()
	note_words = note.split()
	
	#creates empty dictionaries
	mag_dictionary  = {}
	note_dictionary = {}
	
	#defaults true
	can_make = True

    # the first two loops found below populate the dictionaries; the third loop is basically the entire 
    # algorithm proper, it does the value comparisons. notice how succinct it is. 
	# the names m_word, word, and key in those loops are entirely arbitrary, 
	# so dont be thrown off because i used word in one case and key in the other.
	# .get() is a safer way to pull a value based on a key, because it allows you to specify a default value
	#  if the key doesnt yet exist in the dictionary. 
	# so the first time a word is encountered, .get will return 0 and you add 1. 
	# on subsequent instances of the word, itll pull the current value and then add 1 to it.
	
	for m_word in mag_words:
		mag_dictionary[m_word] = mag_dictionary.get(m_word, 0) + 1

	for word in note_words:
		note_dictionary[word] = note_dictionary.get(word, 0) + 1

	for key in note_words:
		note_word_count = note_dictionary[key]
		# notice i use .get() again, because theres no guarantee a word in the note appears in the magazine at all.
		mag_word_count = mag_dictionary.get(key, 0)
		if (note_word_count > mag_word_count):
			can_make = False

	return can_make

	

mag = raw_input("enter the magazine as a string")

note = raw_input("enter the ransom note as a string")

print(str(ransom(mag, note)))
