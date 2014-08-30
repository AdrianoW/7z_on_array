7z_on_array
===========

Python library to unzip 7z files straight to numpy arrays

this small library has the objective of dealing with .7z files without
the need to extract them to the HD. It uses the 7zip bash program to unzip files
directly into nemory and than convert them to arrays

It is directed to treat the files that were sent on kaggle competition but
it may be changed to deal with other files zipped.


references and places to find help

[http://stackoverflow.com/questions/646286/python-pil-how-to-write-png-image-to-string](Stack post)
[https://docs.python.org/2/library/stringio.html](String io)
[http://stackoverflow.com/questions/11552926/how-to-read-raw-png-from-an-array-in-python-opencv/17547525#17547525](Open cv and raw image)
[http://stackoverflow.com/questions/25186591/having-cv2-imread-reading-images-from-file-objects-or-memory-stream-like-data-h](Memory strings as files)
[http://superuser.com/questions/548349/how-can-i-install-7zip-so-i-can-run-it-from-terminal-on-os-x](how to intall 7zip)