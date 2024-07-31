
import powerfactory as pf
import os
import csv
from datetime import datetime

# ===== Calculate the seconds for setting the studycase time in PF =====
starttime = datetime(1970, 1, 1, 0, 0, 0)
timeprofiletime = datetime(2016, 1, 1, 0, 0, 0)
diff_seconds = (timeprofiletime-starttime).total_seconds()-3600

# ===== Get the current PF-Application =====
app = pf.GetApplication()
if app is None:
    raise Exception("Getting PowerFactory application failed.")
user = app.GetCurrentUser()
project = app.GetActiveProject()
if project is None:
    raise Exception("No project activated. Python Importscript stopped.")
script = app.GetCurrentScript()

# Get Study Case
study_case = app.GetActiveStudyCase()

# Set Study Case Time
import datetime
import pandas as pd
time_steps = 500
columns = [bus.loc_name for bus in app.GetCalcRelevantObjects('*.ElmTerm')]
df = pd.DataFrame(columns=columns)

for time_step in range(time_steps):
    target_time = datetime.datetime(2016, 1, 1, 0, 0) + datetime.timedelta(minutes=15*time_step)
    epoch = datetime.datetime(1970, 1, 1)
    seconds_since_epoch = (target_time - epoch).total_seconds()
    study_case.SetStudyTime(seconds_since_epoch)

    # Load flow
    load_flow = app.GetFromStudyCase('ComLdf')
    load_flow.iopt_net = 0
    load_flow.Execute()

    # Get all the buses
    buses = app.GetCalcRelevantObjects('*.ElmTerm')

    # Export all the buses voltages
    voltage_data = {}
    for bus in buses:
        voltage = bus.GetAttribute('m:u')  # get the bus voltage
        voltage_data[bus.loc_name] = voltage
    # df = df.append(voltage_data, ignore_index=True)
    row_df = pd.DataFrame([voltage_data])
    df = pd.concat([df, row_df], ignore_index=True)

df.to_csv('bus_voltages.csv', index=False)
