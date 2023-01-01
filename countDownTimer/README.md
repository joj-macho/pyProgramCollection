# Countdown Timer

## Description

This program is a simulation of a digital timer that counts down to zero.

The second version of the countdown timer uses the Seven Segment Display. The seven segment displays are the output display device that provide a way to display information in the form of image or text or decimal numbers. It is widely used in digital clocks, basic calculators, electronic meters, and other electronic devices that display numerical information. It consists of seven segments of light emitting diodes (LEDs) which is assembled like numerical 8.

A labeled seven-segment display, with each segment labeled A to G:
```
 __A__
|     |    Each digit in a seven-segment display:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|
```

## How it Works

### Countdown Timer

- Prompt the user to give the input number of seconds to start the countdown from.

- The `countDown()` function uses a while loop until the `startTime` reaches zero.
    - To calculate the number of minutes and seconds, use `divmod()` function.
        ```python
        minutes, seconds = divmod(startTime, 60)
        ```
    - The time. sleep() function is used to make the program wait one second.
    - Now decrement time so that the while loop can reach a finish.


## Program Input & Output

When you run `countdown0.py`, the output will look like this;

```
Countdown Timer.

Enter seconds to start countdown:
> 6
00 : 06
00 : 05
00 : 04
00 : 03
00 : 02
00 : 01

COUNTDOWN COMPLETE
```

When you run `countdown.py`, the output will look like this;

```
CountDown Timer.

Enter seconds to start countdown. Press Ctrl-C to quit:
> 5
 __   __       __   __       __   __ 
|  | |  |  *  |  | |  |  *  |  | |__ 
|__| |__|  *  |__| |__|  *  |__|  __|
 __   __       __   __       __      
|  | |  |  *  |  | |  |  *  |  | |__|
|__| |__|  *  |__| |__|  *  |__|    |
 __   __       __   __       __   __ 
|  | |  |  *  |  | |  |  *  |  |  __|
|__| |__|  *  |__| |__|  *  |__|  __|
 __   __       __   __       __   __ 
|  | |  |  *  |  | |  |  *  |  |  __|
|__| |__|  *  |__| |__|  *  |__| |__ 
 __   __       __   __       __      
|  | |  |  *  |  | |  |  *  |  |    |
|__| |__|  *  |__| |__|  *  |__|    |
 __   __       __   __       __   __ 
|  | |  |  *  |  | |  |  *  |  | |  |
|__| |__|  *  |__| |__|  *  |__| |__|


COUNTDOWN COMPLETE
```