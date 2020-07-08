# AnkiCardMaker
#### A very boring title, I know. 

This is an application that generates Anki flashcards for any language. Anki is a spaced repetition flashcard software that is popular with GRE students and language learners. However, the process of creating flashcards is very tedious so most people end up using pre-made card decks. But there are no pre-made decks for languages that aren't mainstream. I wanted an easy way to create flashcards for any language.

The progress so far: the program can take in a list of URLs of webpages, and output a list containing a range of the most repeated words in those webpages. Then, it will use Google Translate via Selenium to obtain the words in Kannada, and their transliterations. The program takes quite a while to process each word right now, and this is because of Selenium. The reason I use Selenium is because I haven't been able to find a good online dictionary for Kannada yet and Google Translate cannot be scraped without Selenium (as far as I know). 

Features I plan to add:
<ol>
  <li>Give the user a choice between a custom set of URLs or automatically picked URLs from some news website</li>
  <li>A GUI</li>
  <li>Cards with better formatting</li>
  <li>This one's a long shot, but cards with images</li>
</ol>

