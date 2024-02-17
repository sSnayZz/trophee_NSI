def play_image(chemin,type_fichier,stage,exceed):
    stage+=1
    if stage>=exceed:
        stage=0
    return [chemin+str(stage)+type_fichier,stage]
 
stage=0
running=True

while running:
    print(play_image("test_anim/img_",".jpg",stage,10)[0])
    stage=play_image("chemin",".png",stage,3)[1]
    a=input('tesdt:::::')
