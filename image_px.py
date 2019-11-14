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
    img_bin_data_array = np.empty((0,784), int) # np.int_([])
    print(img_bin_data_array.shape)
    for i in range(10):
        for j in range(11):
            path = "Data/"+str(i)+"/"+str(i)+"("+str(j)+").png"
            image = Image.open(path,'r')
            img_px = np.array(image)
            img_bin = img2bin(img_px)
            img_bin_data_array = np.append(img_bin_data_array,np.array([img_bin]),axis=0)
    return img_bin_data_array

def generate_output_data():
    # [0 0 0 0 0 0 0 0 0 0]
    # = indexen zullen de cijfers worden die voorpeld worden
    # [0 1 2 3 4 5 6 7 8 9]
    zero = np.array([1,0,0,0,0,0,0,0,0,0])
    one =  np.array([0,1,0,0,0,0,0,0,0,0])
    two =  np.array([0,0,1,0,0,0,0,0,0,0])
    three =np.array([0,0,0,1,0,0,0,0,0,0])
    four = np.array([0,0,0,0,1,0,0,0,0,0])
    five = np.array([0,0,0,0,0,1,0,0,0,0])
    six =  np.array([0,0,0,0,0,0,1,0,0,0])
    seven =np.array([0,0,0,0,0,0,0,1,0,0])
    eight =np.array([0,0,0,0,0,0,0,0,1,0])
    nine = np.array([0,0,0,0,0,0,0,0,0,1])

    digits = [zero, one, two, three, four, five, six, seven, eight, nine]

    sol_data = np.empty((0,10), int)
    for digit in digits:
        for i in range(11):
            sol_data = np.append(sol_data, np.array([digit]), axis=0)
    return sol_data

if __name__ == "__main__":
    print('generating... fase1')
    training_data=generate_training_data()
    print(training_data.shape)
    print('generating... fase2')
    output_data = generate_output_data()
    print(output_data.shape)





