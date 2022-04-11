<p align="center"><a href="https://github.com/juancrrn/merlin-mobile" target="_blank"><img src="https://juancrrn.io/img/merlin-github-header-rgb-expanded.svg"></a></p>

## About Merlin Classifier

Component: face embedding microservice.

Merlin Desktop is the Merlin project's desktop application AI-based classifier module.

(Under developement).

## Requirements

This module requires the following packages:

- Python 3.8
- Numpy 1.22
- Dlib 19.23
- Face recognition 1.2.2 (https://github.com/ageitgey/face_recognition/)
- Flask 2.1.1

## Python virtual environment

If you are willing to use a Python virtual environment, the `python3.8-venv` package is required. In Ubuntu systems, install it running `$ sudo apt install python3.8-venv`.

Initialize the virtual environment and enter it:

```console
$ python3 -m venv .venv

$ source .venv/bin/activate
```

Once inside the virtual environment, you are ready to install the required packages.

To include globally-installed packages to your virtual environment, use `.pth` files inside your `.venv/lib/python3.8/site-packages` directory. Example:

```console
$ cd .venv/lib/python3.8/site-packages/

$ echo "/usr/local/lib/python3.8/site-packages/cv2" > cv2.pth

$ echo "/usr/local/lib/python3.8/dist-packages/dlib-19.23.0-py3.8-linux-x86_64.egg" > dlib.pth"
```

## Settings

Rename the `config_sample.py` file to `config.py` and set your desired configuration inside it:

- `BASE_DIR`: the base directory of the app.
    - Defaults to `os.path.abspath(os.path.dirname(__file__))`.
- `DATA_DIR`: the Merlin-global data directory.
    - Defaults to `os.path.expanduser("~/Merlin/Data")`.
- `HOST`: the host in which to serve the app.
    - Defaults to `'0.0.0.0'`.
- `PORT`: the port in which to serve the app.
    - Defaults to `49153`.
- `DEBUG` wether to output debug information (`True`) or not (`False`).
    - Defaults to `False`.

## Run

To run in a developement server, use:

```console
$ python run.py
```

## Request

### `/face-embedding/get-face-embedding` (`GET`)

Generate a 128-dimension face embedding of a pre-detected face in an image, specified by a rectangle.

Request parameters:

- `path: string`: path of the image file, relative to `DATA_DIR`.
- `rect_top: integer`: top coordinate of the face rectangle.
- `rect_right: integer`: right coordinate of the face rectangle.
- `rect_bottom: integer`: bottom coordinate of the face rectangle.
- `rect_left: integer`: left coordinate of the face rectangle.

Example request URL: `http://localhost:49153/face-embedding/get-face-embedding?path=test.jpg&rect_top=26&rect_right=125&rect_bottom=74&rect_left=78`.

Example response:

```json
{
    "face_embedding": [
        0.011884365230798721,
        "...",
        -0.009591675363481045
    ]
}
```