# IMPORT REQUIRED LIBRARIES
import pandas as pd                 # For reading and handling CSV files
import matplotlib.pyplot as plt     # For plotting data
import numpy as np                  # For numerical operations

# DEFINE GAIN SETS
gain_sets = [
    {"k_rho": 2.0, "k_alpha": 5.0, "k_beta": -1.5}, # k_rho > 0, k_alpha - k_rho > 0, k_beta < 0 (Controller Law for Control Design)
    {"k_rho": 1.0, "k_alpha": 4.0, "k_beta": -1.0}, # k_rho > 0, k_alpha - k_rho > 0, k_beta < 0 (Controller Law for Control Design)
    {"k_rho": 0.5, "k_alpha": 3.0, "k_beta": -0.5}, # k_rho > 0, k_alpha - k_rho > 0, k_beta < 0 (Controller Law for Control Design)
]

# DEFINE FILE PATHS FOR CSV FILES GENERATED FROM SIMULATION
csv_files = ['simdata/Nominal/Init_angle_1.57_seed_1_Nactor_10/3wrobotNI_Nominal_2025-06-22_17h52m11s__run01.csv', '/home/gouransh/Desktop/Control Assignment/rcognita-edu-main/simdata/Nominal/Init_angle_1.57_seed_1_Nactor_10/3wrobotNI_Nominal_2025-06-22_17h32m42s__run01.csv', '/home/gouransh/Desktop/Control Assignment/rcognita-edu-main/simdata/Nominal/Init_angle_1.57_seed_1_Nactor_10/3wrobotNI_Nominal_2025-06-22_17h35m33s__run01.csv']

# DEFINE COLORS FOR EACH RUN
colors = ['red', 'blue', 'green']

# FUNCTION TO READ CSV WHILE SKIPPING METADATA COMMENTS
def smart_read_csv(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # Identify the header line (starts with "t [s],")
    for i, line in enumerate(lines):
        if line.startswith("t [s],"):
            header_index = i
            break
    return pd.read_csv(file_path, skiprows=header_index)

# PLOT 1: ROBOT TRAJECTORY VS REFERENCE (x vs y)
plt.figure(figsize=(8, 6))
for i, (file, color) in enumerate(zip(csv_files, colors), start=1):
    data = smart_read_csv(file)
    data.columns = [col.strip() for col in data.columns]

    # Plot the actual robot trajectory
    plt.plot(data['x [m]'], data['y [m]'], label=f'Run {i}', color=color)

plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Robot Trajectories (Kinematic Controller)')
plt.legend()
plt.grid(True)
plt.axis('equal')  # x-y plot, so equal scaling makes sense
plt.savefig('simdata/Robot_Trajectories_Kinematics.png')
plt.close()

# PLOT 2: LINEAR VELOCITY v(t)
plt.figure(figsize=(8, 6))
for i, (file, color) in enumerate(zip(csv_files, colors), start=1):
    data = smart_read_csv(file)
    data.columns = [col.strip() for col in data.columns]

    # Plot v [m/s] over time
    plt.plot(data['t [s]'], data['v [m/s]'], label=f'Run {i}', color=color)

plt.xlabel('t [s]')
plt.ylabel('v [m/s]')
plt.title('Linear Velocity Over Time')
plt.legend()
plt.grid(True)
plt.savefig('simdata/Linear_Velocity_Kinematics.png')
plt.close()

# PLOT 3: ANGULAR VELOCITY omega(t)
plt.figure(figsize=(8, 6))
for i, (file, color) in enumerate(zip(csv_files, colors), start=1):
    data = smart_read_csv(file)
    data.columns = [col.strip() for col in data.columns]

    # Plot omega [rad/s] over time
    plt.plot(data['t [s]'], data['omega [rad/s]'], label=f'Run {i}', color=color)

plt.xlabel('t [s]')
plt.ylabel('omega [rad/s]')
plt.title('Angular Velocity Over Time')
plt.legend()
plt.grid(True)
plt.savefig('simdata/Angular_Velocity_Kinematics.png')
plt.close()

# PLOT 4: TRACKING ERROR VS TIME (Using fixed goal)
plt.figure(figsize=(8, 6))

# Define your fixed goal location (set your actual goal here)
x_goal, y_goal = 0.0, 0.0

for i, (file, color) in enumerate(zip(csv_files, colors), start=1):
    data = smart_read_csv(file)
    data.columns = [col.strip() for col in data.columns]

    # Compute distance to fixed goal at every time step
    error = np.sqrt((data['x [m]'] - x_goal)**2 + (data['y [m]'] - y_goal)**2)

    # Plot tracking error over time
    plt.plot(data['t [s]'], error, label=f'Run {i}', color=color)

plt.xlabel('t [s]')
plt.ylabel('Tracking Error [m]')
plt.title('Tracking Error Over Time')
plt.legend()
plt.grid(True)
plt.savefig('simdata/Tracking_Error_Over_Time.png')
plt.close()
# PRINT SUCCESS MESSAGE
print("Plots Saved:")
print("  • Robot_Trajectories_Kinematics.png")
print("  • Linear_Velocity_Kinematics.png")
print("  • Angular_Velocity_Kinematics.png")
print("  • Tracking_Error_Over_Time.png")