import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1 - Create a "placeholder" with the same number of blanks as the chosen_word
#Create an empty String called placeholder.
# For each letter in the chosen_word, add a _ to placeholder.
# So if the chosen_word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2 - Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# Create an empty string called "display".
# Loop through each letter in the chosen_word
# If the letter at that position matches guess then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be _ p p _ _.
# Print display and you should see the guessed letter in the correct position.
# But every letter that is not a match is represented with a "_".

display = ""
for word in chosen_word:
    if word == guess:
        display += word
    else:
        display += "_"
print(display)


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
