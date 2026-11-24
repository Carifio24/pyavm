TIFF_LE = b"II*\x00"  # Little-endian (49 49 2A 00)
TIFF_BE = b"MM\x00*"  # Big-endian    (4D 4D 00 2A)

TIFF_SIGNATURES = (TIFF_LE, TIFF_BE)


def is_tiff(filename):
    with open(filename, "rb") as f:
        header = f.read(4)
    return header in TIFF_SIGNATURES


class TIFFChunk:
    @classmethod
    def read(cls, fileobj):
        self = cls()

        
