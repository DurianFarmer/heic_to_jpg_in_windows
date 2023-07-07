# HEIC to JPG in Windows

This code converts HEIC(or HEIF) image files to JPG using Windows OS.
In general, HEIC extention is not readable in Windows.
The below code allows Pillow to open HEIC files.

```py
pillow_heif.register_heif_opener() # to open heif files in Windows
```

The rest of the code is trivial.