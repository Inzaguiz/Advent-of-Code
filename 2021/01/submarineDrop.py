with open("2021/01/input.txt", "r") as f:
    measurements = []
    trioMeasurements = []
    nbIncrement = 0
    for line in f:
        measurements.append(int(line))
    for A, B, C in zip(measurements, measurements[1:], measurements[2:]):
            trioMeasurements.append(A + B + C)
    for previous, current in zip(trioMeasurements, trioMeasurements[1:]): 
        if previous < current:
            nbIncrement+=1
    else: 
        print(nbIncrement)