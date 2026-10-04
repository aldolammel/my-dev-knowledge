

MYPY: IGNORING FALSE-POSITIVE ERRORS


    When you face and typing error by MyPy, for example, lay the cursor to the error and way. The hint with the error will pop up:

        E.g.
            "Incompatible types in assignment
            (expression has type 'tuple[tuple[None, _FieldOpts]]')
            Mypy (assignment)"
    
        The error type is between parentheses!



    >> Ignoring a specific error type:
        
        <your code line>  # type: ignore[operator]



    >> Ignoring more than one specific error type:
        
        <your code line>  # type: ignore[assignment, misc]



    >> Ignoring any error type (NOT RECOMMENDED):
        
        <your code line>  # type: ignore