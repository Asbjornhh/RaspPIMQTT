  #!/bin/bash

tested=""
failed=""

usage()
{
   cat <<EOF
This program checks the Raspberry Pi 4's GPIOs.

The program reads and writes all the GPIOs. Ensure NOTHING
is connected to the GPIOs during this test.

The program uses the pigpio daemon which must be running.

To start the daemon use the command sudo pigpiod.

Press the ENTER key to continue or ctrl-C to abort...
EOF

   read a
}

check_gpio()
{
   # $1 gpio

   m=$(pigs mg $1) # save mode
   L=$(pigs r $1)  # save level

   s=$(pigs m $1 w)

   if [[ $s  = "" ]]
   then
      f=0
      tested+="$1 "

      # write mode tests
      $(pigs w $1 0)
      r=$(pigs r $1)
      if [[ $r -ne 0 ]]; then f=1; echo "Write 0 to gpio $1 failed."; fi

      $(pigs w $1 1)
      r=$(pigs r $1)
      if [[ $r -ne 1 ]]; then f=1; echo "Write 1 to gpio $1 failed."; fi

      # read mode tests using pull-ups and pull-downs
      $(pigs m $1 r)

      $(pigs pud $1 d)
      r=$(pigs r $1)
      if [[ $r -ne 0 ]]; then f=1; echo "Pull down on gpio $1 failed."; fi

      $(pigs pud $1 u)
      r=$(pigs r $1)
      if [[ $r -ne 1 ]]; then f=1; echo "Pull up on gpio $1 failed."; fi

      $(pigs pud $1 o)   # switch pull-ups/downs off
      $(pigs w $1 $L)    # restore original level

      if [[ $f -ne 0 ]]; then failed+="$1 "; fi
   fi
}  2>/dev/null

usage

echo "Testing Raspberry Pi 4 GPIOs..."

# List of user-accessible GPIO pins on Raspberry Pi 4 Model B
gpio_pins=(2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27)

for pin in "${gpio_pins[@]}"; do
   check_gpio $pin
done

if [[ $failed = "" ]]; then failed="None"; fi

echo "Tested GPIOs: $tested"
echo "Failed GPIOs: $failed"
