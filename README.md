# Quebec Covid QR code Reader
Read and present in a human readable format the content of the COVID QR code using a simple python program.

## Sources
My main source of information on how to read the QR code: [Mikkel Paulson blog](https://mikkel.ca/blog/digging-into-quebecs-proof-of-vaccination/)

## How to use
The QR code must read with another tool. My code simply translate the raw text data contained in the QR code to a human readable format. To use it save the content of the QR code to a text file and feed that text file as the argument when calling the script.
You can use a website like [zxing.org](https://zxing.org/w/decode.jspx) to extract the text data from the QR code image.

```
python3 vaxqr_reader.py <QR_code_text_data.txt>
```

## Requirements
- Python3

### packages
Install the following via pip3:
- jwcrypto
- zlib
