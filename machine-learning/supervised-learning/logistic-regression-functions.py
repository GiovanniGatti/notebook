import os
import tarfile
from tempfile import TemporaryDirectory
import numpy as np
from google_drive_downloader import GoogleDriveDownloader as gdd
import icontract
import pylab

@icontract.ensure(lambda result: result[0].shape[0] == result[1].size)
def load_dataset():
    with TemporaryDirectory() as tmpdir:
        targz_path = os.path.join(tmpdir, "logistic-regression-data.tar.gz")

        gdd.download_file_from_google_drive(
            file_id='1ZfyFgzkZYxtA_O5zv4Y7oEIBAdlE4p1N', dest_path=str(targz_path))

        tar = tarfile.open(targz_path)
        tar.extractall(path=str(tmpdir))
        tar.close()

        x_dat = os.path.join(tmpdir, "logistic-regression-data", "x.dat")
        X = np.fromfile(file=str(x_dat), dtype=np.dtype('float64'), sep=" ").reshape((-1, 2))
        
        y_dat = os.path.join(tmpdir, "logistic-regression-data", "y.dat")
        y = np.fromfile(file=str(y_dat), dtype=np.dtype('float64'), sep=" ").reshape((-1))

        return X, y

@icontract.require(lambda X: X.shape[1] == 2)
@icontract.require(lambda X, y: X.shape[0] == len(y))
def plot(X, y, lwlr):
    res=50
    plot_pos = 0
    for tau in (0.01, 0.05, 0.1, 0.5, .5, 5):
        print(tau.type)
        query_x = np.zeros(X.shape[1])
        query_points_x = np.zeros((res, res))
        query_points_y = np.zeros((res, res))
        predicted_y = np.zeros((res, res))
        for i in range(1, res):
            for j in range(1, res):
                query_x[0] = 2*(i-1)/(res-1)-1
                query_x[1] = 2*(j-1)/(res-1)-1
                predicted_y[j][i] = lwlr(X, y, query_x, tau)
                query_points_x[j][i] = query_x[0]
                query_points_y[j][i] = query_x[1]

        pylab.subplot(2, 3, plot_pos)
        plot_pos += 1
        pylab.pcolormesh(query_points_x, query_points_y, predicted_y)
        pylab.plot(X[y==1][:,0], X[y==1][:,1], linestyle='None', color='black', marker='x')
        pylab.plot(X[y==0][:,0], X[y==0][:,1], linestyle='None', color='black', marker='o')
