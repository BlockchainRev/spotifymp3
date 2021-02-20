# spotifymp3 
### Spotify to MP3 is a service to take a .csv of your Spotify playlist (instructions below) and then download every song to a .mp3 format. ###
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Description ##

This takes the csv, searches the keywords on Youtube, takes the first link, and downloads the video. Not perfect and can possibly return the wrong file. Also, there may be a UI coming soon!

** ~750-800 song playlist will take 2 hours, and a 100 song playlist 15 minutes.**
The instructions are made (really) easy, so anyone can use this.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Steps #
1) Go to joellehman.com/playlist/index.html and export the playlist to .csv format If make .csv does not work, just copy the text into an Excel sheet and export to csv. It will format itself. It should look exactly like this format. 
 
*Foreign characters may come out off because of encodings. I've found Macs work with Cyrillic letters and Windows often doesn't*

![If image does not load, check Images folder](https://raw.githubusercontent.com/BlockchainRev/spotifymp3/main/Images/Screen%20Shot%202021-01-04%20at%2012.11.49%20PM.png?token=ALLIN5635FPXI5TUWROURGK76NS7Y)

2) Clone this GitHub repository. 

3) Go to Chrome > Click the 3 dots on the right > Help > About Google Chrome > Check your version. 

It should be something like 86, 87, or 88.

4) Go to https://chromedriver.chromium.org/downloads and download the chromedriver that matches your operating system and Chrome version.

5) With a code editor (I recommend VS Code) , change the variable 'PATH' that's indicated in the code to the directory of the chromedriver.

For Windows, it would look similar to: C:/Downloads/chromedriver.exe
For Mac, it would look similar to: /Users/user/Downloads/chromedriver

Notice the extensions and lack thereof.

6) In VS Code, open the GitHub folder.

7) Copy and paste your .csv file into the GitHub Folder

8) Run the script

9) Provide the .csv name in the format **name.csv**

10) Wait for downloads to complete.

