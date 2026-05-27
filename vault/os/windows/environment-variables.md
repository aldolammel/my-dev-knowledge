

WINDOWS: ENVIRONMENT VARIABLES

    Check all environment variables:
        
        # Activate the Virtual Environment (if necessary):
            $ <env_name>\Scripts\activate

        # Check the variables over there:
            $ Get-ChildItem Env:
        
        Add and edit an environment variable:
            $ $env:<VARIABLE_NAME>='<value>'
        
        Delete an environment variable:
            $ Remove-Item Env:<ENVIRONMENT_VARIABLE_NAME>
