import pydicom
from pydicom.dataset import Dataset, FileDataset
from pydicom.uid import generate_uid
from PIL import Image
import numpy
import uuid

# Your input file here
INPUT_FILE = ##########

# Name for output DICOM
dicomized_filename = str(uuid.uuid4()) + '.dcm'

# Load image with Pillow
img = Image.open(INPUT_FILE)
width, height = img.size
print("File format is {} and size: {}, {}".format(img.format, width, height))

# Convert PNG and BMP files
if img.format == 'PNG' or img.format == 'BMP':
    img = img.convert('RGB')

# Convert image modes (types/depth of pixels)
# Docs: https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html
if img.mode == 'L':
    np_frame = ds.PixelData = np_frame.tobytes()
elif img.mode == 'RGBA' or img.mode == 'RGB':
    np_frame = numpy.array(img.getdata(), dtype=numpy.uint8)
else:
    print("Unknown image mode")
    return

# Create DICOM from scratch
ds = Dataset()
ds.file_meta = Dataset()
ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian
ds.file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.1.1'
ds.file_meta.MediaStorageSOPInstanceUID = "1.2.3"
ds.file_meta.ImplementationClassUID = "1.2.3.4"

ds.PatientName = 'Created'

ds.Rows = img.height
ds.Columns = img.width
ds.PhotometricInterpretation = "YBR_FULL_422"
if np_frame.shape[1] == 3:
    ds.SamplesPerPixel = 3
else:
    ds.SamplesPerPixel = 1
ds.BitsStored = 8
ds.BitsAllocated = 8
ds.HighBit = 7
ds.PixelRepresentation = 0
ds.PlanarConfiguration = 0
ds.NumberOfFrames = 1

ds.SOPClassUID = generate_uid()
ds.SOPInstanceUID = generate_uid()
ds.StudyInstanceUID = generate_uid()
ds.SeriesInstanceUID = generate_uid()

ds.PixelData = np_frame

ds.is_little_endian = True
ds.is_implicit_VR = False

ds.save_as(dicomized_filename, write_like_original=False)
