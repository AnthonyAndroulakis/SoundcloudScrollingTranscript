#parse csv transcript file into html
import sys

def run(filename): #example input: captions.en.csv
	#first parse csv file for relevant data
	lines = open(filename).read().split('\n')
	lines = list(filter(None, lines))
	data = [i.split(';') for i in lines][1:]
	tracknum = lines[0].split(';')[0] #make tracknum id name in html and js
	seconds = [[int(k) for k in j[0].split(':')][0]*3600+[int(k) for k in j[0].split(':')][1]*60+[int(k) for k in j[0].split(':')][2]+[int(k) for k in j[0].split(':')][3]*0.1 for j in data] #ignore first
	words = [l[1] for l in data] #ignore first
	timeDisplay = [m[0][:-2] for m in data]

	#check for any logic errors
	class TranscriptError(Exception):
    		pass

	if seconds[0]<seconds[-1]:
		raise TranscriptError("LENGTH needs to be greater than last time mark.")

	#create txt file with html-version of transcript
	htmltext = '<h3 style="font-family:arial;"> Transcript: </h3>'
	htmltext += '<div class="wavesurfer-transcript'+tracknum+'">' #ending = </div>
	for i in range(len(data)-1): #look at i+1
		if i==len(data)-2: #if at last element
			htmltext += '<div class="wavesurfer-marker'+tracknum+'" data-start="'+str(seconds[i+1])+'" data-end="'+str(seconds[0])+'"> <table><tr><td>'+timeDisplay[i+1]+'&nbsp;&nbsp;</td> <td>'+words[i+1]+'</td></tr></table></div>'
		else:
			htmltext += '<div class="wavesurfer-marker'+tracknum+'" data-start="'+str(seconds[i+1])+'" data-end="'+str(seconds[i+2])+'"> <table><tr><td>'+timeDisplay[i+1]+'&nbsp;&nbsp;</td> <td>'+words[i+1]+'</td></tr></table></div>'

	htmltext += '</div>'
	htmltext += '<script>var MarkersInit=function(e){var r=document.querySelectorAll(".wavesurfer-marker'+tracknum+'");Array.prototype.forEach.call(r,function(r,t){var a=r.dataset.start,n=r.dataset.end,o=r.dataset.id;o>=1?o-=1:o=0,marker={},marker.time_start=a,marker.time_end=n,marker.dom=r,void 0===e[o]&&(e[o]=[]),e[o].push(marker)})};document.onreadystatechange=(()=>{if("complete"===document.readyState){var e=[];MarkersInit(e);var r=document.querySelectorAll("iframe").querySelectorAll("iframe[src=\'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/'+tracknum+'&amp;color=ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false\']"),t=SC.Widget(r),a=document.querySelectorAll(".wavesurfer-marker'+tracknum+'");Array.prototype.forEach.call(a,function(e,r){e.onclick=function(){var r=1e3*e.dataset.start+1;t.seekTo(r)}}),t.bind(SC.Widget.Events.PLAY_PROGRESS,function(){t.getPosition(function(r){r/=1e3;e[0].forEach(function(e,t){r>=e.time_start&&r<=e.time_end?(e.dom.classList.add("wavesurfer-marker-current'+tracknum+'"),e.dom.scrollIntoView({block:"nearest"})):e.dom.classList.remove("wavesurfer-marker-current'+tracknum+'")})})})}});</script>'
	htmltext += '<style>.wavesurfer-transcript'+tracknum+'{width:600px;height:200px;font-size:17px;position:relative;font-family:Arial,sans-serif;overflow:auto}.wavesurfer-marker'+tracknum+':hover{cursor:pointer;background-color:#c9f3f3}.wavesurfer-marker-current'+tracknum+'{background-color:#e2fbfb}</style>'
	open(tracknum+'.html','w').write(htmltext)

run(sys.argv[1])
