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

tbd