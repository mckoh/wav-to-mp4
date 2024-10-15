# WAV to MP4 Converter

## Requirements

You can find all relevant python packages in the `requirements.txt`. It is recommendet to use a virtual environment to manage your requirements for this project. Use the following command line prompt to install your requirements.

```sh
# Install virtualenv if it's not already installed
pip install virtualenv

# Create a virtual environment
virtualenv myenv

# Activate the virtual environment
# On Windows
myenv\Scripts\activate
# On Unix or MacOS
source myenv/bin/activate

# Install the dependencies from requirements.txt
pip install -r requirements.txt
```

This will install all necessary components. Make sure to use the virtual environment as your python kernel afterwards, to have access to all these components.

**Important:** One package used in this project requires an additional command line tool called `ffmpeg`. You can directly download this tool from [github](https://github.com/BtbN/FFmpeg-Builds/releases). Make sure to unpack the downloaded archive and add the bin folder of the unpacked archive to your PATH variable. Alternatively, you can place the `ffmpeg.exe` file in the root directory of this repository.

## Use of the tool

The easiest way to use this tool is by starting it with docker. You can build your own cocker image using the `docker_build.sh` file. The Docker container will be named `streamlit_mp4_converter` and will already contain all necessary requirements. Run the container with the following command:

```sh
docker run streamlit_mp4_converter
```

Alternatively, you can run the `streamlit` app locally on your machine. If so, make sure that all requirements are installed (see Requirements) on your local machine. Startup the app by executing the following command on your terminal (open the terminal in the root folder of this repositiory, where `app.py` is located):

```sh
streamlit run app.py
```

In either way, you can access the app using your browser by going to [http://localhost:8501](http://localhost:8501).

>**Note:** The port might be different depending on wether you have already another streamlit app running on your machine. If so, try 8502, 8503 and so fourth.
