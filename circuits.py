import fastf1
from matplotlib import pyplot as plt
import numpy as np

jaar = input("Kies jaartal: ")
jaar = int(jaar)
gp = input("Kies Grand Prix: ")
sessie = input("Kies een sessie: ")
ronde = input("Kies een ronde: ")
ronde = int(ronde)
coureur = input("Kies een coureur: ")
coureur2 = input("Kies een coureur tweede: ")
getal = input("Welke bocht?")

session = fastf1.get_session(jaar, gp, sessie)
session.load()

circuit_info = session.get_circuit_info()
lap = session.laps.pick_driver(coureur).pick_lap(ronde)
pos = lap.get_pos_data()
car_data = lap.get_car_data().add_distance()
corner_margin = 50

fig, ax = plt.subplots(figsize=(10, 5), facecolor="white")

def rotate(xy, *, angle):
    rot_mat = np.array([[np.cos(angle), np.sin(angle)],
                        [-np.sin(angle), np.cos(angle)]])
    return np.matmul(xy, rot_mat)

track = pos.loc[:, ('X', 'Y')].to_numpy()
track_angle = circuit_info.rotation / 180 * np.pi
offset_vector = [500, 0]
rotated_track = rotate(track, angle=track_angle)
plt.plot(rotated_track[:, 0], rotated_track[:, 1], color='tab:orange')

for _, corner in circuit_info.corners.iterrows():
    # Create a string from corner number and letter
    txt = f"{corner['Number']}{corner['Letter']}"

    # Convert the angle from degrees to radian.
    offset_angle = corner['Angle'] / 180 * np.pi

    # Rotate the offset vector so that it points sideways from the track.
    offset_x, offset_y = rotate(offset_vector, angle=offset_angle)

    # Add the offset to the position of the corner
    text_x = corner['X'] + offset_x
    text_y = corner['Y'] + offset_y

    # Rotate the text position equivalently to the rest of the track map
    text_x, text_y = rotate([text_x, text_y], angle=track_angle)

    # Rotate the center of the corner equivalently to the rest of the track map
    track_x, track_y = rotate([corner['X'], corner['Y']], angle=track_angle)

    # Draw a circle next to the track.
    plt.scatter(text_x, text_y, color="black", s=140)

    # Draw a line from the track to this circle.
    plt.plot([track_x, text_x], [track_y, text_y], color="green")

    # Finally, print the corner number inside the circle.
    plt.text(text_x, text_y, txt,
             va='center_baseline', ha='center', size='small', color="orange")

plt.show()


for _, corner in circuit_info.corners.iterrows():
    # Extract data specific to the current corner
    corner_distance = corner['Distance']
    corner_number = f"{corner['Number']}{corner['Letter']}"

    if corner_number == getal:
        fig, ax = plt.subplots()
        ax.plot(car_data['Distance'], car_data['Speed'],
                color="green", label=lap['Driver'])
        session = fastf1.get_session(jaar, gp, sessie)
        session.load()
        lap2 = session.laps.pick_driver(co sureur2).pick_lap(ronde)
        car_data2 = lap2.get_car_data().add_distance()
        ax.plot(car_data2['Distance'], car_data2['Speed'],
                color="blue", label=lap['Driver'])

        # Define x-axis limits centered around the corner
        ax.set_xlim(corner_distance - corner_margin, corner_distance + corner_margin)

        # Draw vertical line at the current corner
        ax.axvline(x=corner_distance, linestyle='dotted', color='grey')

        # Display corner number below the vertical line
        ax.text(corner_distance, car_data['Speed'].min() - 30, corner_number,
                va='center_baseline', ha='center', size='small')

        ax.set_xlabel('Afstand in meters')
        ax.set_ylabel('Snelheid in km/h')

        ax.legend()
        plt.show()

    else:
        continue


