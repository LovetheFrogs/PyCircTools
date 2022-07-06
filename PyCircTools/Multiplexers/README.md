<a name="multiplexers"></a>
# Multiplexers Module

Here is an in depth explanation for the PyCircTools.Multiplexers module. Multiplexers adds implementation for multiplexers ranging from 2-to-1 to 16-to-1. 
For further reference about each of the multiplexers, check its section in this README.

# Table of contents

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

<a name="2-to-1-mux"></a>
# 2-to-1 Multiplexer

The **2-to-1** Multiplexer adds the implementation for this circuit element. Below you will find a picture depicting this mux and its equation.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/175434169-d87df6e6-0002-40e9-a2a2-5f79e669dc30.png", alt="2-to-1 Multiplexer"></p>

<a name="2-1-attributes"></a>
## Attributes

The 2-to-1 Multiplexer has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | Input of the multiplexer | list[bool] |
| **set** | Set control signals of the multiplexer | bool |
| **output** | Output of the multiplexer | bool |

Note that for this multiplexer, the number of inputs is two and the number of control signals is one.

<a name="2-1-constructor"></a>
## Constructor

The constructor of the 2-to-1 Multiplexer has the following format: <br>

<p align="center" style="bold" ><b>Mux2to1()</b></p>
Which doesn't take any parameters and returns a 2-to-1 Multiplexer with its two inputs set to False, its set control signal set to False and output calculated by the 2-to-1 Mux gate <a href="#2-1-cal-output">calculate output method</a>

<a name="2-1-methods"></a>
## Methods

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
# 4-to-1 Multiplexer

The **4-to-1** Multiplexer adds the implementation for this circuit element. Below you will find a picture depicting this mux and its equation.

<p align="center"><img src="https://user-images.githubusercontent.com/102818341/175567422-867f9575-1fa2-4e06-af2a-723f05c48155.png", alt="4-to-1 Multiplexer"></p>

<a name="4-1-attributes"></a>
## Attributes

The 4-to-1 Multiplexer has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | Input of the multiplexer | list[bool] |
| **set** | Set control signals of the multiplexer | list[bool] |
| **output** | Output of the multiplexer | bool |

Note that for this multiplexer, the number of inputs is four and the number of control signals is two.

<a name="4-1-constructor"></a>
## Constructor

The constructor of the 4-to-1 Multiplexer has the following format: <br>

<p align="center" style="bold" ><b>Mux4to1()</b></p>
Which doesn't take any parameters and returns a 4-to-1 Multiplexer with its four inputs set to False, its set control signals set to False and output calculated by the 4-to-1 Mux gate <a href="#4-1-cal-output">calculate output method</a>

<a name="4-1-methods"></a>
## Methods

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
# 8-to-1 Multiplexer

The **8-to-1** Multiplexer adds the implementation for this circuit element. It has 8 inputs and the output value is selected by the input number in the set signal.

<a name="8-1-attributes"></a>
## Attributes

The 8-to-1 Multiplexer has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | Input of the multiplexer | list[bool] |
| **set** | Set control signals of the multiplexer | list[bool] |
| **output** | Output of the multiplexer | bool |

Note that for this multiplexer, the number of inputs is eight and the number of control signals is three.

<a name="8-1-constructor"></a>
## Constructor

The constructor of the 8-to-1 Multiplexer has the following format: <br>

<p align="center" style="bold" ><b>Mux8to1()</b></p>
Which doesn't take any parameters and returns an 8-to-1 Multiplexer with its four inputs set to False, its set control signals set to False and output calculated by the 8-to-1 Mux gate <a href="#8-1-cal-output">calculate output method</a>

<a name="8-1-methods"></a>
## Methods

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
# 16-to-1 Multiplexer

The **16-to-1** Multiplexer adds the implementation for this circuit element. It has 16 inputs and the output value is selected by the input number in the set signal.

<a name="16-1-attributes"></a>
## Attributes

The 16-to-1 Multiplexer has the following attributes:

| Name | Description | Type |
| - | - | - |
| **input** | Input of the multiplexer | list[bool] |
| **set** | Set control signals of the multiplexer | list[bool] |
| **output** | Output of the multiplexer | bool |

Note that for this multiplexer, the number of inputs is sixteen and the number of control signals is four.

<a name="16-1-constructor"></a>
## Constructor

The constructor of the 8-to-1 Multiplexer has the following format: <br>

<p align="center" style="bold" ><b>Mux16to1()</b></p>
Which doesn't take any parameters and returns a 16-to-1 Multiplexer with its sixteen inputs set to False, its set control signals set to False and output calculated by the 16-to-1 Mux gate <a href="#16-1-cal-output">calculate output method</a>

<a name="16-1-methods"></a>
## Methods

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
