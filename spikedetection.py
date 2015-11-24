import matplotlib.pyplot as plt
import numpy

import SDfunctions


class SpikeData:
    def __init__(self, filename):

        self.time, self.voltage, self.lightstim, self.drugstim = SDfunctions.read_spike_train(filename)

    def plotrawdata(self):

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
        pks = []
        trs = []
        a = 0
        b = 0
        d = 0
        x = numpy.asarray(self.voltage)

        # Loop through all indices and find all peaks and all troughs
        for ind in numpy.arange(len(self.voltage)):
            if d == 0:
                if x[a] >= x[ind] + diff:
                    d = 2
                elif x[ind] >= x[b] + diff:
                    d = 1
                if x[a] <= x[ind]:
                    a = ind
                elif x[ind] <= x[b]:
                    b = ind
            elif d == 1:
                if x[a] <= x[ind]:
                    a = ind
                elif x[a] >= x[ind] + diff:
                    pks.append(a)
                    b = ind
                    d = 2
            elif d == 2:
                if x[ind] <= x[b]:
                    b = ind
                elif x[ind] >= x[b] + diff:
                    trs.append(b)
                    a = ind
                    d = 1

        return pks, trs

    def plotpeakdata(self):

        # Populate this part of the code with a method that plots the raw data overlaid with the peaks from peakdetect
        # Hint: you can also try using this with inputs and have two options defined by an if statement:
        #   (1)  var.plotpeakdata(False,pks,trs)  -> in which pks,trs come from peakdetect
        #   (2)  var.plotpeakdata(True)           -> this will call peakdetect to create the variables pks,trs

        plt.plot(self.voltage)

    def findthreshold(self):

        # Create a method that finds an appropriate threshold given your data

        diff = 0

        return diff

    def calculatestats(self):

        #   Now that you have all of the peaks from peakdetect(), try calculating some statistics
        #   You can use the same "if" statement like you did for plotpeakdata(), so that you can
        #   either input pks,trs or you could have it call peakdetect().

        # Try calculating:
        #   (1) mean spike rate
        #   (2) standard deviation of spike rate
        #   (3) coefficient of variation given (1) and (2)
        #   (4) ...and others

        # I would also try making a histogram of the inter-spike intervals if you calculate (1) and (2)

        # You can also try to overlay the stimulus plot with  points or lines that correspond to
        # the peaks or troughs. This allows for easy visualization of the results so that you can
        # compare them with the stimuli.

        plt.plot(self.voltage)


# Run the script
sd = SpikeData('data2.txt')
peaks, troughs = sd.peakdetect(1)
sd.plotrawdata()
print ('The voltage at time ' '%f' ' is ' '%f') % (sd.time[100], sd.voltage[100])
print ('There are ' '%d' ' peaks and ' '%d' ' troughs.') % (len(peaks), len(troughs))
