#!/usr/bin/env python
# coding: utf-8

# # Matt McClinton's Parking Function Verifier
# This code takes in a tuple, runs the parking function algorithm, and confirms if the tuple is indeed a parking function
# 
# 
# __Definitions__
# 
# __i__ = the $i^{th}$ parking spot
# 
# __ci__ = car $i$
# 
# __ai__ = desired parking spot for __ci__

# In[1]:


def nrow(n): # this makes a row of n zeros [0, 0, ..., 0]
    row = []
    for i in range(n):
        row.append(0)
    return row


# For simplicity we will refer to the tuple by PF

# In[4]:


def PFconfirm(PF): # this will test if list PF is indeed a parking function.
    n = len(PF)
    ParkingLot = nrow(n) # this will keep track of the parking spots that get filled.
    for ci in PF:
        for ai in range(len(ParkingLot)):
            if ci == ai + 1 and ParkingLot[ai] == 0:    # if preferred spot AVAILABLE, park here.
                ParkingLot[ai] += ci
                break
            elif ci < ai + 1 and ParkingLot[ai] == 0:   # else if preferred spot UNAVAILABLE, go to next available spot.
                ParkingLot[ai] += ci
                break
            elif ai + 1 == n and ParkingLot[ai] != 0:   # if last spot unavailable, leave the parking lot.
                return('Not a parking function!')
    return "It's a parking function!",ParkingLot;


# In[ ]:




