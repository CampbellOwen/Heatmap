import heatmap
from bs4 import BeautifulSoup

'''
Edit variables for appropriate file and settings
'''
filename = "graffiti.kml"
outputName = "final.kml"
tag = "coordinates"
dotsize = 20
opacity = 128
size = (1024,1024)
colourScheme = "classic"
area = None

def GetCoordinates(file, tag):
	soup = BeautifulSoup(open(file))
	raw_tags = soup.find_all(tag)
	tag_contents = [data.contents for data in raw_tags]
	format_contents = []
	for x in range(len(tag_contents)):
		format_contents.append(str(tag_contents[x][0]))
	coordinates = []
	for x in range(len(format_contents)):
		comma = []
		for i in range(len(format_contents[x])):
			if format_contents[x][i] == ',':
				comma.append(i)
		coordinates.append([float(format_contents[x][0:comma[0]].strip("'")), float(format_contents[x][comma[0]+1:comma[1]].strip("'"))])
	return coordinates
	
def Generate_map(points):
		hm.heatmap(points, dotsize, opacity, size, colourScheme, area)
		hm.saveKML(outputName)
		
hm = heatmap.Heatmap()	
points = GetCoordinates(filename, tag)
Generate_map(points)