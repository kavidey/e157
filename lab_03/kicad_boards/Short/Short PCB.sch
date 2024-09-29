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
LIBS:Short PCB-cache
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
U 1 1 59C5CFFD
P 8300 3750
F 0 "U2" H 8300 3650 50  0000 C CNN
F 1 "coax" H 8300 3850 50  0000 C CNN
F 2 "Lib_fp:rfcoax" H 8300 3750 50  0001 C CNN
F 3 "DOCUMENTATION" H 8300 3750 50  0001 C CNN
	1    8300 3750
	1    0    0    -1  
$EndComp
$Comp
L coax U1
U 1 1 59C5D057
P 6700 3750
F 0 "U1" H 6700 3650 50  0000 C CNN
F 1 "coax" H 6700 3850 50  0000 C CNN
F 2 "Lib_fp:rfcoax" H 6700 3750 50  0001 C CNN
F 3 "DOCUMENTATION" H 6700 3750 50  0001 C CNN
	1    6700 3750
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR01
U 1 1 59C5D0C9
P 8300 4250
F 0 "#PWR01" H 8300 4000 50  0001 C CNN
F 1 "GND" H 8300 4100 50  0000 C CNN
F 2 "" H 8300 4250 50  0001 C CNN
F 3 "" H 8300 4250 50  0001 C CNN
	1    8300 4250
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 59C5D121
P 6700 3250
F 0 "#PWR02" H 6700 3000 50  0001 C CNN
F 1 "GND" H 6700 3100 50  0000 C CNN
F 2 "" H 6700 3250 50  0001 C CNN
F 3 "" H 6700 3250 50  0001 C CNN
	1    6700 3250
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR03
U 1 1 59C5D16E
P 7500 3850
F 0 "#PWR03" H 7500 3600 50  0001 C CNN
F 1 "GND" H 7500 3700 50  0000 C CNN
F 2 "" H 7500 3850 50  0001 C CNN
F 3 "" H 7500 3850 50  0001 C CNN
	1    7500 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	7500 3750 7500 3850
$EndSCHEMATC
