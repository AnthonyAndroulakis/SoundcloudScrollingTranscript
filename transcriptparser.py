#parse csv transcript file into html
import sys

def run(filename): #example input: captions.en.csv
	#first parse csv file for relevant data
	lines = open(filename).read().split('\n')
	data = [i.split(';') for i in lines]
	seconds = [[int(k) for k in j[0].split(':')][0]*3600+[int(k) for k in j[0].split(':')][1]*60+[int(k) for k in j[0].split(':')][2]+[int(k) for k in j[0].split(':')][3]*0.1 for j in data] #ignore first
	words = [l[1] for l in data] #ignore first
	timeDisplay = [m[0][:-2] for m in data]

	#check for any logic errors
	class TranscriptError(Exception):
    	pass

	if seconds[0]<seconds[-1]:
		raise TranscriptError("LENGTH needs to be greater than last time mark.")

	#create txt file with html-version of transcript
	htmltext = '<div class="wavesurfer-transcript">' #ending = </div>
	for i in range(len(data)-1): #look at i+1
		if i==len(data)-2: #if at last element
			htmltext += '<div class="wavesurfer-marker" data-start="'+str(seconds[i+1])+'" data-end="'+str(seconds[0])+'"> <table><tr><td>'+timeDisplay[i+1]+'&nbsp;&nbsp;</td> <td>'+words[i+1]+'</td></tr></table></div>'
		else:
			htmltext += '<div class="wavesurfer-marker" data-start="'+str(seconds[i+1])+'" data-end="'+str(seconds[i+2])+'"> <table><tr><td>'+timeDisplay[i+1]+'&nbsp;&nbsp;</td> <td>'+words[i+1]+'</td></tr></table></div>'

	htmltext += '</div>'
	open(filename[:-4]+'.txt','w').write(htmltext)

run(sys.argv[1])