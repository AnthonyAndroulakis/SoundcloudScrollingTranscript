# SoundcloudScrollingTranscript
<img align="center" src="https://github.com/AnthonyAndroulakis/SoundcloudScrollingTranscript/blob/master/screenshot.png" alt="screenshot" width="400" height="300">
Demo: https://repl.it/@AnthonyAndroula/soundcloudtranscript

Slightly modified version of (changes: autoscrolling, some css changes, multi-line transcripts (see demo)):
https://codepen.io/X-Raym/pen/QdwEgJ

Demo soundcloud song used: https://soundcloud.com/user-811313743/a-charlie-brown-christmas-christmastime-is-here-vocal

If you use this code, be sure to use an MIT license and cite this repo as well as https://codepen.io/X-Raym/pen/QdwEgJ.

This is simple to implement on your website; check out the repl demo I've provided.

# Transcript format (captions.en.csv)
```
hh:mm:ss:decisecond; LENGTH    
hh:mm:ss:decisecond; 1st words    
hh:mm:ss:decisecond; 2nd words    
hh:mm:ss:decisecond; 3rd words    
hh:mm:ss:decisecond; 4th words     
.     
.     
.     
```

# HtmlTranscriptGenerator (transcriptparser.py)
Example run: `python3 transcriptparser.py captions.en.csv` output will be named captions.en.txt      
Look at demo page to see where to paste this output.
