# JPG to DICOM
[This short snippet](https://github.com/jwitos/JPG-to-DICOM/blob/master/jpeg-to-dicom.py) will allow you to save JPG (PNG, BMP) files as DICOM.

Output DCMs should be possible to open in major DICOM viewers. They can also be stored in e.g. Orthanc.

This is a minimalistic approach, so only most important meta tags related to DICOM display are saved. You can easily add them, however, inside the code.

By default, this code has SOP Class set as `1.2.840.10008.5.1.4.1.1.1.1` (Digital X-Ray). If snippet doesn't work for you, try changing this value to a [different SOP Class code](http://dicom.nema.org/dicom/2013/output/chtml/part04/sect_B.5.html).

# Requirements
* pydicom
* numpy
* PIL

# Tested use cases
* Chest X-ray JPG, PNG, BMP photos to DICOM
* Color JPG, PNG, BMP photos to DICOM
* Storage of generated DICOMs in Orthanc
