import matplotlib.pyplot as plt

# Données pour TCP New Reno
time_values_reno = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
generated_packets_reno = [16176, 32809, 49403, 66026, 82420, 98865, 115503, 132159, 148687, 165284, 181668, 198273, 214892, 231394, 247903]
lost_packets_reno = [103, 156, 206, 260, 315, 371, 422, 482, 537, 592, 650, 711, 764, 819, 875]

# Calcul du taux de perte de paquets en pourcentage pour TCP New Reno
packet_loss_rate_reno = [(lost / generated) * 100 for lost, generated in zip(lost_packets_reno, generated_packets_reno)]

# Données pour l'autre ensemble de valeurs
time_values_other = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
generated_packets_other = [15881, 32155, 48279, 64493, 80750, 96996, 113240, 129509, 145778, 162058, 178148, 194083, 210334, 226297, 242512]
lost_packets_other = [245, 365, 501, 655, 775, 942, 1050, 1193, 1318, 1473, 1581, 1719, 1856, 2012, 2116]

# Calcul du taux de perte de paquets en pourcentage pour l'autre ensemble de valeurs
packet_loss_rate_other = [(lost / generated) * 100 for lost, generated in zip(lost_packets_other, generated_packets_other)]

# Tracer les courbes pour le taux de perte de paquets en fonction du temps
plt.plot(time_values_reno, packet_loss_rate_reno, label='TCP New Reno')
plt.plot(time_values_other, packet_loss_rate_other, label='Autre ensemble de valeurs')

# Afficher les valeurs pour TCP New Reno
for i, txt in enumerate(lost_packets_reno):
    plt.annotate(txt, (time_values_reno[i], packet_loss_rate_reno[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Afficher les valeurs pour l'autre ensemble de valeurs
for i, txt in enumerate(lost_packets_other):
    plt.annotate(txt, (time_values_other[i], packet_loss_rate_other[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Ajouter de titres et de légendes
plt.title('Packet Loss Rate over Time')
plt.xlabel('Time')
plt.ylabel('Packet Loss Rate (%)')
plt.legend()

# Afficher le graphique
plt.grid(True)
plt.show()
