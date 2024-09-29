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
LIBS:Through40-cache
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
U 1 1 59C592F2
P 8050 3550
F 0 "U2" H 8050 3450 50  0000 C CNN
F 1 "coax" H 8050 3650 50  0000 C CNN
F 2 "Lib_fp:rfcoax" H 8050 3550 50  0001 C CNN
F 3 "DOCUMENTATION" H 8050 3550 50  0001 C CNN
	1    8050 3550
	1    0    0    -1  
$EndComp
$Comp
L coax U1
U 1 1 59C593A0
P 6450 3550
F 0 "U1" H 6450 3450 50  0000 C CNN
F 1 "coax" H 6450 3650 50  0000 C CNN
F 2 "Lib_fp:rfcoax" H 6450 3550 50  0001 C CNN
F 3 "DOCUMENTATION" H 6450 3550 50  0001 C CNN
	1    6450 3550
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR01
U 1 1 59C5944A
P 8050 4050
F 0 "#PWR01" H 8050 3800 50  0001 C CNN
F 1 "GND" H 8050 3900 50  0000 C CNN
F 2 "" H 8050 4050 50  0001 C CNN
F 3 "" H 8050 4050 50  0001 C CNN
	1    8050 4050
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 59C594BC
P 6450 3050
F 0 "#PWR02" H 6450 2800 50  0001 C CNN
F 1 "GND" H 6450 2900 50  0000 C CNN
F 2 "" H 6450 3050 50  0001 C CNN
F 3 "" H 6450 3050 50  0001 C CNN
	1    6450 3050
	-1   0    0    1   
$EndComp
$EndSCHEMATC
