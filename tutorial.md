# NGspice Tutorial

When exploring electronics, getting started is going to be quite annoying. You need lots of components,
a breadboard time to put it all together, and even then if a change is desired, you need to do it all over
again. In comparison to that, simulation of electronic components and circuits does not require any of
the hardware, you have every possible component at hand, and it is additionally possible to perform
automatic sweeps accross the various component sets, even if some amount of external software may be
needed for that. This assumes that ngspice is already installed and you are running a linux machine.

NGspice is a software that is able to simulate electronic circuits quite accurately and is free to use and
modify. This text should guide you to become comfortable in using ngspice for designing circuits, before
having them be turned in to actual hardware.

# The humble voltage divider
As a first circuit, let us consider the humble voltage divider. This is mostly used to get you used to the
notation of things. First we need to specify the divider netlist. A netlist is essentially a textual
representation of a circuit diagram. It contains devices and the nodes that interconnect them, as well
as the values of the various components being used in the circuit. The following shows the netlist
for a voltage divider, which is stored in a file called `voltage_divider.circ`

```
.title Voltage Divider
* This is a comment line
* There is a voltage source at the input that provides 10V
Vin input 0 dc 10 ac 0
Rt input output 100
Rb output 0 100
.end
```

As can be seen, the voltage divider has an input source, and two resistors across the voltage source, with
the middle node being the output. So far so good, but if we want to know how the output voltage is, ther
is still one more thing to do, which is to tell NGspice what we want it to do with this cirucuit.

To get NGspice to load the circuit, either ngspice can be started with the path to the circuit file as an
argument, or if no argument is usedm by simply calling `ngspice` and when getting to the ngspice prompt calling `source voltage_divider.circ`.

Now that the circuit is loaded, tell it to calculate the steady state voltages. This is called the
'operating point', which is why the command in ngspice is calle `op`. So once the circuit is loaded,
call

``` ngspice 225 -> op ```

ngspice should respond with:

```
Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver

No. of Data Rows : 1
```

showing that it did the analysis and that it produced a single row of data. To show the values it
calculated, the `print` command of ngspice can be used.

``` ngspice 225 -> print output ```

should thus print the output voltage. The unit here is V, but with scientific notation.
And there we go, we have sucessfully run our first simulation.
