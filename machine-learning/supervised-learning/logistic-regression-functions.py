import os
import tarfile
from tempfile import TemporaryDirectory
import numpy as np
from google_drive_downloader import GoogleDriveDownloader as gdd


def load_dataset():
    with TemporaryDirectory() as tmpdir:
        targz_path = os.path.join(tmpdir, "logistic-regression-data.tar.gz")

        gdd.download_file_from_google_drive(
            file_id='1ZfyFgzkZYxtA_O5zv4Y7oEIBAdlE4p1N', dest_path=str(targz_path))

        tar = tarfile.open(targz_path)
        tar.extractall(path=str(tmpdir))
        tar.close()

        x_dat = os.path.join(tmpdir, "logistic-regression-data", "x.dat")
        X = np.fromfile(file=str(x_dat), dtype=np.dtype('d'), sep=" ").reshape((-1, 2))
        
        y_dat = os.path.join(tmpdir, "logistic-regression-data", "y.dat")
        y = np.fromfile(file=str(y_dat), dtype=np.dtype('d'), sep=" ").reshape((-1))
        return X, y