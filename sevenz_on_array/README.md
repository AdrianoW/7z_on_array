7z_on_array
===========

Python library to unzip 7z files straight to numpy arrays

this small library has the objective of dealing with .7z files without
the need to extract them to the HD. It uses the 7zip bash program to unzip files
directly into nemory and than convert them to arrays

It is directed to treat the image files that were sent on kaggle competition CIFAR
but it may be changed to deal with other zipped files.

On the first test, if I had to decompress and read each file, it would take 2 hours to complete.

Using this library, it took 1 minute.


### Requirements
7zip bash tool. If you have Anaconda installed, you will have already numpy and pil
[http://superuser.com/questions/548349/how-can-i-install-7zip-so-i-can-run-it-from-terminal-on-os-x](how to intall 7zip)


### references and places to find help

[http://stackoverflow.com/questions/646286/python-pil-how-to-write-png-image-to-string](Stack post)
[https://docs.python.org/2/library/stringio.html](String io)
[http://stackoverflow.com/questions/11552926/how-to-read-raw-png-from-an-array-in-python-opencv/17547525#17547525](Open cv and raw image)
[http://stackoverflow.com/questions/25186591/having-cv2-imread-reading-images-from-file-objects-or-memory-stream-like-data-h](Memory strings as files)


### How to use
Just copy the directory to the same directory where your original code is.

Then:
```
    import 7z_on_array

    file_name = '~/Machine Learning/Kaggle/CIFAR/train.7z'
    f_info = get_files_info(file_name)
    raw_data = uncompress_file(file_name)
    data = get_files_array(f_info, raw_data)
```
