from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from sqlconnector import getSeasonTurnovers, getSeasonPCShots, getSeasonShots

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
    draw.text((418, 286),str(basic_metrics['ce']['1']['lost']),(255,255,255),font=font)

    # CE2
    draw.text((575, 461),str(basic_metrics['ce']['2']['goals']),(255,255,255),font=font)
    draw.text((575, 502),str(basic_metrics['ce']['2']['pc_win']),(255,255,255),font=font)
    draw.text((575, 543),str(basic_metrics['ce']['2']['gso']),(255,255,255),font=font)
    draw.text((575, 584),str(basic_metrics['ce']['2']['pp_win']),(255,255,255),font=font)
    draw.text((575, 625),str(0),(255,255,255),font=font)
    draw.text((575, 666),str(basic_metrics['ce']['2']['lost']),(255,255,255),font=font)

    # CE3
    draw.text((875, 631),str(basic_metrics['ce']['3']['goals']),(255,255,255),font=font)
    draw.text((875, 672),str(basic_metrics['ce']['3']['pc_win']),(255,255,255),font=font)
    draw.text((875, 713),str(basic_metrics['ce']['3']['gso']),(255,255,255),font=font)
    draw.text((968, 631),str(basic_metrics['ce']['3']['pp_win']),(255,255,255),font=font)
    draw.text((968, 672),str(0),(255,255,255),font=font)
    draw.text((968, 713),str(basic_metrics['ce']['3']['lost']),(255,255,255),font=font)

    # CE4
    draw.text((1292, 462),str(basic_metrics['ce']['4']['goals']),(255,255,255),font=font)
    draw.text((1292, 503),str(basic_metrics['ce']['4']['pc_win']),(255,255,255),font=font)
    draw.text((1292, 544),str(basic_metrics['ce']['4']['gso']),(255,255,255),font=font)
    draw.text((1292, 585),str(basic_metrics['ce']['4']['pp_win']),(255,255,255),font=font)
    draw.text((1292, 626),str(0),(255,255,255),font=font)
    draw.text((1292, 667),str(basic_metrics['ce']['4']['lost']),(255,255,255),font=font)

    # CE5
    draw.text((1440, 81),str(basic_metrics['ce']['5']['goals']),(255,255,255),font=font)
    draw.text((1440, 122),str(basic_metrics['ce']['5']['pc_win']),(255,255,255),font=font)
    draw.text((1440, 164),str(basic_metrics['ce']['5']['gso']),(255,255,255),font=font)
    draw.text((1440, 205),str(basic_metrics['ce']['5']['pp_win']),(255,255,255),font=font)
    draw.text((1440, 246),str(0),(255,255,255),font=font)
    draw.text((1440, 287),str(basic_metrics['ce']['5']['lost']),(255,255,255),font=font)

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

def createCircleEntryImagePP(basic_metrics, team):
    img = Image.open("./assets/images/HockeyCirclePP.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 25)
    # CE1
    draw.text((418, 81),str(basic_metrics['ce']['1']['goals']),(255,255,255),font=font)
    draw.text((418, 122),str(basic_metrics['ce']['1']['pc_win']),(255,255,255),font=font)
    draw.text((418, 163),str(basic_metrics['ce']['1']['gso']),(255,255,255),font=font)
    draw.text((418, 204),str(basic_metrics['ce']['1']['pp_win']),(255,255,255),font=font)
    draw.text((418, 245),str(0),(255,255,255),font=font)
    draw.text((418, 286),str(basic_metrics['ce']['1']['lost']),(255,255,255),font=font)

    # CE2
    draw.text((575, 461),str(basic_metrics['ce']['2']['goals']),(255,255,255),font=font)
    draw.text((575, 502),str(basic_metrics['ce']['2']['pc_win']),(255,255,255),font=font)
    draw.text((575, 543),str(basic_metrics['ce']['2']['gso']),(255,255,255),font=font)
    draw.text((575, 584),str(basic_metrics['ce']['2']['pp_win']),(255,255,255),font=font)
    draw.text((575, 625),str(0),(255,255,255),font=font)
    draw.text((575, 666),str(basic_metrics['ce']['2']['lost']),(255,255,255),font=font)

    # CE3
    draw.text((875, 631),str(basic_metrics['ce']['3']['goals']),(255,255,255),font=font)
    draw.text((875, 672),str(basic_metrics['ce']['3']['pc_win']),(255,255,255),font=font)
    draw.text((875, 713),str(basic_metrics['ce']['3']['gso']),(255,255,255),font=font)
    draw.text((968, 631),str(basic_metrics['ce']['3']['pp_win']),(255,255,255),font=font)
    draw.text((968, 672),str(0),(255,255,255),font=font)
    draw.text((968, 713),str(basic_metrics['ce']['3']['lost']),(255,255,255),font=font)

    # CE4
    draw.text((1292, 462),str(basic_metrics['ce']['4']['goals']),(255,255,255),font=font)
    draw.text((1292, 503),str(basic_metrics['ce']['4']['pc_win']),(255,255,255),font=font)
    draw.text((1292, 544),str(basic_metrics['ce']['4']['gso']),(255,255,255),font=font)
    draw.text((1292, 585),str(basic_metrics['ce']['4']['pp_win']),(255,255,255),font=font)
    draw.text((1292, 626),str(0),(255,255,255),font=font)
    draw.text((1292, 667),str(basic_metrics['ce']['4']['lost']),(255,255,255),font=font)

    # CE5
    draw.text((1440, 81),str(basic_metrics['ce']['5']['goals']),(255,255,255),font=font)
    draw.text((1440, 122),str(basic_metrics['ce']['5']['pc_win']),(255,255,255),font=font)
    draw.text((1440, 164),str(basic_metrics['ce']['5']['gso']),(255,255,255),font=font)
    draw.text((1440, 205),str(basic_metrics['ce']['5']['pp_win']),(255,255,255),font=font)
    draw.text((1440, 246),str(0),(255,255,255),font=font)
    draw.text((1440, 287),str(basic_metrics['ce']['5']['lost']),(255,255,255),font=font)

    # arrows
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 35)
    draw.text((488, 173),str(basic_metrics['ce']['1']['total']),(0,0,0),font=font)
    draw.text((628, 425),str(basic_metrics['ce']['2']['total']),(0,0,0),font=font)
    draw.text((902, 530),str(basic_metrics['ce']['3']['total']),(0,0,0),font=font)
    draw.text((1175, 430),str(basic_metrics['ce']['4']['total']),(0,0,0),font=font)
    draw.text((1320, 173),str(basic_metrics['ce']['5']['total']),(0,0,0),font=font)

    img.save('./assets_output/' + team + ' Circle Entries PP.png')

def createCircleEntryImageLeftOnly(basic_metrics, team):
    img = Image.open("./assets/images/HockeyCircleLeftOnly.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 25)

    # CE3
    draw.text((875, 631),str(basic_metrics['ce']['3']['goals']),(255,255,255),font=font)
    draw.text((875, 672),str(basic_metrics['ce']['3']['pc_win']),(255,255,255),font=font)
    draw.text((875, 713),str(basic_metrics['ce']['3']['gso']),(255,255,255),font=font)
    draw.text((968, 631),str(basic_metrics['ce']['3']['pp_win']),(255,255,255),font=font)
    draw.text((968, 672),str(0),(255,255,255),font=font)
    draw.text((968, 713),str(basic_metrics['ce']['3']['lost']),(255,255,255),font=font)

    # CE4
    draw.text((1292, 462),str(basic_metrics['ce']['4']['goals']),(255,255,255),font=font)
    draw.text((1292, 503),str(basic_metrics['ce']['4']['pc_win']),(255,255,255),font=font)
    draw.text((1292, 544),str(basic_metrics['ce']['4']['gso']),(255,255,255),font=font)
    draw.text((1292, 585),str(basic_metrics['ce']['4']['pp_win']),(255,255,255),font=font)
    draw.text((1292, 626),str(0),(255,255,255),font=font)
    draw.text((1292, 667),str(basic_metrics['ce']['4']['lost']),(255,255,255),font=font)

    # CE5
    draw.text((1440, 81),str(basic_metrics['ce']['5']['goals']),(255,255,255),font=font)
    draw.text((1440, 122),str(basic_metrics['ce']['5']['pc_win']),(255,255,255),font=font)
    draw.text((1440, 164),str(basic_metrics['ce']['5']['gso']),(255,255,255),font=font)
    draw.text((1440, 205),str(basic_metrics['ce']['5']['pp_win']),(255,255,255),font=font)
    draw.text((1440, 246),str(0),(255,255,255),font=font)
    draw.text((1440, 287),str(basic_metrics['ce']['5']['lost']),(255,255,255),font=font)

    # arrows
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 35)
    draw.text((902, 530),str(basic_metrics['ce']['3']['total']),(0,0,0),font=font)
    draw.text((1175, 430),str(basic_metrics['ce']['4']['total']),(0,0,0),font=font)
    draw.text((1320, 173),str(basic_metrics['ce']['5']['total']),(0,0,0),font=font)

    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 45)
    draw.text((466, 800),str(basic_metrics['25e']['L']),(0,0,0),font=font)

    img.save('./assets_output/' + team + ' Circle Entries Left Only.png')

def createSeasonTurnoverImage():
    turnovers = getSeasonTurnovers()
    img = Image.open("./assets/images/HockeyPitch.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 65)

    # Expected Numbers
    draw.text((155, 320),str(turnovers['1.0']['PositiveWins']),(255,255,0),font=font)
    draw.text((380, 320),str(turnovers['2.0']['PositiveWins']),(255,255,0),font=font)
    draw.text((650, 320),str(turnovers['3.0']['PositiveWins']),(255,255,0),font=font)
    draw.text((885, 320),str(turnovers['4.0']['PositiveWins']),(255,255,0),font=font)

    draw.text((155, 495),str(turnovers['1.1']['PositiveWins']),(255,255,0),font=font)
    draw.text((380, 495),str(turnovers['2.1']['PositiveWins']),(255,255,0),font=font)
    draw.text((650, 495),str(turnovers['3.1']['PositiveWins']),(255,255,0),font=font)
    draw.text((885, 495),str(turnovers['4.1']['PositiveWins']),(255,255,0),font=font)

    draw.text((155, 690),str(turnovers['1.2']['PositiveWins']),(255,255,0),font=font)
    draw.text((380, 690),str(turnovers['2.2']['PositiveWins']),(255,255,0),font=font)
    draw.text((650, 690),str(turnovers['3.2']['PositiveWins']),(255,255,0),font=font)
    draw.text((885, 690),str(turnovers['4.2']['PositiveWins']),(255,255,0),font=font)

    draw.text((155, 885),str(turnovers['1.3']['PositiveWins']),(255,255,0),font=font)
    draw.text((380, 885),str(turnovers['2.3']['PositiveWins']),(255,255,0),font=font)
    draw.text((650, 885),str(turnovers['3.3']['PositiveWins']),(255,255,0),font=font)
    draw.text((885, 885),str(turnovers['4.3']['PositiveWins']),(255,255,0),font=font)

    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 25)
    # Total Wins
    draw.text((80, 305),str(turnovers['1.0']['TotalWins']),(255,255,255),font=font)
    draw.text((295, 305),str(turnovers['2.0']['TotalWins']),(255,255,255),font=font)
    draw.text((550, 305),str(turnovers['3.0']['TotalWins']),(255,255,255),font=font)
    draw.text((820, 305),str(turnovers['4.0']['TotalWins']),(255,255,255),font=font)

    draw.text((80, 450),str(turnovers['1.1']['TotalWins']),(255,255,255),font=font)
    draw.text((295, 450),str(turnovers['2.1']['TotalWins']),(255,255,255),font=font)
    draw.text((550, 450),str(turnovers['3.1']['TotalWins']),(255,255,255),font=font)
    draw.text((820, 450),str(turnovers['4.1']['TotalWins']),(255,255,255),font=font)

    draw.text((80, 650),str(turnovers['1.2']['TotalWins']),(255,255,255),font=font)
    draw.text((295, 650),str(turnovers['2.2']['TotalWins']),(255,255,255),font=font)
    draw.text((550, 650),str(turnovers['3.2']['TotalWins']),(255,255,255),font=font)
    draw.text((820, 650),str(turnovers['4.2']['TotalWins']),(255,255,255),font=font)

    draw.text((80, 840),str(turnovers['1.3']['TotalWins']),(255,255,255),font=font)
    draw.text((295, 840),str(turnovers['2.3']['TotalWins']),(255,255,255),font=font)
    draw.text((550, 840),str(turnovers['3.3']['TotalWins']),(255,255,255),font=font)
    draw.text((820, 840),str(turnovers['4.3']['TotalWins']),(255,255,255),font=font)

    # Total Wins Percentage
    if turnovers['1.0']['TotalWins'] != 0:
        draw.text((205, 305),(str(int(round((turnovers['1.0']['PositiveWins']/turnovers['1.0']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['2.0']['TotalWins'] != 0:
        draw.text((460, 305),(str(int(round((turnovers['2.0']['PositiveWins']/turnovers['2.0']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['3.0']['TotalWins'] != 0:
        draw.text((730, 305),(str(int(round((turnovers['3.0']['PositiveWins']/turnovers['3.0']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['4.0']['TotalWins'] != 0:
        draw.text((930, 305),(str(int(round((turnovers['4.0']['PositiveWins']/turnovers['4.0']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)

    if turnovers['1.1']['TotalWins'] != 0:
        draw.text((195, 450),(str(int(round((turnovers['1.1']['PositiveWins']/turnovers['1.1']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['2.1']['TotalWins'] != 0:
        draw.text((460, 450),(str(int(round((turnovers['2.1']['PositiveWins']/turnovers['2.1']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['3.1']['TotalWins'] != 0:
        draw.text((730, 450),(str(int(round((turnovers['3.1']['PositiveWins']/turnovers['3.1']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['4.1']['TotalWins'] != 0:
        draw.text((930, 450),(str(int(round((turnovers['4.1']['PositiveWins']/turnovers['4.1']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)

    if turnovers['1.2']['TotalWins'] != 0:
        draw.text((205, 650),(str(int(round((turnovers['1.2']['PositiveWins']/turnovers['1.2']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['2.2']['TotalWins'] != 0:
        draw.text((460, 650),(str(int(round((turnovers['2.2']['PositiveWins']/turnovers['2.2']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['3.2']['TotalWins'] != 0:
        draw.text((730, 650),(str(int(round((turnovers['3.2']['PositiveWins']/turnovers['3.2']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['4.2']['TotalWins'] != 0:
        draw.text((930, 650),(str(int(round((turnovers['4.2']['PositiveWins']/turnovers['4.2']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)

    if turnovers['1.3']['TotalWins'] != 0:
        draw.text((205, 840),(str(int(round((turnovers['1.3']['PositiveWins']/turnovers['1.3']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['2.3']['TotalWins'] != 0:
        draw.text((460, 840),(str(int(round((turnovers['2.3']['PositiveWins']/turnovers['2.3']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['3.3']['TotalWins'] != 0:
        draw.text((730, 840),(str(int(round((turnovers['3.3']['PositiveWins']/turnovers['3.3']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)
    if turnovers['4.3']['TotalWins'] != 0:
        draw.text((930, 840),(str(int(round((turnovers['4.3']['PositiveWins']/turnovers['4.3']['TotalWins']),2)*100))+'%'),(255,255,255),font=font)

    # Total Goals
    draw.text((80, 410),str(turnovers['1.0']['GSO']),(255,255,0),font=font)
    draw.text((295, 410),str(turnovers['2.0']['GSO']),(255,255,0),font=font)
    draw.text((550, 410),str(turnovers['3.0']['GSO']),(255,255,0),font=font)
    draw.text((820, 410),str(turnovers['4.0']['GSO']),(255,255,0),font=font)

    draw.text((80, 600),str(turnovers['1.1']['GSO']),(255,255,0),font=font)
    draw.text((295, 600),str(turnovers['2.1']['GSO']),(255,255,0),font=font)
    draw.text((550, 600),str(turnovers['3.1']['GSO']),(255,255,0),font=font)
    draw.text((820, 600),str(turnovers['4.1']['GSO']),(255,255,0),font=font)

    draw.text((80, 800),str(turnovers['1.2']['GSO']),(255,255,0),font=font)
    draw.text((295, 800),str(turnovers['2.2']['GSO']),(255,255,0),font=font)
    draw.text((550, 800),str(turnovers['3.2']['GSO']),(255,255,0),font=font)
    draw.text((820, 800),str(turnovers['4.2']['GSO']),(255,255,0),font=font)

    draw.text((80, 980),str(turnovers['1.3']['GSO']),(255,255,0),font=font)
    draw.text((295, 980),str(turnovers['2.3']['GSO']),(255,255,0),font=font)
    draw.text((550, 980),str(turnovers['3.3']['GSO']),(255,255,0),font=font)
    draw.text((820, 980),str(turnovers['4.3']['GSO']),(255,255,0),font=font)

    # Total Goals Percentage
    if turnovers['1.0']['TotalWins'] != 0:
        draw.text((2305, 410),(str(int(round((turnovers['1.0']['GSO']/turnovers['1.0']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['2.0']['TotalWins'] != 0:
        draw.text((460, 410),(str(int(round((turnovers['2.0']['GSO']/turnovers['2.0']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['3.0']['TotalWins'] != 0:
        draw.text((730, 410),(str(int(round((turnovers['3.0']['GSO']/turnovers['3.0']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['4.0']['TotalWins'] != 0:
        draw.text((930, 410),(str(int(round((turnovers['4.0']['GSO']/turnovers['4.0']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)

    if turnovers['1.1']['TotalWins'] != 0:
        draw.text((205, 600),(str(int(round((turnovers['1.1']['GSO']/turnovers['1.1']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['2.1']['TotalWins'] != 0:
        draw.text((460, 600),(str(int(round((turnovers['2.1']['GSO']/turnovers['2.1']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['3.1']['TotalWins'] != 0:
        draw.text((730, 600),(str(int(round((turnovers['3.1']['GSO']/turnovers['3.1']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['4.1']['TotalWins'] != 0:
        draw.text((930, 600),(str(int(round((turnovers['4.1']['GSO']/turnovers['4.1']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)

    if turnovers['1.2']['TotalWins'] != 0:
        draw.text((205, 800),(str(int(round((turnovers['1.2']['GSO']/turnovers['1.2']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['2.2']['TotalWins'] != 0:
        draw.text((460, 800),(str(int(round((turnovers['2.2']['GSO']/turnovers['2.2']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['3.2']['TotalWins'] != 0:
        draw.text((730, 800),(str(int(round((turnovers['3.2']['GSO']/turnovers['3.2']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['4.2']['TotalWins'] != 0:
        draw.text((930, 800),(str(int(round((turnovers['4.2']['GSO']/turnovers['4.2']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)

    if turnovers['1.3']['TotalWins'] != 0:
        draw.text((205, 980),(str(int(round((turnovers['1.3']['GSO']/turnovers['1.3']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['2.3']['TotalWins'] != 0:
        draw.text((460, 980),(str(int(round((turnovers['2.3']['GSO']/turnovers['2.3']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['3.3']['TotalWins'] != 0:
        draw.text((730, 980),(str(int(round((turnovers['3.3']['GSO']/turnovers['3.3']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)
    if turnovers['4.3']['TotalWins'] != 0:
        draw.text((930, 980),(str(int(round((turnovers['4.3']['GSO']/turnovers['4.3']['TotalWins']),2)*100))+'%'),(255,255,0),font=font)

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
    data = getSeasonShots()
    img = Image.open(input_file).convert('RGB')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./assets/images/OpenSans-Semibold.ttf", 35)
    # CE1
    draw.text((165, 30),str(data['zone1']['total']),(255,255,255),font=font)
    draw.text((275, 30),(str(int(round((data['zone1']['onTarget']/data['zone1']['total']),2)*100))+'%'),(255,255,255),font=font)
    # CE2
    draw.text((220, 210),str(data['zone2']['total']),(255,255,255),font=font)
    draw.text((330, 210),(str(int(round((data['zone2']['onTarget']/data['zone2']['total']),2)*100))+'%'),(255,255,255),font=font)
    # CE3
    draw.text((555, 450),str(data['zone3']['total']),(255,255,255),font=font)
    draw.text((665, 450),(str(int(round((data['zone3']['onTarget']/data['zone3']['total']),2)*100))+'%'),(255,255,255),font=font)
    # CE4
    draw.text((880, 210),str(data['zone4']['total']),(255,255,255),font=font)
    draw.text((980, 210),(str(int(round((data['zone4']['onTarget']/data['zone4']['total']),2)*100))+'%'),(255,255,255),font=font)
    # CE5
    draw.text((925, 30),str(data['zone5']['total']),(255,255,255),font=font)
    draw.text((1045, 30),(str(int(round((data['zone5']['onTarget']/data['zone5']['total']),2)*100))+'%'),(255,255,255),font=font)
    # Reaction Zone
    draw.text((555, 30),str(data['zone6']['total']),(0,0,0),font=font)
    draw.text((665, 30),(str(int(round((data['zone6']['onTarget']/data['zone6']['total']),2)*100))+'%'),(0,0,0),font=font)

    img.save('./assets_output/' + output_file)

def createAllShotMap():
    createShotMap('ShotMapFor.png', 'Shot Map For.png')
    createShotMap('ShotMapAgainst.png', 'Shot Map Against.png')

def createAllPCShotMap():
    createPCShotMap('PCA.png','PCA Shot Map.png')
    createPCShotMap('PCD.png','PCD Shot Map.png')

createSeasonTurnoverImage()