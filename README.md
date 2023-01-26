# Lexica Aperture API

An unofficial python wrapper for the Lexica Aperture image generation model API.

## Features

You can generate and save images using the Lexica Aperture model with custom prompts. Four `jpg` images are returned after every query and, are saved in your working directory. 

If you wish to modify the source code to fit your requirements, you are open to doing so.

## Important
The console may display several errors such as depreciation warnings or certificate errors. These can simply be overlooked, the program works just fine.

Also, Lexica gives a total of 100 free images to its users so, upon exhaustion of those 100 images, this program won't work either.

Finally, different wait times are given at places in the program. If you feel they need to be changed, you do so by editing the argument in `time.sleep(arg)`

### Installation

Download the source code and copy the function as well as the module imports from `main.py` to your python program. Make sure to install all the dependencies such as selenium and requests. You can also import the program as a module.

### Usage

#### Obtaining a session_token

1. Go to https://lexica.art/aperture and open the developer tools using `F12`.
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://lexica.art/aperture`.
3. Copy the value in the `Cookie Value` field.

![image](https://user-images.githubusercontent.com/87384376/214851010-3ae41c08-6d99-4c2c-8861-c1ae62f21789.jpg)

#### Using the function

The function `img_generate` takes three parameters
1. Your `session_token`, which you obtained from the previous step.
2. Your `email`, the account with which you've signed in to Lexica (I wasn't able to bypass the popup that asks for your email using the session token)
3. Your `prompt`, a prompt for the image you want to generate 

Example:
```img_generate("prompt", session_token, "abc@123.com")```

### How do I use this API on Google Colab?

This script uses a headless version of the selenium webdriver and, Google Colab causes issues in locating elements as well as performing simple tasks on web elements.

Thus, this is still under development.


## Disclaimer

This project is not affiliated with Lexica in any way. Please read the Lexica TOS before using this project.
