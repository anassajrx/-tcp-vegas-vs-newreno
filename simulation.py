import matplotlib.pyplot as plt

# Données pour TCP New Reno
time_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
generated_packets = [15881, 32155, 48279, 64493, 80750, 96996, 113240, 129509, 145778, 162058, 178148, 194083, 210334, 226297, 242512]
lost_packets = [245, 365, 501, 655, 775, 942, 1050, 1193, 1318, 1473, 1581, 1719, 1856, 2012, 2116]

# Calcul du taux de perte de paquets en pourcentage
packet_loss_rate = [(lost / generated) * 100 for lost, generated in zip(lost_packets, generated_packets)]

# Tracer la courbe pour le taux de perte de paquets en fonction du temps
plt.plot(time_values, packet_loss_rate, label='TCP New Reno')

# Ajouter de titres et de légendes
plt.title('Packet Loss Rate over Time for TCP New Reno')
plt.xlabel('Time')
plt.ylabel('Packet Loss Rate (%)')

# Afficher le graphique
plt.grid(True)
plt.show()
