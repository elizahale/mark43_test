from flask import render_template, flash, redirect
from app import app
from .forms import TextForm

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Mark 43 Team'}  # fake user
    return render_template("index.html",
                           title='Home',
                           user=user,
                           )

# for this function I have decided to ignore numericals, such as '2' or '10,000' because they are not words, per say.
# I am also not counting hyphens or apostraphes as part of the length of the word, I am only counting letters.
def average_word_length(text=None):
    if text == None:
        avg_len = 0
    elif type(text) != str:
        avg_len = 0
    else:
        # split the text into a list, split at each whitespace char
        raw_words = text.split()
        # remove all words that are not purely letters
        words = [word for word in raw_words if word.isalpha()]
        
        # for words with non-letter characters ('-', '\', etc.) remove the non-letter characters
        # add these new words to list
        for word in raw_words:
            if not word.isalpha():
                new_word = ''
                for char in word:
                    if char.isalpha(): new_word += char
                if (len(new_word) >= 1):words.append(new_word)
                
        # count number of words and get sum of all word lengths to calculate average
        n_words = len(words)
        sum_of_lengths = len(''.join(words))
        avg_len = float(sum_of_lengths)/n_words
    return avg_len

@app.route('/words/avg_len', methods=['GET', 'POST'])
def avg_word_len():
    form = TextForm()
    if form.validate_on_submit():
    	avg_word_length = average_word_length(str(form.text.data))
    	flash('Average word length=%s' % (avg_word_length))
        return redirect('/words/avg_len')
    return render_template('avg_word_len.html', 
                           title='Average Word Length',
                           form=form)

def most_common_word(text=None):
    # check to make sure input is not blank or wrong type
    if text == None:
        common_word = 'Error: empy text'
    elif type(text) != str:
        common_word = 'Error: not valid input type'
    else:
        # split the text into a list, split at each whitespace char
        raw_words = text.split()
        # remove all words that are not purely letters
        words = [word for word in raw_words if word.isalpha()]
        
        # remove the non-letter characters except for "-" and "'"
        # add these new words to list
        for word in raw_words:
            if not word.isalpha():
                new_word = ''
                for char in word:
                    if (char.isalpha()) or (char == "'") or (char == "-"):
                        new_word += char
                if (len(new_word) >= 1) and (new_word != "'") and (new_word != "-"):
                    words.append(new_word)
                    
        # create dictionary to store word and count
        word_count = {}
        for word in words:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # create a list to store the word(s) that occur most frequently
        common_words = []
        for key, value in word_count.iteritems():
            if value == max(word_count.values()):
                common_words.append(key)
        # if there is more than one most common word, sort alphabetically, return first
        common_words.sort() 
    return common_words[0]

@app.route('/words/most_com', methods=['GET', 'POST'])
def most_com_word():
    form = TextForm()
    if form.validate_on_submit():
    	common_word = most_common_word(str(form.text.data))
    	flash('Most common word:' + common_word)
        return redirect('/words/most_com')
    return render_template('most_com_word.html', 
                           title='Most Common Word',
                           form=form)


def find_median_word(text=None):
    # check to make sure input is not blank or wrong type
    if text == None:
        common_word = 'Error: empy text'
    elif type(text) != str:
        common_word = 'Error: not valid input type'
    else:
        # split the text into a list, split at each whitespace char
        raw_words = text.split()
        # remove all words that are not purely letters
        words = [word for word in raw_words if word.isalpha()]
        
        # remove the non-letter characters except for "-" and "'"
        # add these new words to list
        for word in raw_words:
            if not word.isalpha():
                new_word = ''
                for char in word:
                    if (char.isalpha()) or (char == "'") or (char == "-"):
                        new_word += char
                if (len(new_word) >= 1) and (new_word != "'") and (new_word != "-"):
                    words.append(new_word)
                    
        # create dictionary to store word and count
        word_count = {}
        for word in words:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # create a list to store the median word(s)
        median_words = []
        # find out whether or not we will have a tie for the median number of words
        if len(word_count)%2 == 1: index = [len(word_count)/2]
        else: index = [len(word_count)/2-1, len(word_count)/2]
        # store median appearance number(s)
        counts = sorted(word_count.values())
        median_appearances = [counts[i] for i in index]
            
        for key, value in word_count.iteritems():
            if (value in median_appearances):
                median_words.append(key)
        # if there is more than one most common word, sort alphabetically, return first
        median_words.sort() 
    return median_words[0]


@app.route('/words/median', methods=['GET', 'POST'])
def median_word():
    form = TextForm()
    if form.validate_on_submit():
    	med_word = find_median_word(str(form.text.data))
    	flash('Median word:' + med_word)
        return redirect('/words/median')
    return render_template('median_word.html', 
                           title='Median Word',
                           form=form)









