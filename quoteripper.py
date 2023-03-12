# %%
import requests
import re
from bs4 import BeautifulSoup
import datetime
nowstart = datetime.datetime.now()
print("start time:", now.strftime("%Y-%m-%d %H:%M:%S"))

word = 'Marcus Aurelius'
url = 'https://en.wikiquote.org/w/index.php?action=edit&title=' + word

#specific to wikiquote, the lines will start with text you want to remove
prefixes_to_remove = [
    '* I',
    '** I',
    '*** I',
    '**** I',
    '* V',
    '** V',
    '*** V',
    '**** V',
    '* X',
    '** X',
    '*** X',
    '**** X'
]

# Get the page content and extract quotes
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
quotes = soup.text
quotes = re.sub("===([a-z]|[A-Z]|\s|[0-9]|[\\'-_@!#$<>%&\\(\\)\\[\\]])*===", "<hr width=\"50%\"/>\n", quotes)
quotes = re.sub("\\[\\[w:([a-z]|[A-Z]|\s|[0-9]|[\\'-_@!#$%&\\(\\)\\[\\]])*\\|", "", quotes)
quotes = re.sub("\\]\\]", "", quotes)
quotes = re.sub("\\:\'\'\'", "<b>", quotes)
quotes = re.sub("=\s", "=", quotes)
quotes = re.sub("\s=", "=", quotes)
quotes = re.sub("\n\n", "\n", quotes)
quotes = re.sub("\n\n", "\n", quotes)
quotes = re.sub("<\s", "<", quotes)
quotes = re.sub("\s>", ">", quotes)
quotes = re.sub("\'\'\'", "<b>", quotes)
quotes = re.sub("\\:\'\'", "<i>", quotes)
quotes = re.sub("\'\'", "<i>", quotes)
extracted = re.sub("\\<hr width=\"50\\%\"\\/>\\n", "%%%%\n\n", quotes)
extracted = re.split("%%%%\n", extracted)
extracted.remove(extracted[-1])
extracted.remove(extracted[0])

# Write extracted quotes to txt file in local folder
with open('extract.txt', 'w', encoding='utf-8') as f:
    f.writelines(extracted)

quotes = re.sub("\\<hr width=\"50\\%\"\\/>\\n", f"\n - {word.replace('_', ' ')}\n%%%%\n%\n", quotes)
quotes = re.sub("<b>", "", quotes)
quotes = re.sub("<i>", "", quotes)
quotes = re.split("%%%%\n", quotes)
quotes.remove(quotes[-1])
quotes.remove(quotes[0])
quotes[0] = quotes[0].replace('%\n', '')

# Write extracted quotes to txt file in local folder
with open('extract.txt', 'w', encoding='utf-8') as f:
    f.writelines(extracted)

# Open the extracted quote file for reading
with open('extract.txt', 'r', encoding='iso-8859-1') as infile:
    # Read in the contents of the file
    text = infile.read()

# Clean quotes in extracted file
text = re.sub(r'<.*?>|\S*\.jpg\S*|\S*#\S*', '', text)
text = re.sub(r'[^\x00-\x7F]+', '', text)
text = re.sub(r'\s+\S*:\S+\s+|\S+:\S+\s+|\s+\S*:\S+', '', text)
text = re.sub(r'\([^()]*\)', '', text)
text = re.sub(r'^[^\r\na-zA-Z]*[^\r\na-zA-Z\s]+[^\r\na-zA-Z]*$|^\s*$', '', text, flags=re.MULTILINE)
text = text.replace('[', '')
text = text.replace(']', '')

# Open the cleaned sentences output file for writing
with open('cleaned_sentences.txt', 'w', encoding='utf-8') as outfile:
# Write the modified text to the output file
    outfile.write(text)

# Open the cleaned sentences file for reading
with open('cleaned_sentences.txt', 'r', encoding='iso-8859-1') as infile:
    # Read in the contents of the file
    text = infile.readlines()

# Remove unwanted lines from text based on the dictionary at the start of the code
for prefix in prefixes_to_remove:
    text = [line for line in text if not line.startswith(prefix)]
text = [line for line in text if '|' not in line]


# Clean text and write to file - this edits the start of lines where the prior code removes entire pointless lines
text = [line.strip() for line in text if line.strip() != '']
text = '\n\n'.join(text) + '\n'
text = text.replace('[', '')
text = text.replace(']', '')
text = text.replace('*', '')
text = text.replace('** ', '')
text = text.replace('*** ', '')
text = text.replace('**** ', '')
text = re.sub(r'^\s+', '', text, flags=re.MULTILINE)
text = text.replace("\n", "\n\n")


with open('cleaned_sentences.txt', 'w', encoding='utf-8') as outfile:
    # Write the modified text to the output file
    outfile.write(text)

with open('cleaned_sentences.txt', 'r', encoding='utf-8') as infile:
    # Read in the contents of the file
    text = infile.read()


# Find all non-ASCII characters in the text
non_ascii_chars = re.findall('[^\x00-\x7F]', text)

# Print the list of non-ASCII characters to terminal
print("Here is a list of non ASCII characters:")
print(non_ascii_chars)

with open('cleaned_sentences.txt', 'r', encoding='utf-8') as infile:
    # Read in the contents of the file
    text = infile.read()

#find any loose characters that are not single letter words
pattern = r"\b(?!(a|i)\b)\w\b"

x = re.findall(pattern, text, re.IGNORECASE)
print("Here is a list of loose characters to clean up:")
print(x)

# Open the input file for reading
with open("cleaned_sentences.txt", "r") as input_file:
    # Read the contents of the input file
    contents = input_file.read()

# Define the regular expression to find words that are one character long (excluding "a" and "i")
pattern = r"\b(?!(a|i)\b)\w\b"

print("~~~REPLACING LOOSE CHARACTERS~~~")
# Replace any matches with an empty string
modified_contents = re.sub(pattern, "", contents, flags=re.IGNORECASE)

# Open the output file for writing
with open("cleaned_sentences.txt", "w") as output_file:
    # Write the modified contents to the output file
    output_file.write(modified_contents)


with open('cleaned_sentences.txt', 'r', encoding='utf-8') as infile:
    # Read in the contents of the file
    text = infile.read()


pattern = r"\b(?!(a|i)\b)\w\b"

x = re.findall(pattern, text, re.IGNORECASE)
print("Here is the cleaned up list of loose characters :")
print(x)


# Open the input file for reading
with open('cleaned_sentences.txt', "r") as input_file:
    # Read the contents of the input file
    contents = input_file.readlines()

# Filter out lines shorter than 10 characters
filtered_contents = [line for line in contents if len(line.strip()) >= 10]

# Add an empty line between each line of text
filtered_contents = "\n".join(filtered_contents).replace("\n", "\n\n")

# Open the output file for writing
print("~~~PRINTING CONTENTS TO FINAL.TXT~~~")
with open('final.txt', "w") as output_file:
    # Write the filtered contents to the output file
    output_file.writelines(filtered_contents)

nowstop = datetime.datetime.now()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Finished ripping quotes at:", nowstop.strftime("%Y-%m-%d %H:%M:%S"))
elapsed_time = nowstop - nowstart
elapsed_seconds = elapsed_time.total_seconds()

if elapsed_seconds >= 86400:
    elapsed_value = elapsed_seconds / 86400
    elapsed_unit = "day"
elif elapsed_seconds >= 3600:
    elapsed_value = elapsed_seconds / 3600
    elapsed_unit = "hour"
elif elapsed_seconds >= 60:
    elapsed_value = elapsed_seconds / 60
    elapsed_unit = "minute"
else:
    elapsed_value = elapsed_seconds
    elapsed_unit = "second"

elapsed_str = f"{elapsed_value:.1f} {elapsed_unit}"
if elapsed_value != 1:
    elapsed_str += "s"

print(f"Elapsed time: {elapsed_str}")
print("\n")


