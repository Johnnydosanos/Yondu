'''
Project Name: Project #1: Yondu Udonta
Author: John Dunn
Due Date: 02/04/2022
Course: CS1400-X02

Put your description here, lessons learned here, and 
any other information someone using yourprogram would 
need to know to make it run.

Yondu Udonta prompts a user for the # of pirates in a raiding party,
and the # of units (money) they have pooled. Both input #s must be
positive integers, pirate # must be > 3, Unit # must be >= 3*pirates.
First a flat share is given to each pirate. Second, Yondu takes a % share
of remaining. Third, Quill takes a % share of remaining. Fourth, what's
left of the units is evenly divided between all pirates. The Remainder
that is not evenly divided goes to RBF, another party.


'''
def main():

    


    '''
    Program starts here.
    '''
    '''try:
        # (1) replace pass with your code
        pass
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return'''


print("How many reavers?")
reavers = float(input())
if reavers < 3:
    print("Not enough crew.")
    exit()
elif reavers % 1 != 0:
    print("Enter positive integers for reavers and units.")
    exit()

        # prompt reavers, convert to int, conditions of variable

print("How many units?")
units = float(input())
if units <= 3 * reavers:
    print("Not enough units.")
    exit()
elif units % 1 != 0:
    print("Enter positive integers for reavers and units.")
    exit()
        # prompt units, convert to int, conditions of variable

current_total_units = units
current_total_units = int(current_total_units)
units_per_pirate = 0
yondu_units = 0
quill_units = 0
        # initial variable positions

current_total_units = units - ((reavers - 2) * 3) 
        # give 3 units to each reaver except yondu and quill
        # and set current units to remaining units
        
yondu_units = ((current_total_units * 13)//100)
        # yondu gets 13% of the current units
current_total_units = (current_total_units - yondu_units)
        # subtract yondus current share from current total units

quill_units = ((current_total_units * 11)//100)
        # quill gets 11% of the current units
current_total_units = (current_total_units - quill_units)
        # subtract quills current share from current total units

rbf_unit = current_total_units % reavers
        # set RBF to remainder
temp_unit_share = (current_total_units - rbf_unit) / reavers
        # the 'split share' each reaver will recieve, while removing 
        # the remainder beforehand
units_per_pirate += temp_unit_share
        # the 'split share' is added to each pirates share count
yondu_units += temp_unit_share
        # the 'split share' is added to yondus share count
quill_units += temp_unit_share
        # the 'split share' is added to quills share count

print("Yondu's share: " + str(yondu_units))
print("Peter's share: " + str(quill_units))
print("Crew: " + str(units_per_pirate))
print("RBF: " + str(rbf_unit))
# output shares

if __name__ == "__main__":
    main()