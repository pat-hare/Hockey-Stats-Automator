from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from sqlconnector import getSeasonTurnovers, getSeasonPCShots

def createCircleEntryImage(basic_metrics, team):
    img = Image.open("./assets/images/HockeyCircle.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 25)
    # CE1
    draw.text((418, 81),str(basic_metrics['ce']['1']['goals']),(255,255,255),font=font)
    draw.text((418, 122),str(basic_metrics['ce']['1']['pc_win']),(255,255,255),font=font)
    draw.text((418, 163),str(basic_metrics['ce']['1']['gso']),(255,255,255),font=font)
    draw.text((418, 204),str(basic_metrics['ce']['1']['pp_win']),(255,255,255),font=font)
    draw.text((418, 245),str(0),(255,255,255),font=font)
    draw.text((418, 286),str(basic_metrics['ce']['1']['loss']),(255,255,255),font=font)

    # CE2
    draw.text((575, 461),str(basic_metrics['ce']['2']['goals']),(255,255,255),font=font)
    draw.text((575, 502),str(basic_metrics['ce']['2']['pc_win']),(255,255,255),font=font)
    draw.text((575, 543),str(basic_metrics['ce']['2']['gso']),(255,255,255),font=font)
    draw.text((575, 584),str(basic_metrics['ce']['2']['pp_win']),(255,255,255),font=font)
    draw.text((575, 625),str(0),(255,255,255),font=font)
    draw.text((575, 666),str(basic_metrics['ce']['2']['loss']),(255,255,255),font=font)

    # CE3
    draw.text((875, 631),str(basic_metrics['ce']['3']['goals']),(255,255,255),font=font)
    draw.text((875, 672),str(basic_metrics['ce']['3']['pc_win']),(255,255,255),font=font)
    draw.text((875, 713),str(basic_metrics['ce']['3']['gso']),(255,255,255),font=font)
    draw.text((968, 631),str(basic_metrics['ce']['3']['pp_win']),(255,255,255),font=font)
    draw.text((968, 672),str(0),(255,255,255),font=font)
    draw.text((968, 713),str(basic_metrics['ce']['3']['loss']),(255,255,255),font=font)

    # CE4
    draw.text((1292, 462),str(basic_metrics['ce']['4']['goals']),(255,255,255),font=font)
    draw.text((1292, 503),str(basic_metrics['ce']['4']['pc_win']),(255,255,255),font=font)
    draw.text((1292, 544),str(basic_metrics['ce']['4']['gso']),(255,255,255),font=font)
    draw.text((1292, 585),str(basic_metrics['ce']['4']['pp_win']),(255,255,255),font=font)
    draw.text((1292, 626),str(0),(255,255,255),font=font)
    draw.text((1292, 667),str(basic_metrics['ce']['4']['loss']),(255,255,255),font=font)

    # CE5
    draw.text((1440, 81),str(basic_metrics['ce']['5']['goals']),(255,255,255),font=font)
    draw.text((1440, 122),str(basic_metrics['ce']['5']['pc_win']),(255,255,255),font=font)
    draw.text((1440, 164),str(basic_metrics['ce']['5']['gso']),(255,255,255),font=font)
    draw.text((1440, 205),str(basic_metrics['ce']['5']['pp_win']),(255,255,255),font=font)
    draw.text((1440, 246),str(0),(255,255,255),font=font)
    draw.text((1440, 287),str(basic_metrics['ce']['5']['loss']),(255,255,255),font=font)

    # arrows
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 35)
    draw.text((488, 173),str(basic_metrics['ce']['1']['total']),(0,0,0),font=font)
    draw.text((628, 425),str(basic_metrics['ce']['2']['total']),(0,0,0),font=font)
    draw.text((902, 530),str(basic_metrics['ce']['3']['total']),(0,0,0),font=font)
    draw.text((1175, 430),str(basic_metrics['ce']['4']['total']),(0,0,0),font=font)
    draw.text((1320, 173),str(basic_metrics['ce']['5']['total']),(0,0,0),font=font)

    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 45)
    draw.text((466, 800),str(basic_metrics['25e']['L']),(0,0,0),font=font)
    draw.text((886, 800),str(basic_metrics['25e']['C']),(0,0,0),font=font)
    draw.text((1308, 800),str(basic_metrics['25e']['R']),(0,0,0),font=font)

    img.save('./assets_output/' + team + ' Circle Entries.png')

def createSeasonTurnoverImage():
    turnovers = getSeasonTurnovers()
    img = Image.open("./assets/images/HockeyPitch.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 65)

    # Expected Numbers
    draw.text((155, 320),"1",(255,255,0),font=font)
    draw.text((380, 320),"1",(255,255,0),font=font)
    draw.text((650, 320),"1",(255,255,0),font=font)
    draw.text((885, 320),"1",(255,255,0),font=font)

    draw.text((155, 495),"1",(255,255,0),font=font)
    draw.text((380, 495),"1",(255,255,0),font=font)
    draw.text((650, 495),"1",(255,255,0),font=font)
    draw.text((885, 495),"1",(255,255,0),font=font)

    draw.text((155, 690),"1",(255,255,0),font=font)
    draw.text((380, 690),"1",(255,255,0),font=font)
    draw.text((650, 690),"1",(255,255,0),font=font)
    draw.text((885, 690),"1",(255,255,0),font=font)

    draw.text((155, 885),"1",(255,255,0),font=font)
    draw.text((380, 885),"1",(255,255,0),font=font)
    draw.text((650, 885),"1",(255,255,0),font=font)
    draw.text((885, 885),"1",(255,255,0),font=font)

    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 25)
    # Total Wins
    draw.text((80, 305),"1",(255,255,255),font=font)
    draw.text((295, 305),"1",(255,255,255),font=font)
    draw.text((550, 305),"1",(255,255,255),font=font)
    draw.text((820, 305),"1",(255,255,255),font=font)

    draw.text((80, 450),"1",(255,255,255),font=font)
    draw.text((295, 450),"1",(255,255,255),font=font)
    draw.text((550, 450),"1",(255,255,255),font=font)
    draw.text((820, 450),"1",(255,255,255),font=font)

    draw.text((80, 650),"1",(255,255,255),font=font)
    draw.text((295, 650),"1",(255,255,255),font=font)
    draw.text((550, 650),"1",(255,255,255),font=font)
    draw.text((820, 650),"1",(255,255,255),font=font)

    draw.text((80, 840),"1",(255,255,255),font=font)
    draw.text((295, 840),"1",(255,255,255),font=font)
    draw.text((550, 840),"1",(255,255,255),font=font)
    draw.text((820, 840),"1",(255,255,255),font=font)

    # Total Wins Percentage
    draw.text((235, 305),"1",(255,255,255),font=font)
    draw.text((490, 305),"1",(255,255,255),font=font)
    draw.text((760, 305),"1",(255,255,255),font=font)
    draw.text((960, 305),"1",(255,255,255),font=font)

    draw.text((235, 450),"1",(255,255,255),font=font)
    draw.text((490, 450),"1",(255,255,255),font=font)
    draw.text((760, 450),"1",(255,255,255),font=font)
    draw.text((960, 450),"1",(255,255,255),font=font)

    draw.text((235, 650),"1",(255,255,255),font=font)
    draw.text((490, 650),"1",(255,255,255),font=font)
    draw.text((760, 650),"1",(255,255,255),font=font)
    draw.text((960, 650),"1",(255,255,255),font=font)

    draw.text((235, 840),"1",(255,255,255),font=font)
    draw.text((490, 840),"1",(255,255,255),font=font)
    draw.text((760, 840),"1",(255,255,255),font=font)
    draw.text((960, 840),"1",(255,255,255),font=font)

    # Total Goals
    draw.text((80, 410),"1",(255,255,0),font=font)
    draw.text((295, 410),"1",(255,255,0),font=font)
    draw.text((550, 410),"1",(255,255,0),font=font)
    draw.text((820, 410),"1",(255,255,0),font=font)

    draw.text((80, 600),"1",(255,255,0),font=font)
    draw.text((295, 600),"1",(255,255,0),font=font)
    draw.text((550, 600),"1",(255,255,0),font=font)
    draw.text((820, 600),"1",(255,255,0),font=font)

    draw.text((80, 800),"1",(255,255,0),font=font)
    draw.text((295, 800),"1",(255,255,0),font=font)
    draw.text((550, 800),"1",(255,255,0),font=font)
    draw.text((820, 800),"1",(255,255,0),font=font)

    draw.text((80, 980),"1",(255,255,0),font=font)
    draw.text((295, 980),"1",(255,255,0),font=font)
    draw.text((550, 980),"1",(255,255,0),font=font)
    draw.text((820, 980),"1",(255,255,0),font=font)

    # Total Goals Percentage
    draw.text((235, 410),"1",(255,255,0),font=font)
    draw.text((490, 410),"1",(255,255,0),font=font)
    draw.text((760, 410),"1",(255,255,0),font=font)
    draw.text((960, 410),"1",(255,255,0),font=font)

    draw.text((235, 600),"1",(255,255,0),font=font)
    draw.text((490, 600),"1",(255,255,0),font=font)
    draw.text((760, 600),"1",(255,255,0),font=font)
    draw.text((960, 600),"1",(255,255,0),font=font)

    draw.text((235, 800),"1",(255,255,0),font=font)
    draw.text((490, 800),"1",(255,255,0),font=font)
    draw.text((760, 800),"1",(255,255,0),font=font)
    draw.text((960, 800),"1",(255,255,0),font=font)

    draw.text((235, 980),"1",(255,255,0),font=font)
    draw.text((490, 980),"1",(255,255,0),font=font)
    draw.text((760, 980),"1",(255,255,0),font=font)
    draw.text((960, 980),"1",(255,255,0),font=font)

    img.save('./assets_output/Turnovers.jpg')

def createPCShotMap(input_file, output_file):
    img = Image.open(input_file).convert('RGB')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 70)

    # out of the goal
    draw.text((120, 320),"1",(255,255,255),font=font)
    draw.text((622, 90),"1",(255,255,255),font=font)
    draw.text((1130, 320),"1",(255,255,255),font=font)

    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 25)
    # top left
    draw.text((255, 230),"1",(255,255,255),font=font)
    draw.text((435, 230),"1",(255,255,255),font=font)
    draw.text((255, 315),"1",(255,255,255),font=font)
    draw.text((435, 315),"1",(255,255,255),font=font)
    # middle left
    draw.text((255, 350),"1",(255,255,255),font=font)
    draw.text((435, 350),"1",(255,255,255),font=font)
    draw.text((255, 560),"1",(255,255,255),font=font)
    draw.text((435, 560),"1",(255,255,255),font=font)
    # bottom left
    draw.text((255, 595),"1",(0,0,0),font=font)
    draw.text((435, 595),"1",(0,0,0),font=font)
    draw.text((255, 685),"1",(0,0,0),font=font)
    draw.text((435, 685),"1",(0,0,0),font=font)
    # top middle
    draw.text((470, 230),"1",(255,255,255),font=font)
    draw.text((795, 230),"1",(255,255,255),font=font)
    draw.text((470, 560),"1",(255,255,255),font=font)
    draw.text((795, 560),"1",(255,255,255),font=font)
    # bottom middle left
    draw.text((470, 595),"1",(0,0,0),font=font)
    draw.text((615, 595),"1",(0,0,0),font=font)
    draw.text((470, 685),"1",(0,0,0),font=font)
    draw.text((615, 685),"1",(0,0,0),font=font)
    # bottom middle right
    draw.text((650, 595),"1",(0,0,0),font=font)
    draw.text((795, 595),"1",(0,0,0),font=font)
    draw.text((650, 685),"1",(0,0,0),font=font)
    draw.text((795, 685),"1",(0,0,0),font=font)
    # top left
    draw.text((830, 230),"1",(255,255,255),font=font)
    draw.text((1010, 230),"1",(255,255,255),font=font)
    draw.text((830, 315),"1",(255,255,255),font=font)
    draw.text((1010, 315),"1",(255,255,255),font=font)
    # middle left
    draw.text((830, 350),"1",(255,255,255),font=font)
    draw.text((1010, 350),"1",(255,255,255),font=font)
    draw.text((830, 560),"1",(255,255,255),font=font)
    draw.text((1010, 560),"1",(255,255,255),font=font)
    # bottom left
    draw.text((830, 595),"1",(0,0,0),font=font)
    draw.text((1010, 595),"1",(0,0,0),font=font)
    draw.text((830, 685),"1",(0,0,0),font=font)
    draw.text((1010, 685),"1",(0,0,0),font=font)

    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 50)
    # conceded counts
    draw.text((340, 255),"1",(255,255,255),font=font)
    draw.text((340, 430),"1",(255,255,255),font=font)
    draw.text((340, 620),"1",(0,0,0),font=font)
    draw.text((622, 380),"1",(255,255,255),font=font)
    draw.text((535, 620),"1",(0,0,0),font=font)
    draw.text((715, 620),"1",(0,0,0),font=font)
    draw.text((910, 255),"1",(255,255,255),font=font)
    draw.text((910, 430),"1",(255,255,255),font=font)
    draw.text((910, 620),"1",(0,0,0),font=font)

    img.save('./assets_output/' + output_file)

def createShotMap(input_file, output_file):
    img = Image.open(input_file).convert('RGB')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 35)
    # CE1
    draw.text((165, 30),"1",(255,255,255),font=font)
    draw.text((275, 30),"1",(255,255,255),font=font)
    # CE2
    draw.text((220, 210),"1",(255,255,255),font=font)
    draw.text((330, 210),"1",(255,255,255),font=font)
    # CE3
    draw.text((575, 450),"1",(255,255,255),font=font)
    draw.text((685, 450),"1",(255,255,255),font=font)
    # CE4
    draw.text((930, 210),"1",(255,255,255),font=font)
    draw.text((1040, 210),"1",(255,255,255),font=font)
    # CE5
    draw.text((1095, 30),"1",(255,255,255),font=font)
    draw.text((985, 30),"1",(255,255,255),font=font)
    # Reaction Zone
    draw.text((575, 30),"1",(0,0,0),font=font)
    draw.text((685, 30),"1",(0,0,0),font=font)

    img.save('./assets_output/' + output_file)

def createAllShotMap():
    createPCShotMap('ShotMapFor.png', 'Shot Map For.png')
    createPCShotMap('ShotMapAgainst.png', 'Shot Map Against.png')

def createAllPCShotMap():
    createPCShotMap('PCA.png','PCA Shot Map.png')
    createPCShotMap('PCD.png','PCD Shot Map.png')
