#!/bin/bash

# Set bash environment variables for the two statements
export STATEMENT1="statement1"
export STATEMENT2="statement2"

# Collect tweets from the past month for each statement
#twarc search "$STATEMENT1" --since 2021-11-01 > statement1.json
#twarc search "$STATEMENT2" --since 2021-11-01 > statement2.json

# Use jq to extract the text of each tweet and save it to a separate file
jq -r '.full_text' statement1.json > statement1_text.txt
jq -r '.full_text' statement2.json > statement2_text.txt

# Use vader sentiment analysis to analyze the sentiment of each tweet and save the results to a file

python <<EOF
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
with open('statement1_text.txt') as f:
    for line in f:
        print('{},{}'.format(line, analyzer.polarity_scores(line)['compound']))
EOF > statement1_sentiment.txt

python <<EOF
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
with open('statement2_text.txt') as f:
    for line in f:
        print('{},{}'.format(line, analyzer.polarity_scores(line)['compound']))
EOF > statement2_sentiment.txt


# Use gnuplot to create an ASCII graph showing the
# overlapping distribution of sentiment scores
