# Operators.

PyCircTools bundles some operators capable of completing more complex tasks which are often required in more advanced circuits.
To check information about this module, please reffer to this README.

# Table of contents.

- [1. Adder](#adder)
- [2. Subtractor](#subtractor)
- [3. Conversor](#conversor)
- [4. Extender](#extender)
- [5. Shifter](#shifter)
- [6. ALU](#alu)
- [7. Help](#help)

<a name="adder"></a>
## Adder

An adder is a circuit used to add two binary inputs (A and B). It outputs their sum and the resulting carry of the operation.
PyCircTools includes a 1-bit adder module, used for both half and full adders.

To create an adder object, just call the constructor **Adder(full: bool)** and specify if the adder is full by setting the atribute full to True.

Note that a half adder can be convverted to a full one at any given time by calling the function Adder.convert.

To create an n bit adder, connect a half adder's carryOut signal to a full adder's carryIn, and connect the last one carryOut to the next full adder.

<a name="subtractor"></a>
## Subtractor

The subtractor bundled with this library is similar in use to the adder module. It can also be converted between a full and a half one and its methods are the same. Reffer to the DocString of the module for an in-depth explanation of the methods of this module.

<a name="conversor"></a>
## Conversor

Most of today's computers operate using two's complement binary system. In order to simplify the use of this type of binary, PyCircTools includes a module wich can be used to convert from pure binary to two's complement.

Just call **Conversor(length: int)**, with lenght being the number of digits of the input you want converted, write your own input with Converter.set_input and take the output in two's complement.

<a name="extender"></a>
## Extender

An extender is used to extend the length of a binary number by adding ones or two's to its most significant part. PyCircTool's extender is built using the constructor **Extender(into: int, out: int, pure: bool)**, where into is the length of the initial input, out is the desired length of the output, and pure is a boolean which speccifies wheter the input is in pure binary or not (defaults to True).

<a name="shifter"></a>
## Shifter

A shifter is used to move the values inside a number a given number of positions, either to the left or to the right. It is often used when calculating directions inside a CPU.
A PyCircTools' shifter object is created by calling the constructor **Shifter(num: int, pos: int, dirs: bool)**, where num is the length of the number to shift, pos is the number of positions, and dirs is the direction of the shift (False for right and True for left). Intrenally, it uses PyCircTools' DFlipflop module.

<a name="alu"></a>
## ALU

An ALU is one of the most important parts of a computer. It is capable of doing a variety of operations, depending on a control signal.

PyCircTools includes a simple 1-bit ALU, capable of doing and, or comparisons, adding and subtracting. Create a new ALU object by calling **Alu()** and change it's inputs and control signal **Operation** by using the methods inside the module. The quote below is extracted from the ALU's DocString. Please reffer to it for help on the control signals' values.

```
  This control signal is used to select the solution needed. 
  The following lines explain which signal selects which operation.
    False, False -> A and B
    True, False -> A or B
    False, True -> A + B
    True, True -> A - B
  Note that the less significant value is the 0th position of the list and so on.
```

<a name="help"></a>
## Help

Please note this module has a lot of technical information as it is substantially more complex than the ones included in previous updates. For further help, reffer directly to the module's DocString, as they have a deeper explanation of each method.
