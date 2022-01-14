1. Data preparation
To check the operation of the model, you need to prepare an excel file in which the following drilling parameters will be present:
Depth, Bit position, Bit diameter, Borehole diameter, CSGO 1, Topping up, Rotations, Asset amount. containers, Fur. cp speed, Working capacity. 1, VH temperature, Working capacity. 2, Weight on cr, Pressure, Position of cr, Density on vh, Density on vh, Nagr. On the chisel, The temperature of the output, the Lithology code, the stratigraphy code, the complication code
If any of these parameters are missing from the data, the neural network will not work. If the complication code is unknown, then you can simply add an empty column with that name to the excel file. Other parameters may be present in the data, but they will be discarded during the network operation check. When training the network, the lithology codes and stratigraphy codes specified in the files in the Data folder were used. If there are codes in the data that differ from the codes in these files, then the neural network will not work. The prepared data should be put in the Data folder.
2. Checking the model
At the moment, 2 types of networks are available for verification: the first predicts the presence of complications at a given point in depth, and the second predicts complications 10 steps ahead in depth. The code for checking the operation of networks is in the Code folder (the RNN_test file corresponds to the first type of networks, and RNN_test_for_future_errors to the second). When you try to open one of the files, the browser will automatically redirect you to the site colab.google.com . On this site, all code will be executed in the cloud with the ability to connect a GPU to speed up the neural network. The code that opens consists of separate cells that can be executed separately from each other by pressing the arrow:
First you need to execute the first cell of the laptop. In this cell, the newest version of NumPy is installed, which is necessary for the code to work. After executing this code, you need to restart the runtime. To do this, select in the tabs above: Runtime -> Restart the Runtime and click Ok in the window that appears. Next, you need to perform a cell with a Google drive connection. When executing the code, a link will appear that you need to follow:
When you click on the link, a window opens with a selection of accounts. You need to select an Amirig ML account and log in, after which the code will appear:
It needs to be copied to the "Enter your authorization code" field:”. After executing the code, the following state should be observed:
In the next cell, specify the name of the data file, which is located in the Data folder. After that, you need to run all the data preprocessing code. The code can be executed sequentially by pressing the arrow in each cell or all the necessary code at once by pressing the button:
Next, you need to run all the code in the sections Loading the model, Generating a dataset from data, and Testing the model. After that, you can visualize the prediction of the network. If you want to save the visualization, then you need to set the value of the save_fig variable to True. In the case of a network predicting future complications, it is still necessary to specify which of the graphs (10 graphs are being built separately for predicting n steps ahead, where n varies from 1 to 10) to save. In this case, a file with the name that matches the name of the data file will be written to the Data/Prediction_vis folder.
 Colab https://colab.research.google.com/drive/1I4zKvZe7223Gq4fBUeix09vPqInjab4m?usp=sharing