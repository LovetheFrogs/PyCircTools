# PyCircTools

PyCircTools is a python package which contains tools to build circuits using python 3. It is a work in progress, and will be updated frequently to add more
modules. 

## Table of contents

- [1. Installing PyCircTools and importing it](#installing-CTools)
- [2. Logic Gates Module](#logic-gates)
- [Exceptions](#exceptions)
    
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

<a name="about"></a>
## About

PyCircTools is software developed by LovetheFrogs and licensed under GPL-3.0 license.

You can donate to me on paypal at [this link](https://paypal.me/lovethefrogs?country.x=ES&locale.x=es_ES) to support the development of my future projects or invite me to a coffee :).
