# Exceptions

CTools implements the following Exceptions. They are divided depending on which module they are intended to use.

# Table of contents

+ [PyCircTools Exceptions](#ctools-exceptions)
    * [NotTruthValue](#not-truth-value)
+ [Logic gates Exceptions](#logic-gates-exceptions)
    * [NonPositiveInput](#non-positive-input)
    * [NotAnInput](#not-an-input)
+ [Multiplexers Exceptions](#multiplexers-exceptions)
    * [NonExistingInput](#non-existing-input)
    * [NonExistingControlSignal](#non-existing-control-signal)

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
