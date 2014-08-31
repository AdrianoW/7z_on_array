
# the functions

# dependencies
import numpy as np
import subprocess
from PIL import Image
from re import findall
from os import path
# import skimage.io._plugins.pil_plugin as pp
from StringIO import StringIO

# Offsets of the list returned by 7z
HEADER_OFFSET = 17
FOOTER_OFFSET = -3


def get_files_info(p_file_name):
    """
    Get the zipped files information. Needed to parse data information
    :param p_file_name: 7z file to be read
    :return: array with the files list with dir, no dir and size
    """
    # list all files into memory
    f_list = subprocess.Popen(["7z", "l", p_file_name],
                              stdout=subprocess.PIPE).communicate()[0]

    # convert to line and iterate finding the fields
    f_lines = f_list.split('\n')

    # check if there was an error or apply the offset
    if len(f_lines) < HEADER_OFFSET:
        raise Exception, f_lines[4]
    f_lines = f_lines[HEADER_OFFSET:FOOTER_OFFSET]

    list_fields = []
    for l in f_lines:
        fields = findall("(^.+\.A +)(\d+)( +\d* +)([]\w/.\d]+)", l)
        # check if line is a subfolders or folder
        if len(fields) != 1:
            continue
        f_size = fields[0][1]
        f_name_full = fields[0][3]
        f_name = path.basename(fields[0][3])

        # TODO: come with an id system, based on file name?
        # save fields
        list_fields.append([f_size, f_name_full, f_name])

    return np.array(list_fields)


def get_files_array(p_f_list, p_f_data):
    """
    Uncompress file and split the bytes array according to file sizes
    :param p_f_list: list of files and their sizes
    :param p_f_data: byte stream
    :return: array of arrays with data.
    """
    # beginning and end of each file
    low = 0
    up = 0
    images = [0] *len(p_f_list)

    # get each file from the file
    for i, f in enumerate(p_f_list):
        up += int(f[0])
        # get bytes from the array
        raw_img = p_f_data.data[low:up]
        low = up

        # Convert rawImage to Mat
        pil_image = Image.open(StringIO(raw_img))
        np_image = np.array(pil_image)
        ##np_image = pp.(pil_image)
        images[i] = np_image

    return images


def uncompress_file(p_f_name):
    """
    Decompress file to array
    :param p_f_name: file name
    :return: array with file bytes
    """
    f_data = subprocess.Popen(["7z", "e", "-so", p_f_name],
                              stdout=subprocess.PIPE).communicate()[0]

    return np.array(f_data)


if __name__ == '__main__':
    file_name = '/Users/adrianowalmeida/Documents/Box Sync/Box Sync/DSR/Machine Learning/Kaggle/CIFAR/train.7z'
    f_info = get_files_info(file_name)
    raw_data = uncompress_file(file_name)
    data = get_files_array(f_info, raw_data)

# # get file info inside zip
# p = subprocess.Popen(["7z", "l", "awa.7z"],
#                      stdout=subprocess.PIPE).communicate()[0]
# # uncompress all files
# p = subprocess.Popen(["7z", "e", "-so", "awa.7z"],
#                      stdout=subprocess.PIPE).communicate()[0]
#
# ## separate them individually
# f1 = p[0:2106]
#
#
# # Convert rawImage to Mat
# pilImage = Image.open(StringIO(rawImage));
# npImage = np.array(pilImage)
# matImage = cv.fromarray(npImage)
#
# # return one array with all images
# from skimage.io._plugins.pil_plugin import pil_to_ndarray
#
# def roundtrip_pil_image(self, x):
#         pil_image = ndarray_to_pil(x)
#         y = pil_to_ndarray(pil_image)
#         return y