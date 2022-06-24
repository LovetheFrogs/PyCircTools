# PyCircTools

PyCircTools is a python package which contains tools to build circuits using python 3. It is a work in progress, and will be updated frequently to add more
modules. 

## Table of contents

- [1. Installing PyCircTools and importing it](#installing-CTools)
- [2. Logic Gates Module](#logic-gates)
    + [2.1. NOT gate](#not-gate)
        * [2.1.1. Attributes](#not-attributes)
        * [2.1.2. Constructor](#not-constructor)
        * [2.1.3. Methods](#not-methods)
    + [2.2. AND gate](#and-gate)
        * [2.2.1. Attributes](#and-attributes)
        * [2.2.2. Constructor](#and-constructor)
        * [2.2.3. Methods](#and-methods)
    + [2.3. NAND gate](#nand-gate)
        * [2.3.1. Attributes](#nand-attributes)
        * [2.3.2. Constructor](#nand-constructor)
        * [2.3.3. Methods](#nand-methods)
    + [2.4. OR gate](#or-gate)
        * [2.4.1. Attributes](#or-attributes)
        * [2.4.2. Constructor](#or-constructor)
        * [2.4.3. Methods](#or-methods)
    + [2.5. XOR gate](#xor-gate)
        * [2.5.1. Attributes](#xor-attributes)
        * [2.5.2. Constructor](#xor-constructor)
        * [2.5.3. Methods](#xor-methods)
    + [2.6. NOR gate](#nor-gate)
        * [2.5.1. Attributes](#nor-attributes)
        * [2.5.2. Constructor](#nor-constructor)
        * [2.5.3. Methods](#nor-methods)
- [3. Multiplexers Module](#multiplexers)
    + [3.1. 2-to-1 Multiplexer](#2-1-mux)
        * [3.1.1. Attributes](#2-1-attributes)
        * [3.1.2. Constructor](#2-1-constructor)
        * [3.1.3. Methods](#2-1-methods)
    + [3.2. 4-to-1 Multiplexer](#4-1-mux)
        * [3.2.1. Attributes](#4-1-attributes)
        * [3.2.2. Constructor](#4-1-constructor)
        * [3.2.3. Methods](#4-1-methods)
    + [3.3. 8-to-1 Multiplexer](#8-1-mux)
        * [3.3.1. Attributes](#8-1-attributes)
        * [3.3.2. Constructor](#8-1-constructor)
        * [3.3.3. Methods](#8-1-methods)
    + [3.4. 16-to-1 Multiplexer](#16-1-mux)
        * [3.4.1. Attributes](#16-1-attributes)
        * [3.4.2. Constructor](#16-1-constructor)
        * [3.4.3. Methods](#16-1-methods)
- [Exceptions](#exceptions)
    + [PyCircTools Exceptions](#ctools-exceptions)
        * [NotTruthValue](#not-truth-value)
    + [Logic gates Exceptions](#logic-gates-exceptions)
        * [NonPositiveInput](#non-positive-input)
        * [NotAnInput](#not-an-input)
    + [Multiplexer](#multiplexers-exceptions)
        * [NonExistingInput](#non-existing-input)
        * [NonExistingControlSignal](#non-existing-control-signal)
- [About](#about)

<a name="installing-CTools"></a>
## Installing PyCircTools and importing it.

To install PyCircTools, use pip by calling the following command:

```
pip install PyCircTools
```
Importing it is as easy as it gets, just insert the line 
```
from PyCircTools.*subpackage* import *modules*
``` 
at the start of your code, and substitute subpackage with the package you want, and modules with the modules you want to import to your project.

<a name="logic-gates"></a>
## Logic Gates Module

Here is an in depth explanation for the PyCircTools.LogicGates module. LogicGates adds implementation for common logic gates used in circuit design. It allows
to create gates with as many inputs as the user decides (except for the NOT gate). For further reference about each of the gates, check its section in 
this README.

<a name="not-gate"></a>
### NOT gate

The **NOT gate** is a simple logic gate which simply inverts the input. It implements the logical negation (¬) and has one input and one output. The NOT 
gate symbol and truth table is shown below.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/174762309-03ead86b-bdb4-4d99-9597-c7d13ac67949.png" alt="NOT gate"></p>

<a name="not-attributes"></a>
#### Attributes

The NOT gate has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | Input of the gate | bool |
| **output** | Output of the gate | bool |

<a name="not-constructor"></a>
#### Constructor

The constructor of the NOT gate has the following format: <br>

<p align="center" style="bold" ><b>Not()</b></p>
Which doesn't take any parameters and returns a NOT gate with its Input set to True and has its output calculated by the not gate <a href="#not-calculate-output">calculate output method)</a>

<a name="not-methods"></a>
#### Methods

The NOT gate has the following methods:

- **get_input():**
Gets the input of the gate. It returns a bool containing the requested value.

- **get_output():**
Gets the output of the gate. It returns a bool containing the requested value.

- **set_input(bool _value_):**
Sets the input of the gate to the truth value _'value'_, which is passed as a parameter.

<a name="not-calculate-output"></a>
- **__calculate_output():**
Private method which calculates the output of the gate. This output is:
```
not(input)
```

<a name="and-gate"></a>
### AND gate

The **AND gate** is a logic gate with two or more inputs that implements the logical conjunction (^). It's output is True only when all the inputs are True. If any of them is set to False, the output will then be False. Below you can find the AND truth table.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/174772306-1a861819-1046-41d4-80d0-f84d58155e99.png" alt="AND gate"></p>

<a name="and-attributes"></a>
#### Attributes

The AND gate has the following attributes:
| Name | Description | Type |
| - | - | - |
| **input** | List of inputs of the gate | List[bool] |
| **output** | Output of the gate | bool |
| **numOfInputs** | Number of inputs of the gate | int |

<a name="and-constructor"></a>
#### Constructor

The constructor of the AND gate has the following format: <br>

<p align="center"><b>And(int <i>inputNumber</i>)</b></p>
Which takes the inputNumber parameter, an integer set to two by default which can be changed to have more inputs to the gate. The Input will be initialized to a list of False values, containing as many values as inputs specified, Output will be calculated by the and gate <a href="#and-calculate-output">calculate output method</a> and numOfInputs will take the same value as the parameter inputNumber.

<a name="and-methods"></a>
#### Methods

- **get_input(int _num_):**
Gets the value of the input _num_. It returns the boolean value in Output[num]
- **get_output():**
Gets the output of the gate. It returns a bool containing the requested value.
- **get_numOfInputs():**
Gets the number of inputs of the gate. It returns an int containing the requested value.
- **set_input(int _num_, bool _value_):**
Sets the input _'num'_ to the truth value _'value'_. Both of them are passed as parameters to the method.
- **add_input():**
Adds a new input to the gate, which defaults to False and updates both output and numOfInputs.
- **remove_input():**
Removes the last input and updates both output and numOfInputs.
<a name="and-calculate-output"></a>
- **__calculate_output():**
Private method which calculates the output of the gate. This output is: 
```
(input_n and input_n+1)
```
for all the inputs of the gate.

<a name="nand-gate"></a>
### NAND gate

The **NAND gate** is a logic gate with two or more inputs which produces a False output only when all of its inputs are True. Its output is True in any other case. In other words, its output is calculated by negating the conjunction of all inputs of the gate. Below you can find the NAND truth table.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/174785289-c57e3f8a-eaf3-4c5c-9dcd-98d83f8b2ce4.png" alt="NAND gate"></p>

<a name="nand-attributes"></a>
#### Attributes

The NAND gate has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | List of inputs of the gate | List[bool] |
| **output** | Output of the gate | bool |
| **numOfInputs** | Number of inputs of the gate | int |

<a name="nand-constructor"></a>
#### Constructor

The constructor of the NAND gate has the following format: <br>

<p align="center"><b>Nand(int <i>inputNumber</i>)</b></p>
Which takes the inputNumber parameter, an integer set to two by default which can be changed to have more inputs to the gate. The Input will be initialized to a list of False values, containing as many values as inputs specified, Output will be calculated by the nand gate <a href="#nand-calculate-output">calculate output method</a> and numOfInputs will take the same value as the parameter inputNumber.

<a name="nand-methods"></a>
#### Methods

- **get_input(int _num_):**
Gets the value of the input _num_. It returns the boolean value in Output[num]
- **get_output():**
Gets the output of the gate. It returns a bool containing the requested value.
- **get_numOfInputs():**
Gets the number of inputs of the gate. It returns an int containing the requested value.
- **set_input(int _num_, bool _value_):**
Sets the input _'num'_ to the truth value _'value'_. Both of them are passed as parameters to the method.
- **add_input():**
Adds a new input to the gate, which defaults to False and updates both output and numOfInputs.
- **remove_input():**
Removes the last input and updates both output and numOfInputs.
<a name="nand-calculate-output"></a>
- **__calculate_output():**
Private method which calculates the output of the gate. This output is 
```
not(input_n and input_n+1) 
```
for all the inputs of the gate.

<a name="or-gate"></a>
### OR gate

The **OR gate** is a logic gate with two or more inputs which implements the logical disjunction (∨). Its output is True if any of the inputs is True, and False only when all the gate's inputs are set to False. Below you can find the OR gate truth table.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/174787252-49747650-4a1c-415e-ae3d-6a42064133b6.png" alt="OR gate"></p>

<a name="or-attributes"></a>
#### Attributes

The OR gate has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | List of inputs of the gate | List[bool] |
| **output** | Output of the gate | bool |
| **numOfInputs** | Number of inputs of the gate | int |

<a name="or-constructor"></a>
#### Constructor

The constructor of the OR gate has the following format: <br>

<p align="center"><b>Or(int <i>inputNumber</i>)</b></p>
Which takes the inputNumber parameter, an integer set to two by default which can be changed to have more inputs to the gate. The Input will be initialized to a list of False values, containing as many values as inputs specified, Output will be calculated by the or gate <a href="#or-calculate-output">calculate output method</a> and numOfInputs will take the same value as the parameter inputNumber.

<a name="or-methods"></a>
#### Methods

- **get_input(int _num_):**
Gets the value of the input _num_. It returns the boolean value in Output[num]
- **get_output():**
Gets the output of the gate. It returns a bool containing the requested value.
- **get_numOfInputs():**
Gets the number of inputs of the gate. It returns an int containing the requested value.
- **set_input(int _num_, bool _value_):**
Sets the input _'num'_ to the truth value _'value'_. Both of them are passed as parameters to the method.
- **add_input():**
Adds a new input to the gate, which defaults to False and updates both output and numOfInputs.
- **remove_input():**
Removes the last input and updates both output and numOfInputs.
<a name="or-calculate-output"></a>
- **__calculate_output():**
Private method which calculates the output of the gate. This output is 
```
(input_n or input_n+1)
```
for all the inputs of the gate.

<a name="xor-gate"></a>
### XOR gate

The **XOR gate**is a logic gate with two or more inputs whose output is True when the number of True inputs is odd. In any other case, the output value is False. Below you can find the OR gate truth table.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/174814299-a7bfc87a-8274-44d7-a4ac-d0845aafca40.png" alt="XOR gate"></p>

<a name="xor-attributes"></a>
#### Attributes

The XOR gate has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | List of inputs of the gate | List[bool] |
| **output** | Output of the gate | bool |
| **numOfInputs** | Number of inputs of the gate | int |

<a name="xor-constructor"></a>
#### Constructor

The constructor of the XOR gate has the following format: <br>

<p align="center"><b>Xor(int <i>inputNumber</i>)</b></p>
Which takes the inputNumber parameter, an integer set to two by default which can be changed to have more inputs to the gate. The Input will be initialized to a list of False values, containing as many values as inputs specified, Output will be calculated by the xor gate <a href="#xor-calculate-output">calculate output method</a> and numOfInputs will take the same value as the parameter inputNumber.

<a name="xor-methods"></a>
#### Methods

- **get_input(int _num_):**
Gets the value of the input _num_. It returns the boolean value in Output[num]
- **get_output():**
Gets the output of the gate. It returns a bool containing the requested value.
- **get_numOfInputs():**
Gets the number of inputs of the gate. It returns an int containing the requested value.
- **set_input(int _num_, bool _value_):**
Sets the input _'num'_ to the truth value _'value'_. Both of them are passed as parameters to the method.
- **add_input():**
Adds a new input to the gate, which defaults to False and updates both output and numOfInputs.
- **remove_input():**
Removes the last input and updates both output and numOfInputs.
<a name="xor-calculate-output"></a>
- **__calculate_output():**
Private method which calculates the output of the gate. This output is 
```
[(input_n and not(input_n+1)) or (not(input_n) and input_n+1)] 
```
for all the inputs of the gate.

<a name="nor-gate"></a>
### NOR gate

The **NOR gate** is a logic gate which can take two or more inputs. Its output is True only when all the inputs are False. If any of the inputs is True, the output will be False. In other words, its output is calculated by negating the disjunction of all inputs of the gate. Below you can find the NOR gate truth table.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/174819379-e17db12b-5324-4145-be96-d4699ed8a03f.png" alt="NOR gate"></p>

<a name="nor-attributes"></a>
#### Attributes

The NOR gate has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | List of inputs of the gate | List[bool] |
| **output** | Output of the gate | bool |
| **numOfInputs** | Number of inputs of the gate | int |

<a name="nor-constructor"></a>
#### Constructor

The constructor of the NOR gate has the following format: <br>

<p align="center"><b>Nor(int <i>inputNumber</i>)</b></p>
Which takes the inputNumber parameter, an integer set to two by default which can be changed to have more inputs to the gate. The Input will be initialized to a list of False values, containing as many values as inputs specified, Output will be calculated by the Nor gate <a href="#nor-calculate-output">calculate output method</a> and numOfInputs will take the same value as the parameter inputNumber.

<a name="nor-methods"></a>
#### Methods

- **get_input(int _num_):**
Gets the value of the input _num_. It returns the boolean value in Output[num]
- **get_output():**
Gets the output of the gate. It returns a bool containing the requested value.
- **get_numOfInputs():**
Gets the number of inputs of the gate. It returns an int containing the requested value.
- **set_input(int _num_, bool _value_):**
Sets the input _'num'_ to the truth value _'value'_. Both of them are passed as parameters to the method.
- **add_input():**
Adds a new input to the gate, which defaults to False and updates both output and numOfInputs.
- **remove_input():**
Removes the last input and updates both output and numOfInputs.
<a name="nor-calculate-output"></a>
- **__calculate_output():**
Private method which calculates the output of the gate. This output is 
```
not(input_n or input_n+1)
```
for all the inputs of the gate.

<a name="multiplexers"></a>
## Multiplexers Module

Here is an in depth explanation for the PyCircTools.Multiplexers module. Multiplexers adds implementation for multiplexers ranging from 2-to-1 to 16-to-1. 
For further reference about each of the multiplexers, check its section in this README.

<a name="2-to-1-mux"></a>
### 2-to-1 Multiplexer

The **2-to-1** Multiplexer adds the implementation for this circuit element. Below you will find a picture depicting this mux and its equation.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/175434169-d87df6e6-0002-40e9-a2a2-5f79e669dc30.png", alt="2-to-1 Multiplexer"></p>

<a name="2-1-attributes"></a>
#### Attributes

The 2-to-1 Multiplexer has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | Input of the multiplexer | list[bool] |
| **set** | Set control signals of the multiplexer | bool |
| **output** | Output of the multiplexer | bool |

Note that for this multiplexer, the number of inputs is two and the number of control signals is one.

<a name="2-1-constructor"></a>
#### Constructor

The constructor of the 2-to-1 Multiplexer has the following format: <br>

<p align="center" style="bold" ><b>Mux2to1()</b></p>
Which doesn't take any parameters and returns a 2-to-1 Multiplexer with its two inputs set to False, its set control signal set to False and output calculated by the 2-to-1 Mux gate <a href="#2-1-cal-output">calculate output method</a>

<a name="2-1-methods"></a>
#### Methods

The 2-to-1 Multiplexer has the following methods:

- **get_input(int _num_):**
Gets the value of the input _num_. It returns the boolean value in input[num].

- **get_set():**
Gets the value of the set control signal. It returns a bool with the requested value.

- **get_output():**
Gets the output of the mux. It returns a bool containing the requested value.

- **set_input(int _num_, bool _value_):**
Sets the input[num] of the mux to the truth value _'value'_, which is passed as a parameter.

- **set_set(bool _value_):**
Sets the value of the set control signal to _'value'_.

<a name="2-1-cal-output"></a>
- **__calculate_output():**
Private method which calculates the output of the mux. This output is showed in <a href="#2-to-1-mux">2-to-1 Multiplexer chapter.</a>

<a name="4-to-1-mux"></a>
### 4-to-1 Multiplexer

The **4-to-1** Multiplexer adds the implementation for this circuit element. Below you will find a picture depicting this mux and its equation.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/175567422-867f9575-1fa2-4e06-af2a-723f05c48155.png", alt="4-to-1 Multiplexer"></p>

<a name="4-1-attributes"></a>
#### Attributes

The 4-to-1 Multiplexer has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | Input of the multiplexer | list[bool] |
| **set** | Set control signals of the multiplexer | list[bool] |
| **output** | Output of the multiplexer | bool |

Note that for this multiplexer, the number of inputs is four and the number of control signals is two.

<a name="4-1-constructor"></a>
#### Constructor

The constructor of the 4-to-1 Multiplexer has the following format: <br>

<p align="center" style="bold" ><b>Mux4to1()</b></p>
Which doesn't take any parameters and returns a 4-to-1 Multiplexer with its four inputs set to False, its set control signals set to False and output calculated by the 4-to-1 Mux gate <a href="#4-1-cal-output">calculate output method</a>

<a name="4-1-methods"></a>
#### Methods

The 4-to-1 Multiplexer has the following methods:

- **get_input(int _num_):**
Gets the value of the input _num_. It returns the boolean value in input[num].

- **get_set(int _setNum_):**
Gets the value of the set control signal _setNum_. It returns a bool with the requested value.

- **get_output():**
Gets the output of the mux. It returns a bool containing the requested value.

- **set_input(int _num_, bool _value_):**
Sets the input[num] of the mux to the truth value _'value'_, which is passed as a parameter.

- **set_set(int _setNum_, bool _value_):**
Sets the value of the set control signal set[setNum] to _'value'_. Both are passed as parameters.

<a name="4-1-cal-output"></a>
- **__calculate_output():**
Private method which calculates the output of the mux. This output is showed in <a href="#4-to-1-mux">4-to-1 Multiplexer chapter.</a>

<a name="8-to-1-mux"></a>
### 8-to-1 Multiplexer

The **8-to-1** Multiplexer adds the implementation for this circuit element. It has 8 inputs and the output value is selected by the input number in the set signal.

<a name="8-1-attributes"></a>
#### Attributes

The 8-to-1 Multiplexer has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | Input of the multiplexer | list[bool] |
| **set** | Set control signals of the multiplexer | list[bool] |
| **output** | Output of the multiplexer | bool |

Note that for this multiplexer, the number of inputs is eight and the number of control signals is three.

<a name="8-1-constructor"></a>
#### Constructor

The constructor of the 8-to-1 Multiplexer has the following format: <br>

<p align="center" style="bold" ><b>Mux8to1()</b></p>
Which doesn't take any parameters and returns an 8-to-1 Multiplexer with its four inputs set to False, its set control signals set to False and output calculated by the 8-to-1 Mux gate <a href="#8-1-cal-output">calculate output method</a>

<a name="8-1-methods"></a>
#### Methods

The 8-to-1 Multiplexer has the following methods:

- **get_input(int _num_):**
Gets the value of the input _num_. It returns the boolean value in input[num].

- **get_set(int _setNum_):**
Gets the value of the set control signal _setNum_. It returns a bool with the requested value.

- **get_output():**
Gets the output of the mux. It returns a bool containing the requested value.

- **set_input(int _num_, bool _value_):**
Sets the input[num] of the mux to the truth value _'value'_, which is passed as a parameter.

- **set_set(int _setNum_, bool _value_):**
Sets the value of the set control signal set[setNum] to _'value'_. Both are passed as parameters.

<a name="8-1-cal-output"></a>
- **__calculate_output():**
Private method which calculates the output of the mux. This output is showed in <a href="#8-to-1-mux">8-to-1 Multiplexer chapter.</a>

<a name="16-to-1-mux"></a>
### 16-to-1 Multiplexer

The **16-to-1** Multiplexer adds the implementation for this circuit element. It has 16 inputs and the output value is selected by the input number in the set signal.

<a name="16-1-attributes"></a>
#### Attributes

The 16-to-1 Multiplexer has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | Input of the multiplexer | list[bool] |
| **set** | Set control signals of the multiplexer | list[bool] |
| **output** | Output of the multiplexer | bool |

Note that for this multiplexer, the number of inputs is sixteen and the number of control signals is four.

<a name="16-1-constructor"></a>
#### Constructor

The constructor of the 8-to-1 Multiplexer has the following format: <br>

<p align="center" style="bold" ><b>Mux16to1()</b></p>
Which doesn't take any parameters and returns a 16-to-1 Multiplexer with its sixteen inputs set to False, its set control signals set to False and output calculated by the 16-to-1 Mux gate <a href="#16-1-cal-output">calculate output method</a>

<a name="16-1-methods"></a>
#### Methods

The 16-to-1 Multiplexer has the following methods:

- **get_input(int _num_):**
Gets the value of the input _num_. It returns the boolean value in input[num].

- **get_set(int _setNum_):**
Gets the value of the set control signal _setNum_. It returns a bool with the requested value.

- **get_output():**
Gets the output of the mux. It returns a bool containing the requested value.

- **set_input(int _num_, bool _value_):**
Sets the input[num] of the mux to the truth value _'value'_, which is passed as a parameter.

- **set_set(int _setNum_, bool _value_):**
Sets the value of the set control signal set[setNum] to _'value'_. Both are passed as parameters.

<a name="16-1-cal-output"></a>
- **__calculate_output():**
Private method which calculates the output of the mux. This output is showed in <a href="#16-to-1-mux">16-to-1 Multiplexer chapter.</a>

<a name="exceptions"></a>
## Exceptions

CTools implements the following Exceptions. They are divided depending on which module they are intended to use.

<a name="ctools-exceptions"></a>
### PyCircTools Exceptions

These are the general Exceptions used all over the PyCircTools library. An explanation of each one follows below.

<a name="not-truth-value"></a>
#### NotTruthValue Exception

NotTruthValue is an exception that raises when an input which is expected to be a truth value (either True or False)
is of another data type.

<a name="logic-gates-exceptions"></a>
### Logic gates Exceptions

These are the exceptions used in the PyCircTools.LogicGates module. An explanation of each one follows below.

<a name="non-positive-input"></a>
#### NonPositiveInput

NonPositiveInput is raised when the number of inputs for a Logic Gate is lower than 1, as this is the minimum number
of inputs of any logic gate.

<a name="not-an-input"></a>
#### NotAnInput

NotAnInput is raised when the selected input does not exist.

<a name="muliplexers-exceptions"></a>
### Multiplexers Exceptions

These are the exceptions used in the PyCircTools.Multiplexers module. An explanation of each one follows below.

<a name="non-existing-input"></a>
#### NonExistingInput

NonExistingInput is raised when a Multiplexer/Demultiplexer doesn't have the input asked for. It can take an int as an input. This input _'requestedInput'_ is the number which caused the exception.

<a name="non-existing-control-signal"></a>
#### NonExistingControlSignal

NonExistingControlSignal is raised when a Multiplexer/Demultiplexer doesn't have the set control signal asked for.

<a name="about"></a>
## About

PyCircTools is software developed by LovetheFrogs and licensed under GPL-3.0 license.

You can donate to me on paypal at [this link](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/lovethefrogs?country.x=ES&locale.x=es_ES) to support the development of my future projects or invite me to a coffee :).
