# gui_tweetcrawler
Twitter crawling program implemented by graphic <br />
<img src="/images/korean ver.png" width="100px" height="65px" title="korean" alt="korean"></img>
<img src="/images/english ver.png" width="100px" height="65px" title="english" alt="english"></img> <br />
- email address : jms393497@gmail.com <br />
- blog : https://popcorn16.tistory.com/ <br />

## Introduction
1. Get tweets based on the information you set (keyword, start date, end date, limitation).
2. The raw data of tweets are stored in "files/keyword_raw.csv".
3. Use konlpy to analyze morphology and extract nouns.
4. Generate Wordcloud according to the number of nouns and store it in "files/keyword_wordcloud.png".
<br /><img src="/images/results.png" width="40%" height="40%" title="results" alt="results"></img>

## Development Environment
- Python @3.7.6

## Dependency
- twitterscraper <br />
pip3 install twitterscraper
- konlpy <br />
pip3 install konlpy
- wordcloud <br />
pip3 install wordcloud
- matplotlib <br />
pip3 install matplotlib

## License
gui_tweetcrawler is released under the MIT License. http://www.opensource.org/licenses/mit-license
