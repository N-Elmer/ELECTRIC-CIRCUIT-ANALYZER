print("******************************* WELCOME TO THE RESISTANCE CALCULATOR ********************************")
print("*****************************************************************************************************\n")

print("PLEASE CHOOSE THE KIND OF RESISTANCE YOU WISH TO CALCULATE")

print("ENTER 1 FOR VOLTAGE & RESISTANCE IN SERIES\nENTER 2 FOR VOLTAGE & RESISTANCE IN PARALLEL\nENTER 3 FOR VOLTAGE & BOTH TYPE OF RESISTANCES")
choice = int(input())

if choice == 1:

    print("ENTER THE CURRENT IN THE SYSTEM")
    I = float(input())
    # I means current

    print("ENTER THE TOTAL NUMBER OF RESISTORS IN SERIES")
    Rst = int(input())
    # Rst means total number of resistors in series

    print("ENTER A UNIT VALUE FOR EACH OF THE",Rst,"RESISTORS CONNECTED IN SERIES")

    # Rsv = int
    # Rsv means value of sum of resistance in series

    RstList = []
    # RstList is the list that holds Rst in order to calculate Rsv

    for Rst in range(0,Rst,1):
        print("ENTER A RESISTOR UNIT VALUE")
        Rsuv = float(input())
        # Rsuv means series resistance unit value
        RstList.append(Rsuv)

    Rs = sum(RstList)
    # Rs means resistance in series

    print("RESISTANCE IN SERIES IS: %0.2f"%Rs,"Ω")

    V = float(I*Rs)
    # V means voltage

    print("ANY APARATUS CONNECTED TO THIS CIRCUIT SHOULD BE ABLE TO SUPPORT AT LEAST %0.2f"%V,"VOLTS")

elif choice == 2:

    print("ENTER THE CURRENT IN THE SYSTEM")
    I = float(input())
    # I means current

    print("PLEASE ENTER THE TOTAL NUMBER OF RESISTORS IN PARALLEL")
    Rpt = int(input())
    # Rpt means total number of resistors in parallel

    print("ENTER A UNIT VALUE FOR EACH OF THE",Rpt,"RESISTORS CONNECTED IN PARALLEL")

    # Rpv = float
    # Rpv means value of sum of resistance in parallel

    RptList = []
    # RptList is the list that holds Rpt in order to calculate Rpv

    for Rpt in range(0,Rpt,1):
        print("ENTER A RESISTOR UNIT VALUE")
        Rpuv = float(input())
        # Rpuv means parallel resistance unit value
        RptList.append(Rpuv)


    def product(RptList):
        product = 1
        for i in RptList:
            product = product * i
        return product

    Rpsl = sum(RptList)
    # Rpsl means sum of the Rptlist

    Rp = float(product(RptList)/Rpsl)
    # Rp means resistance in series

    print("RESISTANCE IN PARALLEL IS: %0.2f"%Rp,"Ω")

    V = float(I*Rp)
    # V means voltage

    print("ANY APARATUS CONNECTED TO THIS CIRCUIT SHOULD BE ABLE TO SUPPORT AT LEAST %0.2f"%V,"VOLTS")

elif choice == 3:

    print("ENTER THE CURRENT IN THE SYSTEM")
    I = float(input())
    # I means current

    print("ENTER THE TOTAL NUMBER OF RESISTORS IN SERIES")
    Rst = int(input())
    # Rst means total number of resistors in series

    print("ENTER A UNIT VALUE FOR EACH OF THE",Rst,"RESISTORS CONNECTED IN SERIES")

    # Rsv = int
    # Rsv means value of sum of resistance in series

    RstList = []
    # RstList is the list that holds Rst in order to calculate Rsv

    for Rst in range(0,Rst,1):
        print("ENTER A RESISTOR UNIT VALUE")
        Rsuv = float(input())
        # Rsuv means series resistance unit value
        RstList.append(Rsuv)

    Rs = sum(RstList)
    # Rs means resistance in series

    print("RESISTANCE IN SERIES IS: %0.2f"%Rs,"Ω")

    print("PLEASE ENTER THE TOTAL NUMBER OF RESISTORS IN PARALLEL")
    Rpt = int(input())
    # Rpt means total number of resistors in parallel

    print("ENTER A UNIT VALUE FOR EACH OF THE",Rpt,"RESISTORS CONNECTED IN PARALLEL")

    # Rpv = float
    # Rpv means value of sum of resistance in parallel

    RptList = []
    # RptList is the list that holds Rpt in order to calculate Rpv

    for Rpt in range(0,Rpt,1):
        print("ENTER A RESISTOR UNIT VALUE")
        Rpuv = float(input())
        # Rpuv means parallel resistance unit value
        RptList.append(Rpuv)


    def product(RptList):
        product = 1
        for i in RptList:
            product = product * i
        return product


    Rpsl = sum(RptList)
    # Rpsl means sum of the Rptlist

    Rp = float(product(RptList)/Rpsl)
    # Rp means resistance in series

    print("RESISTANCE IN PARALLEL IS: %0.2f"%Rp,"Ω")

    Rspt = Rp+Rs
    # Rspt means the total resistance of a circuit containing both series and parallel connections

    print("THE TOTAL RESISTANCE IS: %0.2f"%Rspt,"Ω")

    V = float(I*Rspt)
    # V means voltage

    print("ANY APARATUS CONNECTED TO THIS CIRCUIT SHOULD BE ABLE TO SUPPORT AT LEAST %0.2f"%V,"VOLTS")

else:
    print("ERROR!!! CHOOSE ANY OPTION FROM 1 TO 3")
    print("RE-RUN THE PROGRAM")