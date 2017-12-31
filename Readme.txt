Yelp Photo Classification

System Requirements
..........................................
1. Libraries for deep learning- Pytorch
2. Supporting OS-Ubuntu, Windows with Anaconda IDE

Steps to run code
.........................................................
1. Download dataset from Yelp dataset challenge(https://www.yelp.com/dataset/download)
2. Input will be a folder with images and image details in a list of JSON file.

Preprocessing
.........................................................
1. Preprocessing command ->  python preprocessing.py <json file>
2. Output will be out.csv which contains the photoid and label after preprocessing input.

Training
..........................................................
1. For GPU:Command to run-> python convnet-GPU.py --data <directory containing all the images> --label <the out.csv generated in the previous step>
   For CPU:Command to run-> python convnet-CPU.py --data <directory containing all the images> --label <the out.csv generated in the previous step>
2. A trained model training.pt will be generated in the same directory. 


Prediction
...............................................................
1.Create a sample folder with images for prediction
2.Create a csv file which contains photoid of image and its actual label
3.Command to run-> python prediction.py training.pt <images folder for prediction> <csv file which contains photoid and actual labels>
4.Output will be prediction.csv which contains photoid,actual label,predicted labels