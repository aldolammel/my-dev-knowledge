

DJANGO: CREATING GLOBAL VARS THROUGH THE APP

    
    This solution avoid the circular import issue, but for it you need to transform vars in functions! This way, the functions always will be load after the Django main files, avoiding completely "not load error" and "circular import error".


    1) Create a runtime service:
        .../django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/services/appname_runtime.py


    2) Wherever you want to call some "global var", call the runtime service function needed:

        E.g.
            from .services import appname_runtime

            appname_stgs = appname_runtime.stgs()
            ...
            if not appname_runtime.is_something() and ... in fields:
                ...
