import os, sys, time, csv
csv_Directory = r"CSV directory with all the csv files in it"

#Global Variables
rowcapture_dic = {}
rowcapture_list = []

def checkcsvforheaders(csvdirectory):
    for filename in os.listdir(csvdirectory):
        print filename
        with open(csv_Directory + "\\" + filename) as csvfile:
            reader = csv.DictReader(csvfile, dialect='excel')
            for row in reader:
                # format is row['header name']
                print(row['Observation Period'])
                print(row['Observation Period Timestamp'])
                print(row['Pin ID'])
                print(row['Pin Type'])
                print(row['X'])
                print(row['Y'])
                print(row['Rotation'])
                print(row['Actor Type'])
                print(row['Actor Type Other'])
                print(row['Interaction Instances'])
                print(row['Interactions'])
                print(row['Observation Period Comments'])
                print(row['Observation ID'])
                print(row['Observation Timestamp'])
                print(row['Posture Type'])
                print(row['Observation Devices'])
                print(row['Observation Comments'])

def copylines(csvdirectory):
    ObservationPeriod = ''
    ObservationTimestamp = ''
    PinID = ''
    PinType = ''
    Xrow = ''
    Yrow = ''
    ActorType = ''
    ActorTypeOther = ''
    InteractionInstances = ''
    Interactions = ''
    ObservationPeriodComments = ''
    ObservationID = ''
    ObservationTimestamp = ''
    PostureType = ''
    ObservationDevices = ''
    ObservationComments = ''
    for filename in os.listdir(csvdirectory):
        print "Capturing " + filename
        with open(csv_Directory + "\\" + filename) as csvfile:
            reader = csv.DictReader(csvfile, dialect='excel')
            for row in reader:
                # format is row['header name']
                ObservationPeriod = row['Observation Period']
                ObservationPeriodTimestamp = row['Observation Period Timestamp']
                PinID = row['Pin ID']
                PinType = row['Pin Type']
                Xrow = row['X']
                Yrow = row['Y']
                #Yrow = row['Rotation']
                ActorType = row['Actor Type']
                ActorTypeOther = row['Actor Type Other']
                InteractionInstances = row['Interaction Instances']
                Interactions = row['Interactions']
                ObservationPeriodComments = row['Observation Period Comments']
                ObservationID = row['Observation ID']
                ObservationTimestamp = row['Observation Timestamp']
                PostureType = row['Posture Type']
                ObservationDevices = row['Observation Devices']
                ObservationComments = row['Observation Comments']
                rowcapture_list.append("{0}?{1}?{2}?{3}?{4}?{5}?{6}?{7}?{8}?{9}?{10}?{11}?{12}?{13}?{14}?{15}?{16}".format(ObservationPeriod, ObservationPeriodTimestamp, PinID, PinType, Xrow, Yrow,
                                                                                                             ActorType, ActorTypeOther, InteractionInstances, Interactions,
                                                                        ObservationPeriodComments, ObservationID, ObservationTimestamp, PostureType, ObservationDevices, ObservationComments, filename))
def writelines(dic, rowcount):
    csvfile = "Folder Name C:\Junk\\ for example" + "\\" + "Filename.csv"
    with open(csvfile, "ab") as csvWrite:
        write = csv.DictWriter(csvWrite, dic.keys())
        if rowcount == 0:
            write.writeheader()
        write.writerow(dic)

checkcsvforheaders(csv_Directory)
copylines(csv_Directory)
#print len(rowcapture_list)
rowcount = 0
for row in rowcapture_list:
    EatDrink = 'No'
    Headphone = 'No'
    ScreenShare = 'No'
    WhiteBoard = 'No'
    Printmat = 'No'
    Ind_Device = 'No'
    TimeofDay = 'None'
    Weekend = "No"
    ObservationPeriod_Final = row.split('?')[0]
    ObservationTimeStamp_Final = row.split('?')[1]
    PinID_Final = row.split('?')[2]
    PinType_Final = row.split('?')[3]
    Xrow_Final = row.split('?')[4]
    Yrow_Final = row.split('?')[5]
    ActorType_Final = row.split('?')[6]
    ActorTypeOther_Final = row.split('?')[7]
    InteractionInstances = row.split('?')[8]
    Interactions_Final = row.split('?')[9]
    ObservationPeriodComments_Final = row.split('?')[10]
    ObservationID_Final = row.split('?')[11]
    ObservationDate = row.split('?')[12]
    DaySplit = ObservationDate.split(' ')[0]
    if DaySplit == "Sun" or DaySplit == "Sat":
        Weekend = "Yes"
    TimeSplit = ObservationDate.split(' ')[-1]
    Time = TimeSplit.split(':')[0]
    if int(Time) <= 15:
        TimeofDay = "Afternoon"
    if int(Time) > 15:
        TimeofDay = "Evening"
    PostureType_Final = row.split('?')[13]
    ObservationDevices_Final = row.split('?')[14] #Ind_device, Interact, Printmat, Headphones, Eat/Drink, Screen_share, Whiteboard
    #Try and Capture Additional Calculated Values
    Devicesplit = ObservationDevices_Final.split(",")
    if "Eat/drink" in Devicesplit:
        EatDrink = "Yes"
    if "Headphones" in Devicesplit:
        Headphone = "Yes"
    if "Printmat" in Devicesplit:
        Printmat = "Yes"
    if "Whiteboard" in Devicesplit:
        WhiteBoard = "Yes"
    if "Screen_share" in Devicesplit:
        ScreenShare = "Yes"
    if "Ind_device" in Devicesplit:
        Ind_Device = "Yes"
    ObservationComments_Final = row.split('?')[15]
    filename_Final = row.split('?')[16]
    my_dict = {"ObservationPeriod": ObservationPeriod_Final, "ObservationTimestamp": ObservationTimeStamp_Final, "PinID": PinID_Final, "PinType": PinType_Final, "X": Xrow_Final, "Y": Yrow_Final,
               "ActorType": ActorType_Final, "ActorTypeOther": ActorTypeOther_Final, "InteractionInstances": InteractionInstances, "Interactions": Interactions_Final, "ObservationPeriodComments": ObservationComments_Final,
               "ObservationID": ObservationID_Final, "Observation Date": ObservationDate, "PostureType": PostureType_Final, "ObservationDevices": ObservationDevices_Final,
               "ObservationComments": ObservationComments_Final, "FileName": filename_Final,
               "EatDrink": EatDrink, "ScreenShare": ScreenShare, "Headphones": Headphone, "WhiteBoard": WhiteBoard, "Printmat": Printmat, "IndividualDevice": Ind_Device, "TimeofDay": TimeofDay, "Weekend": Weekend} #Derived fields based on Devices

    print my_dict
    writelines(my_dict, rowcount)
    rowcount += 1


