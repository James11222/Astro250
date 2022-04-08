# Machine Learning

This homework focuses on neural networks for supervised and deep learning. The homework also touches on auto-encoders which are incredibly useful tools for data analysis.

All relavant info is in `HW6.ipynb`. I wrote this notebook in Google Colab to make use of the GPU runtime feature. This GPU runtime feature allowed for training the CNN in reasonable time. The notebook should work running from start to finish. I don't include saved models and logs here due to memory storage concerns but each model should generate as intended when running the notebook from start to finish.

Furthermore, I made a note about using Conv2D vs. Conv3D in the notebook. With the extra 24 Hour extension, I investigated this just to make sure there wasn't a significant improvement in accuracy between the two CNNs. I found that the Conv3D accuracy is approximately the same when simply replacing Conv2D with Conv3D. Also based on updates from the discord, I wanted to clarify that in the Autoencoder problem, the CNN I used to compare the random forest method was actually the base CNN we did in class. I used this model structure as a starting point for the Galaxy classifier as well.
