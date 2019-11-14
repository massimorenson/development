from PIL import Image
import numpy as np	


def img2bin(img_px):
    bin_array = np.int_([])
    for i in img_px:
        for j in i:
            if np.array_equal(j,np.array([0,0,0])):
                bin_array=np.append(bin_array,[1])
            else:
                bin_array=np.append(bin_array,[0])
    return bin_array

def generate_training_data():
    img_bin_data_array = np.int_([])
    print(img_bin_data_array.shape)
    for i in range(10):
        for j in range(11):
            path = "Data/"+str(i)+"/"+str(i)+"("+str(j)+").png"
            image = Image.open(path,'r')
            img_px = np.array(image)
            img_bin = img2bin(img_px)
            img_bin_data_array = np.append(img_bin_data_array,img_bin,axis=0) #TODO make new row instead of appending on the same one
     return img_bin_data_array

def generate_output_data():
    #TODO 
    # [0 0 0 0 0 0 0 0 0 0]
    # = indexen zullen de cijfers worden die voorpeld worden
    # [0 1 2 3 4 5 6 7 8 9]
    return ''

if __name__ == "__main__":
    print('generating...')
    training_data=generate_training_data()
    print(training_data.shape)

