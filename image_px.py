from PIL import Image
import numpy as np	

image = Image.open('Data/1/1.png','r')

px = np.array(image)
print(px.shape)

black_dots=0
bin_array=np.array([])
bin_array=
for i in px:
    for j in i:
        if np.array_equal(j,np.array([0,0,0])):
            black_dots+=1

    
print(black_dots)
print(bin_array)

