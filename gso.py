import os
import psycopg2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

matchID = input('Match ID: ')
teamID = input('Match ID: ')
DATABASE_URL = 'postgres://guutwjjarimvko:71a1eeb140752e9c5d555bd2004caef0056b65362926a29bb64e8be1727bb1a8@ec2-54-165-164-38.compute-1.amazonaws.com:5432/ddb8599tmhdji5'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
cur.execute('SELECT * FROM public.shot_map WHERE "MatchID" = %s AND "TeamID" = %s', (matchID,teamID,))

rows = cur.fetchall()

img = Image.open("./assets/images/HockeyCircleGSO.png").convert('RGB')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 35)

for row in rows:
    if row[6] == True:
        colour = (0,255,0)
    else:
        colour = (255,0,0)
    draw.text((row[2],row[3]),"X",fill=colour,font=font)

img.save('./assets_output/' + 'GSOs.png')