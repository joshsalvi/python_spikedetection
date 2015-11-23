import numpy as np
import csv
import matplotlib.pyplot as plt

def read_spike_data(file):
    spike_train = open(file, 'rb')
    data2 = []
    time = []
    voltage = []
    light_stimulus = []
    drug_stimulus = []
    line = spike_train.next()
    print type(spike_train)
    for line in spike_train:
        data = line.split("\t")

        data2.append(data)
    for item in data2:
        time.append(float(item[0]))
        voltage.append(float(item[3]))
        light_stimulus.append(float(item[6]))
        drug_stimulus.append(float(item[7]))

    return time, voltage, light_stimulus, drug_stimulus

t, v, ls, ds = read_spike_data('data3.txt')

def plot_spike(time, voltage, light_stimulus, drug_stimulus):
    plt.clf()
    f, axarr = plt.subplots(2, sharex=True)
    axarr[1].plot(time, voltage)
    axarr[1].set_ylim([-10,10])
    plt.xlabel('Voltage (mV)')
    axarr[1].legend(['spike trace'])
    axarr[0].plot(time, light_stimulus, 'b', time, drug_stimulus, 'r')
    axarr[0].legend(["light stimulus", "acetylcholine"])
    plt.xlabel('Voltage (mV)')
    axarr[0].set_ylim([1,4])
    plt.draw()
    plt.show()
    return

plot_spike(t, v, ls, ds)

# from detect_peaks import detect_peaks
#
# def plot_peaks(x):
#     peaks = detect_peaks(x, mph = 5, mpd = 2, edge = 'rising', valley = 'True', show = 'True')
#
# plot_peaks(v)