from datetime import datetime, timedelta

from datetime import datetime, timedelta
from datetime import datetime

#NOTE I used assumed that the times are like '09:00' not '9:00' so it was easier to compare the hours

def get_meet_times(calendar1, calendar2, range1, range2,meeting_time):


    #find the latest starting time from the 2 ranges
    if range1[0]<range2[0]:
        startmax=range2[0]
    else:
        startmax=range1[0]

    # find the earliest end time from the 2 ranges
    if range1[1]>range2[1]:
        endmin=range2[1]

    else:
        endmin=range1[1]




    newcalendar1=[]
    newcalendar2=[]



    #find the free intervals in each calendar

    # if the guy has free time between his starting range and the first meeting
    if range1[0]<calendar1[0][0]:
        newcalendar1.append([range1[0],calendar1[0][0]])

    for i in range(len(calendar1)-1):
        if calendar1[i][1]<calendar1[i+1][0]:
            #create a list o free time slots

                newcalendar1.append([calendar1[i][1],calendar1[i+1][0]])
    #print(calendar1[len(newcalendar1)])
    #if the guy has free time between his last meeting ending and the ending of the range, add it
    if range1[1]>calendar1[len(calendar1)-1][1]:
        newcalendar1.append([calendar1[len(calendar1)-1][1],range1[1]])






    if range2[0]<calendar2[0][0]:
        newcalendar2.append([range2[0],calendar2[0][0]])
    #same for second guy
    for i in range(len(calendar2)-1):
        if calendar2[i][1] < calendar2[i + 1][0]:
            newcalendar2.append([calendar2[i][1],calendar2[i+1][0]])
   # print(calendar2[len(calendar2)-1])
    if range2[1] > calendar2[len(calendar2)-1][1]:
        newcalendar2.append([calendar2[len(calendar2)-1][1], range2[1]])



    #delete the free times earlier than the maxstart range time and later than minend range time


    #print(newcalendar1)
    #print(newcalendar2)
    #print("///")

    # note: the intervals here represent the free times

    finalcalendar1=[]
    finalcalendar2=[]
    for i in newcalendar1:
        if i[0]<startmax and i[1]>startmax:
            #this case is when an interval starts before the max start range time but end after it
            # so a possible time interval can be [startmax,end of the interval]

            finalcalendar1.append([startmax,i[1]])
        if i[0]>=startmax and i[1]<=endmin:
            # this case is when an interval starts after or equal the max start range time and end before
            #the min end time so we just add it
            finalcalendar1.append(i)
        if i[1]>endmin and i[0]<endmin:
            # this case is when an interval starts before the min end time but end after it
            # so a possible time interval can be [beginning of the interval, endmin]
            finalcalendar1.append([i[0],endmin])


    #same cases for calendar2
    for i in newcalendar2:
        if i[0] < startmax and i[1] > startmax:
            finalcalendar2.append([startmax, i[1]])
        if i[0] >= startmax and i[1] <= endmin:
            finalcalendar2.append(i)
        if i[1] > endmin and i[0] < endmin:
            finalcalendar2.append([i[0], endmin])


    #print(finalcalendar1)

    #print(finalcalendar2)



    #print("/////////////")



    #at this point we have a list of free time intervals limited by the correct range limit
    #so we just need to find the common free time slots that are >=meeting_time
    c1=0
    c2=0
    rez=[]
    while c1<len(finalcalendar1) and c2<len(finalcalendar2):
        if finalcalendar1[c1][1]<finalcalendar2[c2][0]:
            #here is the case where ending free time of c1 is smaller than starting free time of c2 so we go to the next element in c1
            c1+=1
        if finalcalendar2[c2][1]<finalcalendar1[c1][0]:
            #same but the roles are swapped
            c2+=1

        if finalcalendar1[c1][0]<finalcalendar2[c2][1] or finalcalendar2[c2][0]<finalcalendar2[c2][1]:
            #now we found common free time slots and we check if the time intervals lasts >=meeting_time
            time1 = datetime.strptime(min(finalcalendar1[c1][1], finalcalendar2[c2][1]), '%H:%M')
            time2 = datetime.strptime(max(finalcalendar1[c1][0], finalcalendar2[c2][0]), '%H:%M')
            duration_in_minutes = (time1 - time2).total_seconds()// 60

            duration_in_minutes_as_int = int(duration_in_minutes)

            #if it does we add it to the rez

            #we need to do the max of the starting time of c1 and c2 because both need to be free so at the latter  of the 2 they are.
            #also we need to do the min of the ending time because again both need to be free so after 1 finishes they can no longer meet
            if duration_in_minutes_as_int>=meeting_time:
                rez.append([max(finalcalendar1[c1][0],finalcalendar2[c2][0]),min(finalcalendar1[c1][1],finalcalendar2[c2][1])])
            if finalcalendar1[c1][1]<finalcalendar2[c2][1]:
                #we incremant the one with ending time earlier
                c1+=1
            else:
                c2+=1

    print(rez)







# Sample input
calendar1 = [['09:30', '10:00'],['10:01','10:30'], ['12:00', '13:00'], ['16:00', '18:00'],['18:30','20:00']]
range1 = ['09:00', '20:30']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
range2 = ['09:00', '20:30']
meeting_time = 30

# Merge the calendars
merged_calendar = get_meet_times(calendar1, calendar2, range1, range2,meeting_time)

# Find all available time slots

