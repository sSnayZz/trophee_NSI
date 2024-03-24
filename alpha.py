
def alpha_intro(intro_count):
    if intro_count!=None and intro_count>=0 :
        return intro_count-1
    else:
        return
    

intro_count=255
running=True
while running==True:
    intro_count = alpha_intro(intro_count)
    print(intro_count)
    if intro_count==0:
        running=False

