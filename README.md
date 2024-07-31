# User Mannual
1. Get bus voltage data from powerfactory

Open Powerfactory and activate the project you want to run. Import `SimBench2PF_studycaseTimeChangingRun.py` as a script. Excute the script then you can get the data `bus_voltage.csv`. You can change the running steps in `time_steps`.

2. Compare the pandapower data with the powerfacotry data

Open `pandapower vs. powerfactory on simbench.ipynb`, make sure `bus_voltage.csv` is in the same directory. Run all the cells. You can get the final results in the last cell. Make sure `time_steps` is as same as with the one we used in the last script.
