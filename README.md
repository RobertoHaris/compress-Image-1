# compress-Image-1
# JPEG Image Compression and Decompression

This Python script is designed for compressing and decompressing images using the JPEG (Joint Photographic Experts Group) image compression algorithm. The JPEG algorithm is widely used for reducing the size of images while maintaining an acceptable level of visual quality. This README provides comprehensive instructions for using the script and a brief overview of its functionality.

## Usage
### Image Compression

To compress an image, execute the `compression.py` script. Ensure that you have installed the required dependencies, such as the Pillow library. The script first resizes the image and then applies the JPEG algorithm for compression. The compressed image will be saved in the file `compressed_image.jpg`.

```bash
python compression.py path_to_image.jpg
```
### Image Decompression
To decompress a previously compressed image, run the `decompression.py` script. The script opens the compressed image `compressed_image.jpg` and restores it to its original size. The decompressed image will be saved in the file `decompressed_image.jpg`.
```bash
python decompression.py
```
## Example
For example, using the image `example.jpg`:
1. Compress the image:
```bash
python compression.py example.jpg
```
2. Decompress the compressed image:
```bash
python decompression.py
```
The decompressed image will be saved as `decompressed_image.jpg`.
## Dependencies
This script utilizes the Pillow Python library for image manipulation. Ensure you install it before running the script.
```bash
pip install Pillow
```
## Author
RobertoHaris
