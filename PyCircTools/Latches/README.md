# Latches Module.

Here is an in-depth explanation for the PyCircTools.Latches module. Latches adds implementation for the most used latches and flip-flops.
Check this README for further reference.

# Table of contents.

- [1. SR latch](#sr-latch)
    + [1.1. Attributes](#sr-attributes)
    + [1.2. Constructor](#sr-constructor)
    + [1.3. Methods](#sr-methods)
- [2. D latch](#d-latch)
    + [2.1. Attributes](#d-attributes)
    + [2.2. Constructor](#d-constructor)
    + [2.3. Methods](#d-methods)
- [3. SR flip-flop](#sr-flipflop)
- [4. D flip-flop](#d-flipflop)
- [5. JK flip-flop](#jk-flipflop)
    + [5.1. Attributes](#jk-attributes)
    + [5.2. Constructor](#jk-constructor)
    + [5.3. Methods](#jk-methods)
- [6. T flip-flop](#t-flipflop)
    + [6.1. Attributes](#t-attributes)
    + [6.2. Constructor](#t-constructor)
    + [6.3. Methods](#t-methods)

<a name="sr-latch"></a>
## SR Latch

The **SR latch** is also called as Set Reset Latch. This latch affects the outputs as long as the enable is maintained at ‘1’.

<a name="sr-attributes"></a>
### Attributes

The SR latch has the following attributes.

| Name | Description | Type |
| - | - | - |
| **S** | Set input signal | bool |
| **R** | Reset input signal | bool |
| **enable** | Enables the latch | bool |
| **Q** | Output of the latch | bool |
| **Qp** | Complementary of the latch's output | bool |

<a name="sr-constructor"></a>
### Constructor

The constructor of the SR latch has the following format: <br>

<p align="center" style="bold" ><b>SRLatch()</b></p>
Which doesn't take any parameters and returns an SR latch with its inputs and outputs set to False.

<a name="sr-methods"></a>
### Methods

The SR latch has the following methods:

- **get_S():**
Gets the value of the Set input signal. It returns a bool containing the requested value.

- **get_R():**
Gets the value of the Reset input signal. It returns a bool containing the requested value.

- **get_enable():**
Gets the value of the Enable input signal. It returns a bool containing the requested value.

- **get_Q():**
Gets the value of the Q output signal. It returns a bool containing the requested value.

- **get_Qp():**
Gets the value of the Qp output signal. It returns a bool containing the requested value.

- **set_R(bool _value_):**
Sets the Reset signal of the latch to the truth value _'value'_, which is passed as a parameter.

- **set_S(bool _value_):**
Sets the Set signal of the latch to the truth value _'value'_, which is passed as a parameter.

- **set_enable(bool _value_):**
Sets the Enable signal of the latch to the truth value _'value'_, which is passed as a parameter.

- **__calculate_output():**
Private method which calculates both the Q and Qp output of the latch.

<a name="d-latch"></a>
## D Latch

The **D latch** it is also called as Data latch. There is one drawback of SR Latch. That is the next state value can’t be predicted when both the inputs S & R are one. So, we can overcome this difficulty by D latch.

<a name="d-attributes"></a>
### Attributes

The D latch has the following attributes.

| Name | Description | Type |
| - | - | - |
| **D** | Data input signal | bool |
| **enable** | Enables the latch | bool |
| **Q** | Output of the latch | bool |
| **Qp** | Complementary of the latch's output | bool |

<a name="d-constructor"></a>
### Constructor

The constructor of the D latch has the following format: <br>

<p align="center" style="bold" ><b>DLatch()</b></p>
Which doesn't take any parameters and returns a D latch with its inputs and outputs set to False.

<a name="d-methods"></a>
### Methods

The D latch has the following methods:

- **get_D():**
Gets the value of the Data input signal. It returns a bool containing the requested value.

- **get_enable():**
Gets the value of the Enable input signal. It returns a bool containing the requested value.

- **get_Q():**
Gets the value of the Q output signal. It returns a bool containing the requested value.

- **get_Qp():**
Gets the value of the Qp output signal. It returns a bool containing the requested value.

- **set_D(bool _value_):**
Sets the Data signal of the latch to the truth value _'value'_, which is passed as a parameter.

- **set_enable(bool _value_):**
Sets the Enable signal of the latch to the truth value _'value'_, which is passed as a parameter.

- **__calculate_output():**
Private method which calculates both the Q and Qp output of the latch.

<a name="sr-flipflop"></a>
## SR Flip-flop

The **SR flip-flop** is similar to an SR latch. The difference is that it works with a clock signal, but code implementation is nearly the same. You should refer to the SR latch documentation to get information about its methods and attributes.

<a name="d-flipflop"></a>
## D Flip-flop

The **D flip-flop** is similar to a D latch. The difference is that it works with a clock signal, but code implementation is nearly the same. You should refer to the D latch documentation to get information about its methods and attributes.

<a name="jk-flipflop"></a>
## JK Flip-flop

The **JK Flip-flop** s the modified version of SR flip-flop. It operates with only positive clock transitions or negative clock transitions.

<a name="jk-attributes"></a>
### Attributes

The JK flip-flop has the following attributes.

| Name | Description | Type |
| - | - | - |
| **J** | J input signal | bool |
| **K** | K input signal | bool |
| **clock** | Enables the latch | bool |
| **Q** | Output of the latch | bool |
| **Qp** | Complementary of the latch's output | bool |

<a name="jk-constructor"></a>
### Constructor

The constructor of the JK flip-flop has the following format: <br>

<p align="center" style="bold" ><b>JKFlipflop()</b></p>
Which doesn't take any parameters and returns a JK flip-flop with its inputs and outputs set to False.

<a name="jk-methods"></a>
### Methods

The JK flip-flop has the following methods:

- **get_J():**
Gets the value of the J input signal. It returns a bool containing the requested value.

- **get_K():**
Gets the value of the K input signal. It returns a bool containing the requested value.

- **get_clock():**
Gets the value of the clock. It returns a bool containing the requested value.

- **get_Q():**
Gets the value of the Q output signal. It returns a bool containing the requested value.

- **get_Qp():**
Gets the value of the Qp output signal. It returns a bool containing the requested value.

- **set_J(bool _value_):**
Sets the J signal of the flip-flop to the truth value _'value'_, which is passed as a parameter.

- **set_K(bool _value_):**
Sets the K signal of the flip-flop to the truth value _'value'_, which is passed as a parameter.

- **set_clock(bool _value_):**
Sets the clock to the truth value _'value'_, which is passed as a parameter.

- **__calculate_output():**
Private method which calculates both the Q and Qp output of the flip-flop.

