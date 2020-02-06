# JPG-to-DICOM
[This short snippet](https://github.com/jwitos/JPG-to-DICOM/blob/master/jpeg-to-dicom.py) will allow you to save JPG (PNG, BMP) files as DICOM.

Output DCMs should be possible to open in major DICOM viewers. They can also be stored in e.g. Orthanc.

This is a minimalistic approach, so only most important meta tags related to DICOM display are saved. You can easily add them, however, inside the code.

# Requirements
* pydicom
* numpy
* PIL
