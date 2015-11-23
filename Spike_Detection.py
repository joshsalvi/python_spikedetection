import matplotlib.pyplot as plt
import numpy

import SDfunctions


class SpikeData:
    def __init__(self, file):

        self.time, self.voltage, self.lightstim, self.drugstim = SDfunctions.read_spike_train(file)

    def plotdata(self):

        # Set up figure and plot the spikes and stimuli with appropriate legends
        plt.clf()
        f, axarr = plt.subplots(2, sharex=True)
        axarr[1].plot(self.time, self.voltage)
        axarr[1].set_ylim([-10, 10])
        plt.xlabel('Voltage (mV)')
        axarr[1].legend(['spike trace'])
        axarr[0].plot(self.time, self.lightstim, 'b', self.time, self.drugstim, 'r')
        axarr[0].legend(["light stimulus", "acetylcholine"])
        plt.xlabel('Voltage (mV)')
        axarr[0].set_ylim([1, 4])
        plt.draw()
        plt.show()

        return

    def peakdetect(self, diff):

        # Initialize variables
        maxt = []
        mint = []
        x = numpy.arange(len(self.voltage))
        voltage = numpy.asarray(self.voltage)
        mn, mx = numpy.Inf, -numpy.Inf
        mnpos, mxpos = numpy.NaN, numpy.NaN
        maxl = True

        for ind in numpy.arange(len(voltage)):
            this = voltage[ind]
            if maxl:
                if this < mx - diff:
                    mint.append((mxpos, mx))
                    mn = this
                    mnpos = x[ind]
                    maxl = False
            else:
                if this > mn + diff:
                    maxt.append((mnpos, mn))
                    mx = this
                    mxpos = x[ind]
                    maxl = True
        self.maxt = numpy.array(maxt)
        self.mint = numpy.array(mint)

        return self.maxt, self.mint


sd = SpikeData('data2.txt')
sd.plotdata()
pks, trs = sd.peakdetect(1)
print ('The voltage at time ' '%f' ' is ' '%f') % (sd.time[100], sd.voltage[100])
