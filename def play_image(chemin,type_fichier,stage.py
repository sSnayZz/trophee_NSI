def play_image(chemin,type_fichier,stage,exceed):
    stage+=1
    if stage>=exceed+1:
        stage=0
    return [chemin+str(stage)+type_fichier,stage]
 
stage=0
running=True

while running:
    print(play_image("chemin",".png",stage,10)[1])
    stage=play_image("chemin",".png",stage,10)[1]
    a=input('tesdt:::::')
