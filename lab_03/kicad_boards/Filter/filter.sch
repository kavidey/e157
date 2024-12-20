EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:coax
LIBS:filter-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L coax U2
U 1 1 59C5DDAB
P 8100 3500
F 0 "U2" H 8100 3400 50  0000 C CNN
F 1 "coax" H 8100 3600 50  0000 C CNN
F 2 "Lib_fp:rfcoax" H 8100 3500 50  0001 C CNN
F 3 "DOCUMENTATION" H 8100 3500 50  0001 C CNN
	1    8100 3500
	1    0    0    -1  
$EndComp
$Comp
L coax U1
U 1 1 59C5DE0D
P 4250 3500
F 0 "U1" H 4250 3400 50  0000 C CNN
F 1 "coax" H 4250 3600 50  0000 C CNN
F 2 "Lib_fp:rfcoax" H 4250 3500 50  0001 C CNN
F 3 "DOCUMENTATION" H 4250 3500 50  0001 C CNN
	1    4250 3500
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR01
U 1 1 59C5DEBD
P 8100 4000
F 0 "#PWR01" H 8100 3750 50  0001 C CNN
F 1 "GND" H 8100 3850 50  0000 C CNN
F 2 "" H 8100 4000 50  0001 C CNN
F 3 "" H 8100 4000 50  0001 C CNN
	1    8100 4000
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 59C5DEE5
P 4250 3000
F 0 "#PWR02" H 4250 2750 50  0001 C CNN
F 1 "GND" H 4250 2850 50  0000 C CNN
F 2 "" H 4250 3000 50  0001 C CNN
F 3 "" H 4250 3000 50  0001 C CNN
	1    4250 3000
	-1   0    0    1   
$EndComp
$Comp
L C C1
U 1 1 59D2A033
P 5200 3500
F 0 "C1" H 5225 3600 50  0000 L CNN
F 1 "C" H 5225 3400 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 5238 3350 50  0001 C CNN
F 3 "" H 5200 3500 50  0001 C CNN
	1    5200 3500
	0    1    1    0   
$EndComp
$Comp
L C C4
U 1 1 59D2A14D
P 5800 3500
F 0 "C4" H 5825 3600 50  0000 L CNN
F 1 "C" H 5825 3400 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 5838 3350 50  0001 C CNN
F 3 "" H 5800 3500 50  0001 C CNN
	1    5800 3500
	0    1    1    0   
$EndComp
$Comp
L C C7
U 1 1 59D2A177
P 6250 3500
F 0 "C7" H 6275 3600 50  0000 L CNN
F 1 "C" H 6275 3400 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 6288 3350 50  0001 C CNN
F 3 "" H 6250 3500 50  0001 C CNN
	1    6250 3500
	0    1    1    0   
$EndComp
$Comp
L C C10
U 1 1 59D2A198
P 6700 3500
F 0 "C10" H 6725 3600 50  0000 L CNN
F 1 "C" H 6725 3400 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 6738 3350 50  0001 C CNN
F 3 "" H 6700 3500 50  0001 C CNN
	1    6700 3500
	0    1    1    0   
$EndComp
$Comp
L C C13
U 1 1 59D2A1C0
P 7150 3500
F 0 "C13" H 7175 3600 50  0000 L CNN
F 1 "C" H 7175 3400 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 7188 3350 50  0001 C CNN
F 3 "" H 7150 3500 50  0001 C CNN
	1    7150 3500
	0    1    1    0   
$EndComp
$Comp
L C C11
U 1 1 59D2A1E8
P 6900 3200
F 0 "C11" H 6925 3300 50  0000 L CNN
F 1 "C" H 6925 3100 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 6938 3050 50  0001 C CNN
F 3 "" H 6900 3200 50  0001 C CNN
	1    6900 3200
	-1   0    0    1   
$EndComp
$Comp
L C C2
U 1 1 59D2A271
P 5500 3200
F 0 "C2" H 5525 3300 50  0000 L CNN
F 1 "C" H 5525 3100 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 5538 3050 50  0001 C CNN
F 3 "" H 5500 3200 50  0001 C CNN
	1    5500 3200
	1    0    0    -1  
$EndComp
$Comp
L C C3
U 1 1 59D2A30F
P 5500 3750
F 0 "C3" H 5525 3850 50  0000 L CNN
F 1 "C" H 5525 3650 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 5538 3600 50  0001 C CNN
F 3 "" H 5500 3750 50  0001 C CNN
	1    5500 3750
	-1   0    0    1   
$EndComp
$Comp
L C C5
U 1 1 59D2A36B
P 6100 3200
F 0 "C5" H 6125 3300 50  0000 L CNN
F 1 "C" H 6125 3100 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 6138 3050 50  0001 C CNN
F 3 "" H 6100 3200 50  0001 C CNN
	1    6100 3200
	-1   0    0    1   
$EndComp
$Comp
L C C6
U 1 1 59D2A3BA
P 6100 3750
F 0 "C6" H 6125 3850 50  0000 L CNN
F 1 "C" H 6125 3650 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 6138 3600 50  0001 C CNN
F 3 "" H 6100 3750 50  0001 C CNN
	1    6100 3750
	-1   0    0    1   
$EndComp
$Comp
L C C9
U 1 1 59D2A42A
P 6450 3750
F 0 "C9" H 6475 3850 50  0000 L CNN
F 1 "C" H 6475 3650 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 6488 3600 50  0001 C CNN
F 3 "" H 6450 3750 50  0001 C CNN
	1    6450 3750
	-1   0    0    1   
$EndComp
$Comp
L C C8
U 1 1 59D2A4A1
P 6450 3200
F 0 "C8" H 6475 3300 50  0000 L CNN
F 1 "C" H 6475 3100 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 6488 3050 50  0001 C CNN
F 3 "" H 6450 3200 50  0001 C CNN
	1    6450 3200
	-1   0    0    1   
$EndComp
$Comp
L C C12
U 1 1 59D2A501
P 6900 3750
F 0 "C12" H 6925 3850 50  0000 L CNN
F 1 "C" H 6925 3650 50  0000 L CNN
F 2 "Lib_fp:filtercap" H 6938 3600 50  0001 C CNN
F 3 "" H 6900 3750 50  0001 C CNN
	1    6900 3750
	-1   0    0    1   
$EndComp
Wire Wire Line
	5350 3500 5650 3500
Wire Wire Line
	5500 3600 5500 3350
Wire Wire Line
	5950 3500 6100 3500
Wire Wire Line
	6100 3600 6100 3350
Wire Wire Line
	6450 3350 6450 3600
Wire Wire Line
	6400 3500 6550 3500
Wire Wire Line
	6850 3500 7000 3500
Wire Wire Line
	6900 3350 6900 3600
$Comp
L GND #PWR03
U 1 1 59D2AD6F
P 6900 3900
F 0 "#PWR03" H 6900 3650 50  0001 C CNN
F 1 "GND" H 6900 3750 50  0000 C CNN
F 2 "" H 6900 3900 50  0001 C CNN
F 3 "" H 6900 3900 50  0001 C CNN
	1    6900 3900
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR04
U 1 1 59D2ADAE
P 6450 3900
F 0 "#PWR04" H 6450 3650 50  0001 C CNN
F 1 "GND" H 6450 3750 50  0000 C CNN
F 2 "" H 6450 3900 50  0001 C CNN
F 3 "" H 6450 3900 50  0001 C CNN
	1    6450 3900
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR05
U 1 1 59D2ADF5
P 6100 3900
F 0 "#PWR05" H 6100 3650 50  0001 C CNN
F 1 "GND" H 6100 3750 50  0000 C CNN
F 2 "" H 6100 3900 50  0001 C CNN
F 3 "" H 6100 3900 50  0001 C CNN
	1    6100 3900
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR06
U 1 1 59D2AE2D
P 5500 3900
F 0 "#PWR06" H 5500 3650 50  0001 C CNN
F 1 "GND" H 5500 3750 50  0000 C CNN
F 2 "" H 5500 3900 50  0001 C CNN
F 3 "" H 5500 3900 50  0001 C CNN
	1    5500 3900
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR07
U 1 1 59D2AE65
P 5500 3050
F 0 "#PWR07" H 5500 2800 50  0001 C CNN
F 1 "GND" H 5500 2900 50  0000 C CNN
F 2 "" H 5500 3050 50  0001 C CNN
F 3 "" H 5500 3050 50  0001 C CNN
	1    5500 3050
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR08
U 1 1 59D2AE9D
P 6100 3050
F 0 "#PWR08" H 6100 2800 50  0001 C CNN
F 1 "GND" H 6100 2900 50  0000 C CNN
F 2 "" H 6100 3050 50  0001 C CNN
F 3 "" H 6100 3050 50  0001 C CNN
	1    6100 3050
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR09
U 1 1 59D2AED5
P 6450 3050
F 0 "#PWR09" H 6450 2800 50  0001 C CNN
F 1 "GND" H 6450 2900 50  0000 C CNN
F 2 "" H 6450 3050 50  0001 C CNN
F 3 "" H 6450 3050 50  0001 C CNN
	1    6450 3050
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR010
U 1 1 59D2AF0D
P 6900 3050
F 0 "#PWR010" H 6900 2800 50  0001 C CNN
F 1 "GND" H 6900 2900 50  0000 C CNN
F 2 "" H 6900 3050 50  0001 C CNN
F 3 "" H 6900 3050 50  0001 C CNN
	1    6900 3050
	-1   0    0    1   
$EndComp
$EndSCHEMATC
