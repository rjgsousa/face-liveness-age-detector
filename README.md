# FLAD: Face Liveness and Age Detector

## Preview

[![A preview](https://i9.ytimg.com/vi/MsdsNgzFpyY/mqdefault.jpg?sqp=CPjK2bAG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgTShIMA8=&rs=AOn4CLBfBurRU5_JOnn5hsFLKVNaRRjFRA)](https://youtu.be/MsdsNgzFpyY  "A preview")

## Requirements

### For insightface approach

Install cuda requirements
```bash
sudo apt install nvidia-cudnn libcublas11 libcublaslt11
```

## Reproducibility

1. Create a conda environment
```bash
conda create -n FLAD python=3.10
conda activate FLAD
```
2. Install project with `make run-experiment-standalone`

3. Results will be displayed as it processes the video 

## Documentation

To generate the documentation file, you first are required to have the LaTeX suite installed in our system.

1. Install the TexLive base
```bash 
sudo apt-get install texlive-latex-base
```

2. Also, it is recommended to install the recommended and extra fonts.
```bash
sudo apt install texlive-fonts-recommended
sudo apt install texlive-fonts-extra
sudo apt install latexmk
```

You must have the project installed. For that, it is suggested to have a conda environment:
```bash
conda create -n FLAD python=3.10
conda activate FLAD
```
Then, install "poetry" (tested with 1.8.2) and "sphinx": 
```bash
pip install -U sphinx
pip install poetry==1.8.2
make install
```

Then, at the root folder of the project `$ make documentation`

## Acknowledgements 

- https://sefiks.com/2020/09/07/age-and-gender-prediction-with-deep-learning-in-opencv/
- https://insightface.ai/