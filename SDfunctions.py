def read_spike_train(file):

    spike_train = open(file, 'rb')
    data2 = []
    time = []
    voltage = []
    light_stimulus = []
    drug_stimulus = []
    for line in spike_train:
        data = line.split("\t")

        data2.append(data)
    for item in data2:
        time.append(float(item[0]))
        voltage.append(float(item[3]))
        light_stimulus.append(float(item[6]))
        drug_stimulus.append(float(item[7]))

    return time, voltage, light_stimulus, drug_stimulus
