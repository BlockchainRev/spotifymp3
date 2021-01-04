# spotifymp3 for Mac
Spotify to MP3 is a service to take a .csv of your Spotify playlist (instructions on how to get that below) and then download every song to a .mp3 format.

The instructions are made (really) easy, so anyone can use this.




1) Go to joellehman.com/playlist/index.html and export the playlist to .csv format If make .csv does not work, just copy the text into an Excel sheet and export to csv. It will format itself.


2) Clone this GitHub repository. 

3) Go to Chrome > Click the 3 dots on the right > Help > About Google Chrome > Check your version. 

It should be something like 86, 87, or 88.

4) Go to https://chromedriver.chromium.org/downloads and download the chromedriver that matches your operating system and Chrome version.

5) With a code editor (I recommend VS Code) , change the variable 'PATH' to the directory of the chromedriver.

For Windows, it would look similar to: C:/Downloads/chromedriver.exe
For Mac, it would look similar to: /Users/user/Downloads/chromedriver

Notice the extensions and lack thereof.

6) In VS Code, open the GitHub folder.

7) Copy and paste your .csv file into the GitHub Folder

8) Run the script

9) Provide the .csv name in the format **name.csv**

10) Wait for downloads to complete.
