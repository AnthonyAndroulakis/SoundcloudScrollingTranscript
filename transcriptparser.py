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
	htmltext += '<script>var MarkersInit'+tracknum+' = function(markers) {  var elements = document.querySelectorAll(".wavesurfer-marker'+tracknum+'");  Array.prototype.forEach.call(elements, function(el, i) {    var time_start = el.dataset.start;    var time_end = el.dataset.end;    var id = el.dataset.id;;    if (id >= 1) {      id = id - 1;    } else {      id = 0;    }    marker = {};    marker.time_start = time_start;    marker.time_end = time_end;    marker.dom = el;    if (typeof(markers[id]) === "undefined") {      markers[id] = [];    }    markers[id].push(marker);  });}document.onreadystatechange = () => {  if (document.readyState === "complete") {    var markers = [];    MarkersInit'+tracknum+'(markers);    var iframeElement = document.querySelectorAll("sound'+tracknum+'");    var widget = SC.Widget(iframeElement);    var elements = document.querySelectorAll(".wavesurfer-marker'+tracknum+'");    Array.prototype.forEach.call(elements, function(el, i) {      el.onclick = function() {        var pos = el.dataset.start * 1000 +1;        widget.seekTo(pos);      }    });    widget.bind(SC.Widget.Events.PLAY_PROGRESS, function() {      widget.getPosition(function(current_time) {        current_time = current_time / 1000;        var j = 0;        markers[j].forEach(function(marker, i) {          if (current_time >= marker.time_start && current_time <= marker.time_end) {            marker.dom.classList.add("wavesurfer-marker-current'+tracknum+'");            marker.dom.scrollIntoView({ block: "nearest"})          } else {            marker.dom.classList.remove("wavesurfer-marker-current'+tracknum+'");          }        });      });    });  }};</script>'
	htmltext += '<style>.wavesurfer-transcript'+tracknum+'{width:600px;height:200px;font-size:17px;position:relative;font-family:Arial,sans-serif;overflow:auto}.wavesurfer-marker'+tracknum+':hover{cursor:pointer;background-color:#c9f3f3}.wavesurfer-marker-current'+tracknum+'{background-color:#e2fbfb}</style>'
	open(tracknum+'.html','w').write(htmltext)

run(sys.argv[1])
