# My pesonal notes

This notebook stores all my personal notes over my sujects of interest.

# Installation

It is required python 3.6+ installed in the host machine. I recommend the user to create a new python environment with

```bash
$ workon notebook
``` 

On the next step we install all requirement packages to read this notebook:

```bash
$ pip install -r requirements.txt
```

Then we can active plugins with:

```bash
$ bash setup.sh 
```

Note that this last step won't work on windows environment. It is though straighfoward to workaround this issue by executing the commands within `setup.sh`.

Finally we can run the notebook with:

```bash
$ jupyter-notebook &
```
