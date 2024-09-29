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
LIBS:Open-cache
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
L C C1
U 1 1 59B6F8DC
P 5950 2900
F 0 "C1" H 5975 3000 50  0000 L CNN
F 1 "C" H 5975 2800 50  0000 L CNN
F 2 "Lib_fp:cap" H 5988 2750 50  0001 C CNN
F 3 "" H 5950 2900 50  0001 C CNN
	1    5950 2900
	0    1    1    0   
$EndComp
$Comp
L coax U2
U 1 1 59C50E47
P 6900 2900
F 0 "U2" H 6900 2800 50  0000 C CNN
F 1 "coax" H 6900 3000 50  0000 C CNN
F 2 "Lib_fp:rfcoax" H 6900 2900 50  0001 C CNN
F 3 "DOCUMENTATION" H 6900 2900 50  0001 C CNN
	1    6900 2900
	1    0    0    -1  
$EndComp
$Comp
L coax U1
U 1 1 59C50EB8
P 5000 2900
F 0 "U1" H 5000 2800 50  0000 C CNN
F 1 "coax" H 5000 3000 50  0000 C CNN
F 2 "Lib_fp:rfcoax" H 5000 2900 50  0001 C CNN
F 3 "DOCUMENTATION" H 5000 2900 50  0001 C CNN
	1    5000 2900
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR01
U 1 1 59C5106B
P 6900 3400
F 0 "#PWR01" H 6900 3150 50  0001 C CNN
F 1 "GND" H 6900 3250 50  0000 C CNN
F 2 "" H 6900 3400 50  0001 C CNN
F 3 "" H 6900 3400 50  0001 C CNN
	1    6900 3400
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 59C51086
P 5000 2400
F 0 "#PWR02" H 5000 2150 50  0001 C CNN
F 1 "GND" H 5000 2250 50  0000 C CNN
F 2 "" H 5000 2400 50  0001 C CNN
F 3 "" H 5000 2400 50  0001 C CNN
	1    5000 2400
	-1   0    0    1   
$EndComp
$EndSCHEMATC
