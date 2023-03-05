# Import everything needed to edit video clips 
from moviepy.editor import *
    
# loading video dsa gfg intro video 
clip = VideoFileClip("out1.mp4") 
     
# getting only first 5 seconds 
clip = clip.subclip(65, 72) 
  
# cutting out some part from the clip
#clip = clip.cutout(3, 10)
  
# showing  clip 
clip.ipython_display(width = 360)
