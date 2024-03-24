
def alpha_intro(intro_count):
    if intro_count!=100 and intro_count!=None:
        return intro_count+1
    else:
        return
    

intro_count=0
running=True
while running==True:
    intro_count = alpha_intro(intro_count)
    print(intro_count)
    if intro_count==100:
        running=False

