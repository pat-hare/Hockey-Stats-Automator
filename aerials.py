import os
import psycopg2
from PIL import Image
from PIL import ImageDraw

matchID = input('Match ID: ')
teamID = input('Match ID: ')
DATABASE_URL = 'postgres://guutwjjarimvko:71a1eeb140752e9c5d555bd2004caef0056b65362926a29bb64e8be1727bb1a8@ec2-54-165-164-38.compute-1.amazonaws.com:5432/ddb8599tmhdji5'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
cur.execute('SELECT * FROM public.aerials WHERE "MatchID" = %s AND "TeamID" = %s', (matchID,teamID,))

rows = cur.fetchall()

img = Image.open("./assets/images/HockeyPitchAerials.png").convert('RGB')
draw = ImageDraw.Draw(img)

for row in rows:
    if row[6] == True:
        colour = (255,0,0)
    else:
        colour = (0,255,0)
    draw.line((row[4],row[5], row[2],row[3]), fill=colour, width=3)

img.save('./assets_output/' + 'Aerials.png')